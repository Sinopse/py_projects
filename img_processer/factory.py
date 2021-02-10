from generate_path import DataInput
from object_3 import ConfigData
from pathlib import Path
import time

def test():

    print("Please, specify target folder: ")
    target = Path(input())

    print("Please, specify destination folder: ")
    destination = Path(input())

    print(target)
    formats = "JPEG", "PNG"
    data = ConfigData()
    print("Please, specify how many regions: ")
    regions = int(input())

    for i in range(regions):

            print(f"Enter parameters for region{i + 1}: ")
            rect = (tuple(int(x) for x in input("Enter rectangle area:\n").split(', ')))
            print("Enter grayscale value: ")
            print("Hint: e.g. gray4")
            grayscale = input()
            data.add_params(f"region{i + 1}", rect, grayscale)

    for k, v in data._regions.items():
        print(k, v)

    while True:
        query = input("Are the defined regions correct? Answer \"y\" or \"n\":\n")
        if query == "Y" or "y":
            break
        elif query == "N" or "n":
            test()
        else:
            exit()

    data_input = DataInput(target=target, destination=destination, **data._regions)
    print(data_input.__dict__.keys())
    # for key, value in data_input.__dict__:
    #     print


    generator = data_input.generate_inputs()
    processor = data_input.process(target, destination, generator, data._regions)  # supply self.__dict__
    print(f'Processed {len(processor)} image(s)\n')

    print("Operation success")
    print("Have a nice day")
    print("Program will exit automatically")
    time.sleep(5)
    return 0

if __name__ == "__main__":
    test()