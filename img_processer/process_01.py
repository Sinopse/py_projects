from PIL import Image
import os

regions_dict = dict()  # generic dict creation? class?
box_crop1 = [(0, 0, 2700, 1140), (55, 55, 55)]  # what to do with odd values?
box_crop2 = [(2700, 0, 4390, 1140), (127, 127, 127)]  # named tuple?
box_crop3 = [(0, 1140, 2700, 2290), (15, 15, 15)]  # named tuple?
box_crop4 = [(2000, 1140, 4390, 2290), (95, 95, 95)]  # named tuple?
regions_dict['region1'] = box_crop1
regions_dict['region2'] = box_crop2
regions_dict['region3'] = box_crop3
regions_dict['region4'] = box_crop4

class ImageProcessor:
    def load_image(self, target, destination, input_class, config):
        count = 0
        for count, name in enumerate(input_class):
#            print(name)
            # specify target and destination
            path = os.path.join(target, str(name))
           # print(path)
            save_path = os.path.join(destination, str(name))
            self._process_image(path, save_path, config)
        return f'Processed {count} images'

    def _process_image(self, target, destination, config):
        layer = Image.open(target, formats=["PNG"]).convert("RGB")
        #layer = Image.open(target)
        # print image info
        print(layer.getbands())
        print(layer.format, layer.size, layer.mode)

        # loop to process a given layer/image
        for key, values in config.items():
            self._crop_image(layer, values)

        # layer_converted = layer.convert("P")
        # print(layer_converted.getbands())
        layer.save(destination, "PNG")
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
                #print(px[pixel_x, pixel_y])
                 if px[pixel_x, pixel_y] < (150, 150, 150):
                    px[pixel_x, pixel_y] = grayscale
        return crop_region

