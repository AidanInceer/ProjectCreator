from dataclasses import dataclass
import yaml
from yaml import SafeLoader


class DotNotationDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


@dataclass
class Config:
    def create_config() -> DotNotationDict:
        with open("config/base.yaml") as f:
            base_config = yaml.load(f, Loader=SafeLoader)
        config = DotNotationDict(base_config)
        return config
