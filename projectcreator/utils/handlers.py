from dataclasses import dataclass


@dataclass
class PathHandler:
    data_path = r"./data/"
    config_path = r"./config/config.yaml"


@dataclass
class InputHandler:
    @staticmethod
    def project_path():
        project_name = (
            str(input('Please input a project name: '))
            .strip()
        )
        project_location = (
            str(input('Please input the absolute path to the project: '))
            .strip()
        )
        return project_location + r'\\' + project_name + r'\\'

    @staticmethod
    def project_type():
        project_type = (
            str(input('Please Choose a project type: "FLASK" or "DEFAULT": '))
            .upper()
            .strip()
        )
        return project_type
