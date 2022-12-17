from dataclasses import dataclass
from projectcreator.utils.handlers import PathHandler
import os


@dataclass
class Generate:
    path_handler: PathHandler

    def create_file(self, file_name):
        data_path = self.path_handler.data_path
        path_to_file = data_path + file_name

        with open(path_to_file, "x") as new_file:
            pass

    def create_folder(self):
        data_path = self.path_handler.data_path
