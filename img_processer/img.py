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
img = Image.open("img.jpg")
img_copy = img

# for visualization purposes displays the marked region of the image like below
# .show() opens a copy of the image -> demonstration purpose
# entering coordinates as such and using them as a parameter
# drawing should be done on a copy of the image!
coord_dict = list()
coord_dict.append([0, 0, 200, 200])
img_draw = ImageDraw.ImageDraw(img).rectangle(coord_dict[0], outline="red", width=2)
img.show()
# copying a subrectangle from the image
box = (0, 0, 200, 200)  # image dimensions should not exceed the subrectangle!
region = img_copy.crop(box)
region = region.convert("L")
# region = region.transpose(Image.ROTATE_180)
img_copy.paste(region, box)
img_copy.show()

box_crop = (0, 0, 640, 335) # what to do with odd values?
layer = Image.open("layer1.jpg")
def crop_image(image, subrectangle):
    region = image.crop(subrectangle)
    region = process_ind_pxls()
    image.paste(region, subrectangle)
    return image

# processing individual bands
def process_ind_pxls(): # this function deals ONLY with pixels! image is opened somewhere else before!
    with Image.open("layer1.jpg") as img:
        px = img.load() # should be implemented above and passed in as an argument to the function
        print(img.size)
        column, row = img.size  # unpacked values
        for pixel_x in range(column):
            for pixel_y in range(row):

                if px[pixel_x, pixel_y] < (200, 200, 200): # threshold value must be customizable
                    # in order to avoid image artifacts
                    # print(px[pixel_x, pixel_y])
                    px[pixel_x, pixel_y] = (127, 127, 127)

    img.show()
# now a specific portion of the image must be processed


process_ind_pxls()

