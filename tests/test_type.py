import unittest
from projectcreator.utils import type


class TestType(unittest.TestCase):
    def test_is_dict_00(self):
        object = {"a": "1"}
        assert type.is_dict(object) is True

    def test_is_dict_01(self):
        object = ["1", "2", "3"]
        assert type.is_dict(object) is False

    def test_is_dict_02(self):
        object = "string"
        assert type.is_dict(object) is False

    def test_is_list_00(self):
        object = {"a": "1"}
        assert type.is_list(object) is False

    def test_is_list_01(self):
        object = ["1", "2", "3"]
        assert type.is_list(object) is True

    def test_is_list_02(self):
        object = "string"
        assert type.is_list(object) is False

    def test_is_str_00(self):
        object = {"a": "1"}
        assert type.is_str(object) is False

    def test_is_str_01(self):
        object = ["1", "2", "3"]
        assert type.is_str(object) is False

    def test_is_str_02(self):
        object = "string"
        assert type.is_str(object) is True
