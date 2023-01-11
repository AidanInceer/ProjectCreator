import os

from projectcreator.core.generate import Generate
from projectcreator.utils.config import Config
from projectcreator.utils.handlers import PathHandler
from projectcreator.utils.logger import logger

if __name__ == '__main__':
    # Initialize classes and variables:
    project_path = str(
        input(
            'Please enter the absolute path where you want to project to be created e.g C:/Users/ : '
        )
    )
    project_name = str(input('Please enter a project name e.g. example_project : '))
    project_type = str(
        input(
            'Please choose a project type from the following list (default, flask, basic, frontend): '
        )
    )
    git_provider = str(
        input(
            'Please choose a git provider from the following list (github, gitlab, ADO, bitbucket, none): '
        )
    ).upper()
    cloud_provider = str(
        input(
            'Please choose a cloud provider from the following list (AWS, GCP, AZURE, none): '
        )
    ).upper()
    path_handler = PathHandler()

    # Generate deisred project path:
    path = Generate.root_folder(project_path, project_name)

    # Sets project type:
    project_type = project_type.upper()
    core_config = Config.create_config(path_handler)
    project_config = Config.select_project(project_type, core_config)
    logger.info(f'Setting project type: {project_type}')

    # Sets git provider:
    git_config = Config.select_git_provider(git_provider, core_config)
    logger.info(f'Setting git provider: {git_provider}')

    # Sets cloud provider:
    cloud_config = Config.select_cloud_provider(cloud_provider, core_config)
    logger.info(f'Setting cloud provider: {cloud_provider}')

    # Builds project directory:
    logger.info(f'Building {project_name.title()} directory...')
    project_generator = Generate(core_config)
    project_generator.create_directory(project_config, path)

    # Builds git provider additions:
    git_generator = Generate(core_config)
    git_generator.create_directory(git_config, path)
    logger.info(
        f'Adding {git_provider} files/folders to {project_name.title()} directory...'
    )

    # Builds cloud provider additions:
    cloud_generator = Generate(core_config)
    cloud_generator.create_directory(cloud_config, path)
    logger.info(
        f'Adding {cloud_provider} files/folders to {project_name.title()} directory...'
    )
    os.system(f'code {path}')
