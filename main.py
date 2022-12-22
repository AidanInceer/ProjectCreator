import os

from projectcreator.core.args import get_arguments
from projectcreator.core.generate import Generate
from projectcreator.utils.config import Config
from projectcreator.utils.handlers import PathHandler
from projectcreator.utils.logger import logger

if __name__ == "__main__":
    # Initialize classes and variables:
    path_handler = PathHandler()
    args = get_arguments()

    # Generate deisred project path:
    path = Generate.root_folder(args)

    # Sets project type:
    project_type = args.projecttype.upper()
    core_config = Config.create_config(path_handler)
    project_config = Config.select_project(project_type, core_config)
    logger.info(f"Setting project type: {project_type}")

    # Sets git provider:
    git_provider = args.gitprovider.upper()
    git_config = Config.select_git_provider(git_provider, core_config)
    logger.info(f"Setting git provider: {git_provider}")

    # Sets cloud provider:
    cloud_provider = args.cloudtype.upper()
    cloud_config = Config.select_cloud_provider(cloud_provider, core_config)
    logger.info(f"Setting cloud provider: {cloud_provider}")

    # Builds project directory:
    logger.info(f"Building {args.projectname.title()} directory...")
    project_generator = Generate(core_config)
    project_generator.create_directory(project_config, path)

    # Builds git provider additions:
    git_generator = Generate(core_config)
    git_generator.create_directory(git_config, path)
    logger.info(
        f"Adding {git_provider} files/folders to {args.projectname.title()} directory..."
    )

    # Builds cloud provider additions:
    cloud_generator = Generate(core_config)
    cloud_generator.create_directory(cloud_config, path)
    logger.info(
        f"Adding {cloud_provider} files/folders to {args.projectname.title()} directory..."
    )
    os.system(f"code {path}")
