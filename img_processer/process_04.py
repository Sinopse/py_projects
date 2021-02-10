from PIL import Image
# from generate_path import target, destination, generator
import os


# cans add format to the proceess() func:
class ImageProcessor:
    def process(self, data_path, save_path, img_input, config):
        stored_images = []
        # also can make here a recursive feucntion instead of yield
        # if not end of the list -> process further -> think about it
        for count, name in enumerate(img_input, 1):
            path = os.path.join(data_path, str(name))
            save = os.path.join(save_path, str(name))
            layer = Image.open(path, formats=["PNG"]).convert("RGB")

            print(layer.getbands())
            print(layer.format, layer.size, layer.mode)

            for key, values in config.items():
                layer = self._crop_image(layer, values)

            # layer_converted = layer.convert("P")
            # print(layer_converted.getbands())
            layer.save(save, "PNG")
            print(f'Processed image #{count} - {name}')
            layer.close()
            stored_images.append(count)
        return stored_images



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



