from projectcreator.core.generate import Generate
from projectcreator.utils.handlers import PathHandler
from projectcreator.utils.config import Config
from projectcreator.core.args import get_arguments
import os


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

    # Sets git provider:
    git_provider = args.gitprovider.upper()
    git_config = Config.select_git_provider(git_provider, core_config)

    # Sets cloud provider:
    cloud_provider = args.cloudprovider.upper()
    cloud_config = Config.select_cloud_provider(cloud_provider, core_config)

    # Builds project directory:
    project_generator = Generate(path_handler, core_config)
    project_generator.create_directory(project_config, path)

    # Builds git provider additions:
    git_generator = Generate(path_handler, core_config)
    git_generator.create_directory(git_config, path)

    # Builds cloud provider additions:
    git_generator = Generate(path_handler, core_config)
    git_generator.create_directory(cloud_config, path)

    # Print created tree
    print("===========================================")
    print(f"Directory {args.projectname} created at: {args.projectpath}")
    os.system(rf"tree {path} /f")
