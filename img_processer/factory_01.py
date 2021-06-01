# image converter by Alexander Tarasov
# requests and contact: aleksander.tarasov@gmail.com
#
#
# 11-02-2021 version 0.1
#
#
#

from generate_path import DataInput
from object_3 import ConfigData
from pathlib import Path
import time
import draw_rect

#FORMATS = ("JPEG", "PNG")
formats = "JPEG", "PNG"
# if user closes img window before selecting regions
if draw_rect.trigger:
    exit()

# a simple interface to interact with user
def test():
    # check if the specified paths are viable
    target = draw_rect.target  # from draw_direct
    # target = Path(input('* Please, specify target folder:\n'))
    # while not target.exists():
    #     print('* The specified directory doesn\'t exist, try again:')
    #     target = Path(input("Please, specify target folder:\n"))

    destination = Path(input('* Please, specify destination folder:\n'))
    while not destination.exists():
        print('* The specified directory doesn\'t exist, try again:')
        destination = Path(input("Please, specify destination folder:\n"))

    print(f'* Available image formats are: {formats}')

    # calling data constructor
    data = ConfigData()
    #regions = int(input('* Please, specify how many regions to process:\n')) # old version
    regions = len(draw_rect.points)
    rect = draw_rect.points # convert to tuple?
    # here comes the image prompt
    if 0 < regions:
        for i in range(regions):
            try:
                # print(f'* Enter parameters for \"region{i + 1}\":')
                # # introduce a while loop to control the input
                # rect = input('* Enter rectangle area:\n')
                # if ',' in rect:
                #     rect = [int(x) for x in rect.split(', ')]
                # else:
                #     rect = [int(x) for x in rect.split(' ')]

                # check the length of the passed in array / tuple
                if len(rect) != 4:
                    return test()
                print(f'* Enter grayscale value for region{i + 1}:')
                print('* Hint: e.g. gray4')
                grayscale = input()
                while "gray" not in grayscale:
                    print("* Incorrect grayscale entered. Try again: ")
                    grayscale = input()
                print(f'* Data for region {i + 1}: {rect[i]}, {grayscale}')
                data.add_params(f"region{i + 1}", rect[i], grayscale)
            # handle other exceptions that might occur
            except:
                return test()
    # display the data input by user
    print(" * These are the regions: ")
    for k, v in data._regions.items():
        print(k, v)

    while True:
        query = input('* Are the defined regions correct? Answer \"y\" or \"n\":\n')
        if query == "Y" or "y":
            break
        elif query == "N" or "n":
            test()
        else:
            print('* The program will now exit')
            time.sleep(3)
            exit()

    try:
        data_input = DataInput(target=target, destination=destination, formats=formats, **data._regions)
        print('*** Starting processing now ***')

        # basic counter
        begin = time.time()
        data_input.generate_inputs()
        # starting processing
        processor = data_input.process()
        end = time.time()
        delta = end - begin
        minutes = delta // 60
        seconds = (delta / 60 - minutes) * 60
        print(f'Processed {processor} image(s)\n')
        print(f'* Took {minutes:.0f} minute(s) and {seconds:.0f} seconds')
    # need except else in between
    finally:
        print('*** Operation success ***')
        print('* Have a nice day')
        print('* Program will exit automatically')
        time.sleep(5)
    return 0


if __name__ == "__main__":
    test()