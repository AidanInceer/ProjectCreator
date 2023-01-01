import unittest

from projectcreator.utils import handlers


class TestHandlers(unittest.TestCase):
    def test_path_handler_00(self):
        test_path = r"./config/config.yaml"
        conf = handlers.PathHandler()
        assert test_path == conf.config_path

    def test_path_handler_01(self):
        test_path = r"test"
        conf = handlers.PathHandler()
        assert test_path != conf.config_path
