from object_02 import container
from process import ImageProcessor
from generate_path import DataInput
from generate_path import data_path
from PIL import Image


def start_process():
    for img in ImageProcessor().prepare_crop(ImageProcessor().process(DataInput, data_path), container):
        img.show()


start_process()