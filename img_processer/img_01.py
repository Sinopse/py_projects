from PIL import Image
from PIL import ImageDraw
from generate_path_01 import res


def open_image(images_iter):
    for i in images_iter:
        print(i)
        try:
            img = Image.open(i)
            img.show()  # opens an image
            print(img.format, img.size, img.mode)
        except OSError:
            pass

# open_image(res)

# drawing a rectangle on the picture
# img = Image.open("img.jpg")
# img_copy = img
#
# # for visualization purposes displays the marked region of the image like below
# # .show() opens a copy of the image -> demonstration purpose
# # entering coordinates as such and using them as a parameter
# # drawing should be done on a copy of the image!
# coord_dict = list()
# coord_dict.append([0, 0, 200, 200])
# img_draw = ImageDraw.ImageDraw(img).rectangle(coord_dict[0], outline="red", width=2)
# img.show()
# # copying a subrectangle from the image
# box = (0, 0, 200, 200)  # image dimensions should not exceed the subrectangle!
# region = img_copy.crop(box)
# region = region.convert("L")
# # region = region.transpose(Image.ROTATE_180)
# img_copy.paste(region, box)
# img_copy.show()

regions_dict = dict()  # generic dict creation? class?
box_crop1 = (0, 0, 640, 669)  # what to do with odd values?
box_crop2 = (200, 200, 1280, 669) # named tuple?
regions_dict['region1'] = box_crop1
regions_dict['region2'] = box_crop2


layer = Image.open("layer1.jpg")


# compose functinality in a mixed in class below!
def crop_image(image, subrectangle):
    print(image.size)
    region = image.crop(subrectangle)
    # pass the region into processing
    region = process_ind_pxls(region)

    image.paste(region, subrectangle)
    image.show()
    return image

# processing individual bands
def process_ind_pxls(image): # this function deals ONLY with pixels! image is opened somewhere else before!
    # with Image.open("layer1.jpg") as image:
        px = image.load() # should be implemented above and passed in as an argument to the function
        print(image.size)
        column, row = image.size  # unpacked values
        for pixel_x in range(column):
            for pixel_y in range(row):

                if px[pixel_x, pixel_y] < (150, 150, 150): # threshold value must be customizable
                    # in order to avoid image artifacts
                    # print(px[pixel_x, pixel_y])
                    px[pixel_x, pixel_y] = (127, 127, 127)  #grayscale

        return image
    #img.show()
# now a specific portion of the image must be processed


# process_ind_pxls()
crop_image(layer, box_crop1)

