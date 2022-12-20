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

    def create_config(path_handler: PathHandler) -> DotNotationDict:
        with open(path_handler.config_path) as f:
            base_config = yaml.load(f, Loader=SafeLoader)
        config = DotNotationDict(base_config)
        return config

    def select(project_type: str, core_config):
        if project_type == "FLASK":
            config = core_config.flask_project['core']
        else:
            config = core_config.default_project['core']
        return config
