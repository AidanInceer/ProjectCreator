import os
import unittest
from unittest.mock import patch

import pytest

from projectcreator.core import generate
from projectcreator.utils import config


class TestGenerate(unittest.TestCase):
    # def setup(self):
    # test_directory = {"src": {"core": "func.py"}}

    def test_root_folder_00(self):
        projectpath = r'.\tests\fixtures'
        projectname = 'root_folder'

        generate.Generate.root_folder(projectpath, projectname)
        output_path = r'.\tests\fixtures\root_folder\\'
        assert os.path.exists(output_path) is True
        rm_path = r'.\tests\fixtures\root_folder'
        os.rmdir(rm_path)

    def test_create_folder_00(self):
        path = r'.\tests\fixtures\\'
        folder_name = 'create_folder'
        generate.Generate.create_folder(path, folder_name)
        output_path = r'.\tests\fixtures\create_folder\\'
        assert os.path.exists(output_path) is True
        rm_path = r'.\tests\fixtures\create_folder'
        os.rmdir(rm_path)

    def test_create_file_00(self):
        path = r'.\tests\fixtures\\'
        file_name = 'file.py'
        generate.Generate.create_folder(path, file_name)
        output_path = r'.\tests\fixtures\file.py'
        assert os.path.exists(output_path) is True
        rm_path = r'.\tests\fixtures\file.py'
        os.rmdir(rm_path)

    def test_is_file_00(self):
        object = None
        assert generate.Generate.is_file(object) == 'None'

    def test_is_file_01(self):
        object = 'file.py'
        assert generate.Generate.is_file(object) is True

    def test_is_file_02(self):
        object = 'folder'
        assert generate.Generate.is_file(object) is False

    @patch('projectcreator.core.generate.Generate.create_folder')
    @patch('projectcreator.core.generate.Generate.create_file')
    def test_create_file_or_folder_00(self, mock_folder, mock_file):
        mock_folder.return_value = 'folder created'
        mock_file.return_value = 'file created'

        class PathHandler:
            config_path = './tests/fixtures/file_or_folder.yaml'

        path_handler = PathHandler()
        conf = config.Config.create_config(path_handler)
        generator = generate.Generate(conf)
        object = '.a'
        dir_path = r'.\tests\fixtures\\'

        assert generator.create_file_or_folder(dir_path, object) is None

    @patch('projectcreator.core.generate.Generate.create_folder')
    @patch('projectcreator.core.generate.Generate.create_file')
    def test_create_file_or_folder_01(self, mock_folder, mock_file):
        mock_folder.return_value = 'folder created'
        mock_file.return_value = 'file created'

        class PathHandler:
            config_path = './tests/fixtures/file_or_folder.yaml'

        path_handler = PathHandler()
        conf = config.Config.create_config(path_handler)
        generator = generate.Generate(conf)
        object = 'a'
        dir_path = r'.\tests\fixtures\\'

        assert generator.create_file_or_folder(dir_path, object) is None

    def test_create_file_or_folder_02(self):
        with pytest.raises(FileExistsError) as _:

            class PathHandler:
                config_path = './tests/fixtures/file_or_folder.yaml'

            path_handler = PathHandler()
            conf = config.Config.create_config(path_handler)
            generator = generate.Generate(conf)
            object = 'fixtures'
            dir_path = r'.\tests\\'
            generator.create_file_or_folder(dir_path, object)

    @patch('projectcreator.core.generate.Generate.create_folder')
    @patch('projectcreator.core.generate.Generate.create_file')
    def test_create_file_or_folder_03(self, mock_folder, mock_file):
        mock_folder.return_value = 'folder created'
        mock_file.return_value = 'file created'

        class PathHandler:
            config_path = './tests/fixtures/file_or_folder.yaml'

        path_handler = PathHandler()
        conf = config.Config.create_config(path_handler)
        generator = generate.Generate(conf)
        object = None
        dir_path = r'.\tests\fixtures\\is_file\\'
        assert generator.create_file_or_folder(dir_path, object) is None
