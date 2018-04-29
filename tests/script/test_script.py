from datetime import datetime

from unittest import TestCase

from api.config import DATETIME_FORMAT
from script.populate_db import create_random_datetime_string, create_messages, \
    msgs_per_insertion


class ScriptTests(TestCase):
    def test_creates_valid_datetime_string(self):
        datetime_string = create_random_datetime_string()

        assert datetime.strptime(datetime_string, DATETIME_FORMAT)

    def test_create_correct_qty_messages(self):
        created_messages = create_messages(3)

        assert 3 == len(created_messages)

    def test_create_message_with_correct_keys(self):
        created_messages = create_messages(1)

        assert 'timestamp' in created_messages[0]
        assert 'event' in created_messages[0]

    def test_if_qty_msgs_lower_than_insertion_qty(self):
        insertions_list = msgs_per_insertion(total=4, per_insertion=10)

        assert [4] == insertions_list

    def test_if_qty_msgs_is_multiple_of_insertion_qty(self):
        insertions_list = msgs_per_insertion(total=50, per_insertion=25)

        assert [25, 25] == insertions_list

    def test_if_qty_msgs_is_not_multiple_of_insertion_qty(self):
        insertions_list = msgs_per_insertion(total=12, per_insertion=10)

        assert [10, 2] == insertions_list
