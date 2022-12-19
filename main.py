from projectcreator.core.generate import Generate
from projectcreator.utils.handlers import PathHandler
from projectcreator.utils.config import Config


if __name__ == "__main__":
    path_handler = PathHandler()
    core_config = Config.create_config(path_handler=path_handler)
    project_type = (
        str(input('Please Choose a project type: "FLASK" or "DEFAULT":  '))
        .upper()
        .strip()
    )
    if project_type == "FLASK":
        config = core_config.flask_project
    else:
        config = core_config.default_project

    generator = Generate(path_handler=path_handler, config=config)
    for folder in config["folder_base"]:
        generator.create_folder(folder_name=folder)

    # TODO:
    # Choose project type ✅
    # Choose git distributor (GITHUB,ADO,GITLAB,NONE) ❌
    # Choose Cloud Provider (AWS,GCP,AZURE,NONE) ❌
    # Create base folders ✅
    # Create subfolders ❌
    # Create core files ❌
    # create files in subfolders ❌
    # populate required files with necessary info ❌
