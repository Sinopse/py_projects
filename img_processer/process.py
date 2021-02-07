from PIL import Image
from generate_path import generate_images
from object_02 import data
import os

save_path = r"C:\Users\aleks\Desktop\Python\img_processer\processed_images"
data_path = r"C:\Users\aleks\Desktop\Python\img_processer\test_images"

class ImageProcessor:
    def process(self, data_input, config):
        return self._prepare_crop(data_input, config)

    # data input is a function which provides image file names
    # config is a dictionary with parameters
    def _prepare_crop(self, data_input, config):
        # img_list = []
        for image in data_input:
            open_path = os.path.join(data_path, "layer1.jpg")
            print(open_path)
            image_file = Image.open(open_path, formats=["JPEG", "PNG"])

            print("*** Applying region on the image***", )
            for key, value in config.items():
                print(key, value)
                subrectangle, grayscale = value[0], value[1]

                region = image_file.crop(subrectangle)
                region = self._process_pixels(region, grayscale)

                image_file.paste(region, subrectangle)
                save_dir = os.path.join(save_path, str(image))
                image_file.save(save_dir)


        #         img_list.append(image_file)
        # return img_list

    def _process_pixels(self, crop_region, grayscale):
        px = crop_region.load()
        print(crop_region.size)
        column, row = crop_region.size  # unpacked values
        for pixel_x in range(column):
            for pixel_y in range(row):
                # customize treshold value
                if px[pixel_x, pixel_y] < (150, 150, 150):
                    # print(px[pixel_x, pixel_y])
                    px[pixel_x, pixel_y] = grayscale
        return crop_region


processor = ImageProcessor().process(generate_images, data._regions)