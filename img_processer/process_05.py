from PIL import Image
# from generate_path import target, destination, generator
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

# cans add format to the proceess() func:
class ImageProcessor:
    def process(self):
        return self._traverse(self.__dict__)

    # maybe there is even more elegant solution?
    # unpacking via starred expression?
    def _traverse(self, instance_dict):
        try:
            data_path = instance_dict["target"]
            save_path = instance_dict["destination"]
            config = instance_dict["_config"]
            img_input = instance_dict["_file_list"]
        except KeyError:
            print("Key was not found")
        else:
            return self._process_images(data_path, save_path, img_input, config)

    def _process_images(self, data_path, save_path, img_input, config):
        count = 0
        # also can make here a recursive feucntion instead of yield
        # if not end of the list -> process further -> think about it
        for count, name in enumerate(img_input, 1):
            path = os.path.join(data_path, str(name))
            save = os.path.join(save_path, str(name))
            layer = Image.open(path, formats=["PNG"]).convert("RGB")

            print(layer.getbands())
            print(layer.size, layer.mode)

            for key, values in config.items():
                layer = self._crop_image(layer, values)

            # layer_converted = layer.convert("P")
            # print(layer_converted.getbands())
            layer.save(save, "PNG")
            print(f'Processed image #{count} - {name}')
            layer.close()

        return count



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
                if px[pixel_x, pixel_y] < (150, 150, 150):
                    # print(px[pixel_x, pixel_y])
                    px[pixel_x, pixel_y] = grayscale
        return crop_region



