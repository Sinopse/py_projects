from PIL import Image
import os

# format conversion if needed?
img = Image.open("layer1.jpg")
img_filename, extension = os.path.splitext("layer1.jpg")
out = img_filename + '.png'
print(out)
img.save(out)