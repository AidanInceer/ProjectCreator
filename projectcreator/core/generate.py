from dataclasses import dataclass
from projectcreator.utils.handlers import PathHandler

@dataclass
class Generate:
    path_handler: PathHandler
    
    def create_project(path_handler: PathHandler):
        output = path_handler.data_path
        print(output)


if __name__ == '__main__':
    gen = Generate()
    x = gen.create_project(path)
    print(x)


