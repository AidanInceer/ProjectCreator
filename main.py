from projectcreator.core.generate import Generate
from projectcreator.utils.handlers import PathHandler
from projectcreator.utils.config import Config


if __name__ == "__main__":

    data_path = PathHandler()
    generator = Generate(path_handler=data_path)
    config = Config.create_config()

    for file in config.core_files:
        generator.create_file(file_name=file)
