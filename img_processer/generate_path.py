import os
from PIL import Image
from process_05 import ImageProcessor

formats = "JPEG", "PNG"

# DataInput stores target and destination folders
class DataInput(ImageProcessor):
    def __init__(self, target=None, destination=None, *formats, **config):
        self.target = target
        self.destination = destination
        self._formats = formats  # not optimal solution
        self._config = config
        self._file_list = []

    def generate_inputs(self):
        for file in os.listdir(self.target):
            # check if images and can be opened
            # if true append to the list
            try:
                img = Image.open(file, formats=self._formats)
                img.close()
            except OSError:
                pass
            self._file_list.append(file)
        return self._file_list


#data_path = os.path.dirname(os.path.realpath(__file__))

#formats = "JPEG", "PNG"

