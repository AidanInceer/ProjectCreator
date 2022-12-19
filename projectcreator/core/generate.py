from dataclasses import dataclass
from projectcreator.utils.handlers import PathHandler
from projectcreator.utils.config import Config
import os


@dataclass
class Generate:
    path_handler: PathHandler  # TODO: replace with directory
    config: Config

    def create_folder(self, folder_name: str | dict) -> None:
        directory = self.path_handler.data_path
        if isinstance(folder_name, dict):
            folder_name = list(folder_name.keys())[0]
        path_to_folder = directory + folder_name
        os.mkdir(path_to_folder)

    def create_file(self, file_name: str) -> None:
        directory = self.path_handler.data_path
        path_to_file = directory + file_name

        with open(path_to_file, "x") as new_file:
            pass
