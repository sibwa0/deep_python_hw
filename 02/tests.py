import unittest
import unittest.mock
import json
from faker import Faker
from json_process import parse_json, is_valid_income_data, \
    word_process, input_random_names_number


class TestJsonProcess(unittest.TestCase):

    # is_valid_income_data
    # valid
    def test_is_valid_true_income_data_(self):
        required_fields = ["key1", "key2"]
        keywords = ['value1', 'value2']
        json_str = {"female": "Cummings", "male": "Ramirez Sanchez"}
        json_str = json.dumps(json_str)

        self.assertTrue(
            is_valid_income_data(json_str, keywords, required_fields)
        )

    # json_str
    def test_is_valid_income_data_wrong_json(self):
        required_fields = ["key1"]
        keywords = ['value1']
        json_str = {"female": "Cummings", "male": 1}
        json_str = json.dumps(json_str)

        self.assertFalse(
            is_valid_income_data(json_str, keywords, required_fields)
        )

    # required_fields
    def test_is_valid_income_data_wrong_require_fields_list_type(self):
        required_fields = 5
        keywords = ['value1']
        json_str = {"female": "Cummings", "male": "Ramirez"}
        json_str = json.dumps(json_str)

        self.assertFalse(
            is_valid_income_data(json_str, keywords, required_fields)
        )

    def test_is_valid_income_data_wrong_require_fields_elems_type(self):
        required_fields = ["key1", 5]
        keywords = ['value1']
        json_str = {"female": "Cummings", "male": "Ramirez"}
        json_str = json.dumps(json_str)

        self.assertFalse(
            is_valid_income_data(json_str, keywords, required_fields)
        )

    # keywords
    def test_is_valid_income_data_wrong_keywords_list_type(self):
        required_fields = 5
        keywords = ['value1']
        json_str = {"female": "Cummings", "male": "Ramirez"}
        json_str = json.dumps(json_str)

        self.assertFalse(
            is_valid_income_data(json_str, keywords, required_fields)
        )

    def test_is_valid_income_data_wrong_keywords_elems_type(self):
        required_fields = ["key1", "key2"]
        keywords = ['value1', 5]
        json_str = {"female": "Cummings", "male": "Ramirez"}
        json_str = json.dumps(json_str)

        self.assertFalse(
            is_valid_income_data(json_str, keywords, required_fields)
        )

    # word_process
    # person is already in dict
    def test_word_process_is_in_dict(self):
        dct = {"Cummings": 1, "Ramirez": 2}

        old_cnt = len(dct)
        word_process("Cummings", dct)
        new_cnt = len(dct)

        self.assertEqual(old_cnt, new_cnt)

    # person is not in dict
    def test_word_process_not_in_dict(self):
        dct = {"Cummings": 1, "Ramirez": 2}

        old_cnt = len(dct)
        word_process("Sklyannyy", dct)
        new_cnt = len(dct)

        self.assertEqual(old_cnt, new_cnt - 1)

    # parse_json
    # valid
    @unittest.mock.patch("json_process.word_process")
    def test_parse_json(self, word_mock):
        json_str = {"female": "Cummings", "male": "Sklyannyy Ramirez"}
        required_fields = ["female", "male"]
        keywords = ["Cummings", "Sklyannyy", "Ramirez"]
        json_str = json.dumps(json_str)

        word_mock.return_value = None
        parse_json(json_str, word_mock, required_fields, keywords)

        self.assertEqual(word_mock.call_count, 3)

    @unittest.mock.patch("json_process.word_process")
    def test_parse_json_fake_generation(self, word_mock):
        fake = Faker()
        tmp_dct = {
            'female': input_random_names_number(100, fake.last_name_female),
            'male': input_random_names_number(100, fake.last_name_male)
        }

        json_str = json.dumps(tmp_dct)
        required_fields = ["female", "male"]
        keywords = [
            "Cummings", "Thomas", "Day", "Rivera",
            "Barton", "Cruz", "Torres", "Ramirez"
        ]

        word_mock.return_value = None
        parse_json(json_str, word_mock, required_fields, keywords)

        self.assertTrue(word_mock.called)

    # invalid
    @unittest.mock.patch("json_process.is_valid_income_data")
    def test_parse_json_invalid_data(self, is_valid_data_mock):
        json_str = {"female": "Cummings", "male": "Sklyannyy Ramirez"}
        required_fields = ["female", 5]
        keywords = ['Cummings', 'Sklyannyy', 'Ramirez']
        json_str = json.dumps(json_str)

        is_valid_data_mock.return_value = False
        self.assertFalse(
            parse_json(json_str, word_process, required_fields, keywords)
        )

        self.assertTrue(is_valid_data_mock.called)

    def test_parse_json_empty_json(self):
        json_str = {}
        required_fields = ["female", "male"]
        keywords = ['Cummings', 'Sklyannyy', 'Ramirez']
        json_str = json.dumps(json_str)

        self.assertEqual(
            parse_json(json_str, word_process, required_fields, keywords),
            None
        )