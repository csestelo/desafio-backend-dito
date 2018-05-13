from http import HTTPStatus
from typing import Optional, Dict

from aiohttp import web


def transform_qs_into_dict_params(request) -> Optional[Dict]:
    params_list = request.query_string.split('&')

    if not bool(params_list[0]):
        return

    params_key_value_list = [param.split('=') for param in params_list]

    dict_params = {}
    for key_value_list in params_key_value_list:
        dict_params[key_value_list[0]] = key_value_list[1]

    return dict_params


def validate_schema(request, schema):
    dict_params = transform_qs_into_dict_params(request)

    if not dict_params:
        return {'errors': {'erro': 'Pelo menos um argumento deve ser passado'}}

    data, errors = schema.dump(dict_params)
    if errors:
        return {'errors': {'erro': errors, 'info': 'Parâmetro inválido'}}

    return data


def cintia_args(schema):
    """
    Created as a studying exercise.
    """
    def decorator(decorated_func):
        def get_with_schema(request):
            data = validate_schema(request, schema)
            is_invalid_schema = data.get('errors')

            if is_invalid_schema:
                return web.json_response(data=data,
                                         status=HTTPStatus.UNPROCESSABLE_ENTITY)
            return decorated_func(request, data)

        return get_with_schema

    return decorator
