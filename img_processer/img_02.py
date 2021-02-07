from PIL import Image
from PIL import ImageDraw
import os
from generate_path_01 import res

# refine handler so it only processes images
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

data_path = r"D:\08_02_21_Puma_Gyroid_V7\Thumbnails"

regions_dict = dict()  # generic dict creation? class?
box_crop1 = [(0, 0, 800, 330), (127, 127, 127)]  # what to do with odd values?
box_crop2 = [(800, 0, 1280, 330), (55, 55, 55)]  # named tuple?
box_crop3 = [(0, 330, 640, 660), (159, 159, 159)]  # named tuple?
box_crop4 = [(640, 330, 1280, 660), (199, 199, 199)]  # named tuple?
regions_dict['region1'] = box_crop1
regions_dict['region2'] = box_crop2
regions_dict['region3'] = box_crop3
regions_dict['region4'] = box_crop4

def traverse_dict(dictionary):
    path = os.path.join(data_path, "Bitmap000001.png")
    layer = Image.open(path)
    for key, values in dictionary.items():
        print(values)
        layer = crop_image(layer, values) # crop here
    return layer

# compose functinality in a mixed in class below!
def crop_image(image, values):
    subrectangle = values[0]
    gscale = values[1]
    print(subrectangle, gscale)
    print(image.size)

    region = image.crop(subrectangle)
    # pass the region into processing
    region = process_ind_pxls(region, gscale)

    image.paste(region, subrectangle)
    # image.show()
    return image

# processing individual bands
def process_ind_pxls(image, gscale): # this function deals ONLY with pixels! image is opened somewhere else before!
    # with Image.open("layer1.jpg") as image:
        px = image.load() # should be implemented above and passed in as an argument to the function
        print(image.size)
        column, row = image.size  # unpacked values
        for pixel_x in range(column):
            for pixel_y in range(row):

                if px[pixel_x, pixel_y] < (150, 150, 150): # threshold value must be customizable
                    # in order to avoid image artifacts
                    # print(px[pixel_x, pixel_y])
                    px[pixel_x, pixel_y] = gscale  #grayscale

        return image
    #img.show()
# now a specific portion of the image must be processed

save_path = r"C:\Users\aleks\Desktop\Python\img_processer\processed_images"
save = os.path.join(save_path, "Bitmap000001.png")
print(save)
#process_ind_pxls()
# crop_image(layer, box_crop)
image = traverse_dict(regions_dict)
image.show()
image.save(save)
