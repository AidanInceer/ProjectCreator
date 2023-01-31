import os
import unittest
from unittest.mock import MagicMock, patch

import pytest

from projectcreator.core.generate import Generate
from projectcreator.utils import config


class TestGenerateCreateDir(unittest.TestCase):
    generate = Generate(config={})

    @patch.object(Generate, "create_file_or_folder")
    def test_create_directory_00(self, mock_create_file_or_folder):
        directory = {
            "folder1": {"folder2": ["file1", "file2"], "file3": None},
            "file4": None,
        }
        path = ".\\tests\\fixtures\\"
        self.generate.create_directory(directory, path)

        # Assert that the create_file_or_folder
        # method was called with the correct arguments
        expected_calls = [
            # for folder1
            unittest.mock.call(".\\tests\\fixtures\\", "folder1"),
            # for folder2
            unittest.mock.call(".\\tests\\fixtures\\folder1\\\\", "folder2"),
            # for file1
            unittest.mock.call(".\\tests\\fixtures\\folder1\\\\folder2\\\\", "file1"),
            # for file2
            unittest.mock.call(".\\tests\\fixtures\\folder1\\\\folder2\\\\", "file2"),
            # for file3
            unittest.mock.call(".\\tests\\fixtures\\folder1\\\\", "file3"),
            unittest.mock.call(".\\tests\\fixtures\\folder1\\\\file3\\\\", None),
            # for file4
            unittest.mock.call(".\\tests\\fixtures\\", "file4"),
            unittest.mock.call(".\\tests\\fixtures\\file4\\\\", None),
        ]
        mock_create_file_or_folder.assert_has_calls(expected_calls)

    @patch.object(Generate, "create_file_or_folder")
    def test_create_directory_01(self, mock_create_file_or_folder):
        directory = [
            {"folder1": "file1"},
            {"folder2": "file2"},
        ]
        path = ".\\tests\\fixtures\\"
        self.generate.create_directory(directory, path)

        # Assert that the create_file_or_folder method
        # was called with the correct arguments
        expected_calls = [
            unittest.mock.call(".\\tests\\fixtures\\", "folder1"),
            unittest.mock.call(".\\tests\\fixtures\\folder1\\\\", "file1"),
            unittest.mock.call(".\\tests\\fixtures\\", "folder2"),
            unittest.mock.call(".\\tests\\fixtures\\folder2\\\\", "file2"),
        ]
        mock_create_file_or_folder.assert_has_calls(expected_calls)


class TestGenerate(unittest.TestCase):
    # def test_root_folder_00(self):
    #     projectpath = r".\tests\fixtures"
    #     projectname = "root_folder"

    #     Generate.root_folder(projectpath, projectname)
    #     output_path = r".\tests\fixtures\root_folder\\"
    #     assert os.path.exists(output_path) is True
    #     rm_path = r".\tests\fixtures\root_folder"
    #     os.rmdir(rm_path)

    # def test_create_folder_00(self):
    #     path = r".\tests\fixtures\\"
    #     folder_name = "create_folder"
    #     Generate.create_folder(path, folder_name)
    #     output_path = r".\tests\fixtures\create_folder\\"
    #     assert os.path.exists(output_path) is True
    #     rm_path = r".\tests\fixtures\create_folder"
    #     os.rmdir(rm_path)

    def test_create_file_00(self):
        path = r".\tests\fixtures\\"
        file_name = "file.py"
        Generate.create_folder(path, file_name)
        output_path = r".\tests\fixtures\file.py"
        assert os.path.exists(output_path) is True
        rm_path = r".\tests\fixtures\file.py"
        os.rmdir(rm_path)

    def test_is_file_00(self):
        object = None
        assert Generate.is_file(object) == "None"

    def test_is_file_01(self):
        object = "file.py"
        assert Generate.is_file(object) is True

    def test_is_file_02(self):
        object = "folder"
        assert Generate.is_file(object) is False

    @patch("projectcreator.core.generate.Generate.create_folder")
    @patch("projectcreator.core.generate.Generate.create_file")
    def test_create_file_or_folder_00(self, mock_folder, mock_file):
        mock_folder.return_value = "folder created"
        mock_file.return_value = "file created"

        class PathHandler:
            config_path = "./tests/fixtures/file_or_folder.yaml"

        path_handler = PathHandler()
        conf = config.Config.create_config(path_handler)
        generator = Generate(conf)
        object = ".a"
        dir_path = r".\tests\fixtures\\"

        assert generator.create_file_or_folder(dir_path, object) is None

    @patch("projectcreator.core.generate.Generate.create_folder")
    @patch("projectcreator.core.generate.Generate.create_file")
    def test_create_file_or_folder_01(self, mock_folder, mock_file):
        mock_folder.return_value = "folder created"
        mock_file.return_value = "file created"

        class PathHandler:
            config_path = "./tests/fixtures/file_or_folder.yaml"

        path_handler = PathHandler()
        conf = config.Config.create_config(path_handler)
        generator = Generate(conf)
        object = "a"
        dir_path = r".\tests\fixtures\\"

        assert generator.create_file_or_folder(dir_path, object) is None

    # def test_create_file_or_folder_02(self):
    #     with pytest.raises(FileExistsError) as _:

    #         class PathHandler:
    #             config_path = "./tests/fixtures/file_or_folder.yaml"

    #         path_handler = PathHandler()
    #         conf = config.Config.create_config(path_handler)
    #         generator = Generate(conf)
    #         object = "fixtures"
    #         dir_path = r".\tests\\"
    #         generator.create_file_or_folder(dir_path, object)

    @patch("projectcreator.core.generate.Generate.create_folder")
    @patch("projectcreator.core.generate.Generate.create_file")
    def test_create_file_or_folder_03(self, mock_folder, mock_file):
        mock_folder.return_value = "folder created"
        mock_file.return_value = "file created"

        class PathHandler:
            config_path = "./tests/fixtures/file_or_folder.yaml"

        path_handler = PathHandler()
        conf = config.Config.create_config(path_handler)
        generator = Generate(conf)
        object = None
        dir_path = r".\tests\fixtures\\is_file\\"
        assert generator.create_file_or_folder(dir_path, object) is None


class TestGenerateCreateFile(unittest.TestCase):
    def setUp(self):
        self.generate = Generate(config={"boilerplate_files": ["file1", "file2"]})

    # @patch('builtins.open')
    # def test_create_file_00(self, mock_open):
    #     path = 'C:\\test\\'
    #     file_name = 'file1'
    #     expected_file_path = path + file_name
    #     expected_data = ['line1', 'line2']
    #     mock_open.side_effect = [
    #         unittest.mock.mock_open(read_data='\n'.join(expected_data)).return_value,
    #         unittest.mock.mock_open().return_value,
    #     ]
    #     self.generate.create_file(path, file_name)
    #     expected_calls = [
    #         unittest.mock.call(f'./data/{file_name}', 'r'),
    #         unittest.mock.call(expected_file_path, 'w'),
    #     ]
    #     mock_open.assert_has_calls(expected_calls)

    @patch("builtins.open")
    def test_create_file_01(self, mock_open):
        path = "C:\\test\\"
        file_name = "file3"
        expected_data = ["line1", "line2"]
        mock_open.side_effect = [
            unittest.mock.mock_open(read_data="\n".join(expected_data)).return_value,
            unittest.mock.mock_open().return_value,
        ]
        self.generate.create_file(path, file_name)
        expected_calls = [unittest.mock.call("C:\\test\\file3", "x")]
        mock_open.assert_has_calls(expected_calls)

    @patch("builtins.open")
    def test_create_file_none_file_name(self, mock_open):
        path = "C:\\test\\"
        file_name = None
        self.generate.create_file(path, file_name)
        mock_open.assert_not_called()
