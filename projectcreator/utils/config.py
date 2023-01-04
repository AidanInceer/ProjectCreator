from dataclasses import dataclass

import yaml
from yaml import SafeLoader

from projectcreator.utils.handlers import PathHandler
from projectcreator.utils.logger import logger


@dataclass
class Config:
    path_handler: PathHandler

    @staticmethod
    def create_config(path_handler: PathHandler):
        with open(path_handler.config_path) as f:
            config = yaml.load(f, Loader=SafeLoader)
        return config

    @staticmethod
    def select_project(project_type: str, core_config):
        if project_type == 'FLASK':
            project_config = core_config['flask_project']['core']
        elif project_type == 'DEFAULT':
            project_config = core_config['default_project']['core']
        elif project_type == 'BASIC':
            project_config = core_config['basic_project']['core']
        else:
            logger.critical('NOT A VALID PROJECT TYPE:')
            raise AssertionError('Incorrect project type')
        return project_config

    @staticmethod
    def select_git_provider(git_type: str, core_config):
        if git_type == 'GITHUB':
            git_config = core_config['git_provider']['github']
        elif git_type == 'ADO':
            git_config = core_config['git_provider']['azure_devops']
        elif git_type == 'GITLAB':
            git_config = core_config['git_provider']['gitlab']
        elif git_type == 'BITBUCKET':
            git_config = core_config['git_provider']['bitbucket']
        elif git_type == 'NONE':
            git_config = {}
        else:
            logger.critical('INVALID GIT PROVIDER')
            raise AssertionError('Incompatible git provider')
        return git_config

    @staticmethod
    def select_cloud_provider(cloud_type: str, core_config):
        if cloud_type == 'AWS':
            cloud_config = core_config['cloud_provider']['AWS']
        elif cloud_type == 'GCP':
            cloud_config = core_config['cloud_provider']['GCP']
        elif cloud_type == 'AZURE':
            cloud_config = core_config['cloud_provider']['AZURE']
        elif cloud_type == 'NONE':
            cloud_config = {}
        else:
            logger.critical('INVALID CLOUD PROVIDER')
            raise AssertionError('Incompatible cloud provider')
        return cloud_config
