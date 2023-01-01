import os
from dataclasses import dataclass

from projectcreator.utils.config import Config
from projectcreator.utils.logger import logger
from projectcreator.utils.type import is_dict, is_list


@dataclass
class Generate:
    config: Config

    def create_directory(self, directory: str | list | dict, path: str) -> None:
        if is_dict(directory):
            for k, v in directory.items():
                self.create_file_or_folder(path, k)
                current_depth_path = path
                path = path + k + r'\\'
                if is_dict(v):
                    self.create_directory(v, path)
                elif is_list(v):
                    for i in v:
                        self.create_directory(i, path)
                else:
                    self.create_file_or_folder(path, v)
                path = current_depth_path
        elif is_list(directory):
            for file_or_folder in directory:
                self.create_directory(file_or_folder, path)
        else:
            self.create_file_or_folder(path, directory)

    def create_file_or_folder(self, dir_path: str, object: str | list | dict) -> None:
        folders = self.config['file_to_folders']
        files = self.config['folder_to_files']

        # Does the path exists allready?
        if os.path.exists(f'{dir_path}{object}'):
            pass

        # Does the object follow dot notation file rules
        if object in folders:
            self.create_folder(dir_path, object)
        elif object in files:
            self.create_file(dir_path, object)

        # Default file/folder check
        else:
            if self.is_file(object) == 'None':
                pass
            if self.is_file(object):
                self.create_file(dir_path, object)
            else:
                self.create_folder(dir_path, object)

    @staticmethod
    def is_file(object: str | list | dict | None) -> bool:
        if object is None:
            return 'None'
        elif '.' in object:
            return True
        else:
            return False

    @staticmethod
    def create_folder(path: str, folder_name: str) -> str:
        logger.debug(f'creating folder: {path}{folder_name}')
        folder_path = path + folder_name
        os.mkdir(folder_path)

    def create_file(self, path: str, file_name: str) -> str:
        logger.debug(f'creating file: {path}{file_name}')
        if file_name is not None:
            boilerplate_files = self.config['boilerplate_files']
            file_path = path + file_name
            if file_name in boilerplate_files:
                with open(f'./data/{file_name}', 'r') as r_file:
                    data = r_file.readlines()
                with open(file_path, 'w') as w_file:
                    w_file.writelines(data)
            else:
                with open(file_path, 'x') as _:
                    pass
        else:
            pass

    @staticmethod
    def root_folder(project_path: str, project_name: str) -> None:
        path = project_path + '\\' + project_name + '\\'
        os.mkdir(f'{path}')
        return path
