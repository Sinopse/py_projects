import os

data_path = os.path.dirname(os.path.realpath(__file__))
# print(data_path)

def generate_inputs():
    for name in os.listdir():
        yield f'{name}'

res = generate_inputs()
