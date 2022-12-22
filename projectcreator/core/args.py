from argparse import ArgumentParser


def get_arguments() -> ArgumentParser:
    parser = ArgumentParser(
        description="Please enter: project name, path, project type, git_provider and cloud provider"
    )
    parser.add_argument(
        "-n",
        "--projectname",
        help="Sets the root folder name of the project.",
        metavar="",
        required=True,
    )
    parser.add_argument(
        "-p",
        "--projectpath",
        help="Sets Absolute path of project. e.g. 'c:/Users/projects'. ",
        metavar="",
        required=True,
    )
    parser.add_argument(
        "-t",
        "--projecttype",
        help="Sets the project type, choose from the following options: 'default', 'flask'. ",
        metavar="",
        required=True,
    )
    parser.add_argument(
        "-g",
        "--gitprovider",
        help="Sets the git provider for the project, choose from the following options: 'github', 'gitlab', 'ADO','bitbucket', 'none'.",
        metavar="",
        required=True,
    )
    parser.add_argument(
        "-c",
        "--cloudtype",
        help="Sets the cloud provider for the project, choose from the following options: 'aws', 'gcp','azure', 'none'.",
        metavar="",
        required=True,
    )
    return parser.parse_args()
