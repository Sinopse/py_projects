from PIL import Image
from generate_path import generate_images
from object_02 import container
import os

#save_path = r"C:\Users\aleks\Desktop\Python Tutorials\Images_Anna"
data_path = r"C:\Users\aleks\Desktop\Python\img_processer\test_images"
save_path = r"C:\Users\aleks\Desktop\Python\img_processer\processed_images"
#data_path = r"D:\08_02_21_Puma_Gyroid_V7"

regions_dict = dict()  # generic dict creation? class?
box_crop1 = [(0, 0, 2700, 1140), (55, 55, 55)]  # what to do with odd values?
box_crop2 = [(2700, 0, 4390, 1140), (127, 127, 127)]  # named tuple?
box_crop3 = [(0, 1140, 2700, 2290), (15, 15, 15)]  # named tuple?
box_crop4 = [(2000, 1140, 4390, 2290), (95, 95, 95)]  # named tuple?
regions_dict['region1'] = box_crop1
regions_dict['region2'] = box_crop2
regions_dict['region3'] = box_crop3
regions_dict['region4'] = box_crop4

# for a number of configs
# generate an image
# process that image
#Mix-in class for DataInput
class ImageProcessor:
    def process(self, img_input, config):
        for name in img_input:
            path = os.path.join(data_path, str(name))
            save = os.path.join(save_path, str(name))
            print(path)
            #layer = Image.open(path, formats=["PNG"]).convert("RGB")
            layer = Image.open(path, formats=["PNG"])

            print(layer.getbands())
            print(layer.format, layer.size, layer.mode)

            for key, values in config.items():
                layer = self._crop_image(layer, values)

            # layer_converted = layer.convert("P")
            # print(layer_converted.getbands())
            layer.save(save, "PNG")
            yield layer

    def _crop_image(self, image, values):
        rectangle, grayscale = values[0], values[1]
        region = image.crop(rectangle)
        region = self._process_pixels(region, grayscale)
        image.paste(region, rectangle)
        return image


    def _process_pixels(self, crop_region, grayscale):
        px = crop_region.load()
        print(crop_region.size)
        column, row = crop_region.size  # unpacked values
        for pixel_x in range(column):
            for pixel_y in range(row):
                # customize treshold value
                #print(px[pixel_x, pixel_y])
                 if px[pixel_x, pixel_y]  == 1:
                    # print(px[pixel_x, pixel_y])
                    px[pixel_x, pixel_y] = 4
        return crop_region


processor = ImageProcessor().process(generate_images, regions_dict)

for img in processor:
    print("processed")
