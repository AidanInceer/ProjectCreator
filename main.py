from projectcreator.core.generate import Generate
from projectcreator.utils.handlers import PathHandler, InputHandler
from projectcreator.utils.config import Config


if __name__ == "__main__":
    path_handler = PathHandler()

    path = InputHandler.project_path()
    Generate.root_folder(path)

    project_type = InputHandler.project_type()
    core_config = Config.create_config(path_handler)

    config = Config.select(project_type, core_config)
    generator = Generate(path_handler, config)
    generator.create_directory(config, path)

    # TODO:
    # Choose project type ✅
    # Create base folders ✅
    # Create subfolders ✅
    # Create core files ✅
    # create files in subfolders ✅
    # Choose git distributor (GITHUB, ADO, GITLAB, NONE) ❌
    # Choose Cloud Provider (AWS, GCP, AZURE, NONE) ❌
    # populate required files with necessary info ❌
    # .xyz folders creation /smart file/folder detection (pull from set config list) ❌
    # Command line interface functionailty ❌
    # tree creation of project ❌
    # refactor code ❌
    # doc strings ❌
    # logging ❌
    # dockerise ❌
    # auto fill files with required things ❌
