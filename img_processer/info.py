__author__ = "Alexander Tarasov"
__license__ = "For free use and distribution"
__version__ = "0.3"
__date__ = "31.05.2021"
__contact__ = "aleksander.tarasov91@gmail.com"
__description__ = "Image converter for 3D printers"


def print_info():
    print("Author: " + __author__)
    print(__description__)
    print("Software vesrion:" + __version__)
    print("Build date: " + __date__)
    print(__license__)
    print("Contact: " + __contact__)

    #instructions how to use the program
    print("\n")
    print("* Press 'q' or click X to quit")
    print("* After selecting at least one region press 'c' to continue")
    print("* Press 'r' to restart selection if any mistake made")

