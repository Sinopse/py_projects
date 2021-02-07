import os
from PIL import Image

# DataInput stores target and destination folders
class DataInput:
    def __init__(self, path):
        self.path = path

    def generate_inputs(self):
        name_list = []
        for name in os.listdir(self.path):
            try:
                img = Image.open(name, formats=["JPEG", "PNG"])
                img.close()

            except OSError:
                pass

            name_list.append(name)
        return name_list

    # # a string representaion of a path
    # def __repr__(self):
    #     return f'"{self.name}"'


#data_path = os.path.dirname(os.path.realpath(__file__))
data_path = r"C:\Users\aleks\Desktop\Python\img_processer\test_images"
#data_path = r"D:\08_02_21_Puma_Gyroid_V7"
generate_images = DataInput(data_path).generate_inputs()

#for _ in generate_images:
#    print(_)

