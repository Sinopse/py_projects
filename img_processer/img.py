from PIL import Image
from generate_path_01 import res


def open_image(images_iter):
    for i in images_iter:
        #print(i)
        try:
            Image.open(i)
        except OSError:
            pass

open_image(res)

