from asynctest import TestCase, Mock, patch

from api.decorator import validate_schema
from api.schemas import GetSchema


class ValidateSchemaTests(TestCase):
    def _request(self, split_qs):
        return Mock(query_string=Mock(split=Mock(return_value=split_qs)))

    def test_dont_receive_any_query_string(self):
        expected_error = {'erro': 'Pelo menos um argumento deve ser passado'}

        data = validate_schema(request=self._request(['']), schema=GetSchema())

        assert expected_error == data['errors']

    def test_receive_valid_query_string(self):
        qs = ['event_startswith=ba']
        expected_data = {'event_startswith': 'ba'}

        data = validate_schema(request=self._request(qs), schema=GetSchema())

        assert not data.get('errors')
        assert expected_data == data

    def test_receive_unmapped_query_string(self):
        qs = ['event_startswith=ba', 'fake_qs=any']
        expected_data = {'event_startswith': 'ba'}

        data = validate_schema(request=self._request(qs), schema=GetSchema())

        assert not data.get('errors')
        assert expected_data == data

    def test_receive_query_string_with_unexpected_type(self):
        with patch('api.decorator.transform_qs_into_dict_params',
                   return_value={'event_startswith': 5}):

            data = validate_schema(request=Mock(), schema=GetSchema())

            assert {'event_startswith': '5'} == data

    def test_receive_error_in_schemas_validation(self):
        expected_error = {'erro': 'invalid qs', 'info': 'Parâmetro inválido'}

        with patch('api.decorator.transform_qs_into_dict_params',
                   return_value={'event_startswith': 5}),\
             patch.object(GetSchema, 'dump', return_value=({}, 'invalid qs')):

            data = validate_schema(request=Mock(), schema=GetSchema())

            assert expected_error == data['errors']
