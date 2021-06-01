import cv2 as cv
import os
from pathlib import Path
from PIL import Image
import info

info.print_info()
# selecting first image from the folder

target = Path(input('* Please, specify target folder:\n'))
while not target.exists():
    print('* The specified directory doesn\'t exist, try again:')
    target = Path(input("Please, specify target folder:\n"))

lst = []
def first_image(path):
    first_img = ''

    #dir_path = os.path.dirname(os.path.realpath(__file__))
    for count, file in enumerate(os.listdir(path), 1):
        first_img = os.path.join(path, str(file))
        try:
            # looking for the first image in folder
            image = Image.open(first_img)
            image.close()
            lst.append(first_img)
            break
        except OSError:
            pass
    return lst, first_img


points = []
temp = []  # intermediate storage for points
cnt = 0
regions = 0


def mouse(event, x, y, flags, param):
    global cnt

    if event == cv.EVENT_LBUTTONDOWN:
        temp.append(x)
        temp.append(y)
        draw(temp)
        cnt += 1


def draw(pts):
    global regions, img, reset
    if len(pts) == 4:
        x1, y1, x, y = pts
        cv.circle(img, (x, y), 10, (0, 0, 255), -1)
        cv.rectangle(img, (x1, y1), (x, y), (255, 0, 0), 2)
        # test rect box
        regions += 1
        cv.putText(img, str(regions), (x1 - 100, y1 + 50), cv.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 255), cv.LINE_AA)
        points.append(tuple(pts))
        pts.clear()

    else:
        x, y = pts
        cv.circle(img, (x, y), 10, (0, 0, 255), -1)


# window name and path to the first image in the folder
image_to_read, window_name = first_image(target)
img = cv.imread(image_to_read[0])

cv.namedWindow(window_name, cv.WINDOW_NORMAL)
cv.setMouseCallback(window_name, mouse)
reset = img.copy()

trigger = False

def image_selector(image):

    global cnt, reset, img, regions, trigger
    while True:
        cv.imshow(window_name, image)
        k = cv.waitKey(1) & 0xFF
        if k == ord('q'):
            trigger = True
            break

        elif k == ord('r'):
            img = reset.copy()
            points.clear()
            cnt = 0
            regions = 0
            image_selector(img)

        elif k == ord('c') and len(points) > 0:
            break

        if cv.getWindowProperty(window_name, cv.WND_PROP_VISIBLE) < 1:
            trigger = True
            break

    cv.destroyAllWindows()
    return points


image_selector(img)

