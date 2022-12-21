import unittest
from projectcreator.utils.config import Config
import pytest


class TestConfig(unittest.TestCase):
    core_config = {
        "flask_project": {"core": "flask_src"},
        "default_project": {"core": "default_src"},
    }

    git_config = {
        "git_provider": {
            "bitbucket": "a",
            "github": "b",
            "azure_devops": "c",
            "gitlab": "d",
            "none": "e",
        }
    }

    cloud_config = {
        "cloud_provider": {"AWS": "a", "GCP": "b", "AZURE": "c", "none": "d"}
    }

    def test_create_config_00(self):
        class PathHandler:
            config_path = "./tests/fixtures/test_config.yaml"

        path_handler = PathHandler()
        assert Config.create_config(path_handler) == {"test_config": ["test"]}

    # project type tests
    def test_select_project_00(self):
        test_type = "FLASK"
        assert Config.select_project(test_type, self.core_config) == "flask_src"

    def test_select_project_01(self):
        test_type = "DEFAULT"
        assert Config.select_project(test_type, self.core_config) == "default_src"

    def test_select_project_02(self):
        with pytest.raises(AssertionError) as _:
            test_type = "test"
            Config.select_project(test_type, self.core_config)

    # git provider tests
    def test_git_provider_00(self):
        test_type = "BITBUCKET"
        assert Config.select_git_provider(test_type, self.git_config) == "a"

    def test_git_provider_01(self):
        test_type = "GITHUB"
        assert Config.select_git_provider(test_type, self.git_config) == "b"

    def test_git_provider_02(self):
        test_type = "ADO"
        assert Config.select_git_provider(test_type, self.git_config) == "c"

    def test_git_provider_03(self):
        test_type = "GITLAB"
        assert Config.select_git_provider(test_type, self.git_config) == "d"

    def test_git_provider_04(self):
        test_type = "NONE"
        assert Config.select_git_provider(test_type, self.git_config) == {}

    def test_git_provider_05(self):
        with pytest.raises(AssertionError) as _:
            test_type = "test"
            Config.select_git_provider(test_type, self.git_config)

    # cloud provider tests
    def test_cloud_provider_00(self):
        test_type = "AWS"
        assert Config.select_cloud_provider(test_type, self.cloud_config) == "a"

    def test_cloud_provider_01(self):
        test_type = "GCP"
        assert Config.select_cloud_provider(test_type, self.cloud_config) == "b"

    def test_cloud_provider_02(self):
        test_type = "AZURE"
        assert Config.select_cloud_provider(test_type, self.cloud_config) == "c"

    def test_cloud_provider_03(self):
        test_type = "NONE"
        assert Config.select_cloud_provider(test_type, self.cloud_config) == {}

    def test_cloud_provider_04(self):
        with pytest.raises(AssertionError) as _:
            test_type = "test"
            Config.select_cloud_provider(test_type, self.cloud_config)
