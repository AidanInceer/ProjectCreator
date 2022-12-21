from projectcreator.core.generate import Generate
from projectcreator.utils.handlers import PathHandler, InputHandler
from projectcreator.utils.config import Config

# TODO:
# Choose project type ✅
# Create base folders ✅
# Create subfolders ✅
# Create core files ✅
# create files in subfolders ✅
# Choose git distributor (GITHUB, ADO, GITLAB, NONE) ✅
# Choose Cloud Provider (AWS, GCP, AZURE, NONE) ✅
# .xyz folders creation /smart file/folder detection (pull from set config list) ✅

# Command line interface functionailty ❌
# tree creation of project ❌
# refactor code ➡️
# doc strings ❌
# logging ❌
# dockerise ❌
# auto fill files with required things ❌


if __name__ == "__main__":
    # Initialize classes and variables:
    path_handler = PathHandler()

    # Generate deisred project path:
    path = InputHandler.project_path()
    Generate.root_folder(path)

    # Set project type:
    project_type = InputHandler.project_type()
    core_config = Config.create_config(path_handler)
    project_config = Config.select_project(project_type, core_config)

    # Set git provider:
    git_provider = InputHandler.git_provider()
    git_config = Config.select_git_provider(git_provider, core_config)

    # Set cloud provider:
    cloud_provider = InputHandler.cloud_provider()
    cloud_config = Config.select_cloud_provider(cloud_provider, core_config)

    # build project directory:
    project_generator = Generate(path_handler, core_config)
    project_generator.create_directory(project_config, path)

    # build git provider additions:
    git_generator = Generate(path_handler, core_config)
    git_generator.create_directory(git_config, path)

    # build cloud provider additions:
    git_generator = Generate(path_handler, core_config)
    git_generator.create_directory(cloud_config, path)
