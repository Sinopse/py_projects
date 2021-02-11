import os
from PIL import Image
from process_05 import ImageProcessor

# DataInput stores target and destination folders
class DataInput(ImageProcessor):
    """
    A class that handles input data, can be instantiated without arguments.
    :returns a list of image file names

    :arg target: directory, where source images are located

    :arg destination: directory, where processed images should be stored

    :arg formats: formats, which the program considers for further processing
    e.g. "JPEG", "PNG", "BMP". More information can be found in the documentation
    of the module Image

    :arg config: configuration parameters for the respective regions of the images to
    be processed:
    see the ConfigData class for more information

    """
    def __init__(self, target=None, destination=None, formats=None, **config):
        self.target = target
        self.destination = destination
        self._formats = formats  # not optimal solution
        self._config = config
        self._file_list = []

    def generate_inputs(self):
        for file in os.listdir(self.target):
            # check if images and can be opened
            # if true append names to the list
            try:
                img = Image.open(file, formats=self._formats)
                img.close()
            except OSError:
                pass
            self._file_list.append(file)
        return self._file_list


