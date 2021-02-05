import os

data_path = os.path.dirname(os.path.realpath(__file__))
# print(data_path)


class DataInput:
    def __init__(self, path):
        self.path = path

# probably should filter out non-image formats (search for file extension)
# or let user specify which formats to skip

    @classmethod
    def generate_inputs(cls, path):
        for name in os.listdir():
            yield cls(name)

# a string representaion of a path
    def __repr__(self):
        return f'"{self.path}"'


def generate_path_names(input_class, path):
    path = input_class.generate_inputs(path)
    return path
    # for i in path:
    #     print(f'"{i}"')

res = generate_path_names(DataInput, data_path)
# for i in res:
#     print(list(i))
