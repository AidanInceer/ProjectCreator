from argparse import ArgumentParser


def get_arguments() -> ArgumentParser:
    parser = ArgumentParser(
        description="Please enter: project name, path, project type, git_provider and cloud provider"
    )
    parser.add_argument(
        "-n",
        "--projectname",
        help="Set the root folder name of the project.",
        metavar="",
        required=True,
    )
    parser.add_argument(
        "-p",
        "--projectpath",
        help="Sets Absolute path of project.",
        metavar="",
        required=True,
    )
    parser.add_argument(
        "-t",
        "--projecttype",
        help="Sets the project type e.g. 'default', 'flask' etc.",
        metavar="",
        required=True,
    )
    parser.add_argument(
        "-g",
        "--gitprovider",
        help="Sets the git provider for the project e.g. 'github', 'gitlab', 'none' etc",
        metavar="",
        required=True,
    )
    parser.add_argument(
        "-c",
        "--cloudprovider",
        help="Sets the cloud provider for the project e.g. 'aws', 'gcp', 'none etc",
        metavar="",
        required=True,
    )
    return parser.parse_args()
