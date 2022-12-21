from dataclasses import dataclass
from projectcreator.utils.handlers import PathHandler
import yaml
from yaml import SafeLoader


class DotNotationDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


@dataclass
class Config:
    path_handler: PathHandler

    @staticmethod
    def create_config(path_handler: PathHandler) -> DotNotationDict:
        with open(path_handler.config_path) as f:
            base_config = yaml.load(f, Loader=SafeLoader)
        config = DotNotationDict(base_config)
        return config

    @staticmethod
    def select_project(project_type: str, core_config):
        if project_type == "FLASK":
            project_config = core_config.flask_project["core"]
        else:
            project_config = core_config.default_project["core"]
        return project_config

    @staticmethod
    def select_git_provider(git_type: str, core_config):
        if git_type == "GITHUB":
            git_config = core_config.git_provider["github"]
        elif git_type == "ADO":
            git_config = core_config.git_provider["azure_devops"]
        elif git_type == "GITLAB":
            git_config = core_config.git_provider["gitlab"]
        elif git_type == "NONE":
            git_config = {}
        return git_config

    @staticmethod
    def select_cloud_provider(cloud_type: str, core_config):
        if cloud_type == "AWS":
            cloud_config = core_config.cloud_provider["AWS"]
        elif cloud_type == "GCP":
            cloud_config = core_config.cloud_provider["GCP"]
        elif cloud_type == "AZURE":
            cloud_config = core_config.cloud_provider["AZURE"]
        elif cloud_type == "NONE":
            cloud_config = {}
        return cloud_config
