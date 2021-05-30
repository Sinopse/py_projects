import cv2 as cv

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
        regions += 1
        cv.putText(img, str(regions), (x1 - 100, y1 + 50), cv.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 255), cv.LINE_AA)
        points.append(tuple(pts))
        print(points)
        pts.clear()

    else:
        x, y = pts
        cv.circle(img, (x, y), 10, (0, 0, 255), -1)


img = cv.imread('img.png')
cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.setMouseCallback('image', mouse)
reset = img.copy()


def run(image):
    global cnt, reset, img, regions
    while True:
        cv.imshow('image', image)
        k = cv.waitKey(1) & 0xFF
        if k == ord('q'):
            break

        elif k == ord('r'):
            img = reset.copy()
            points.clear()
            cnt = 0
            regions = 0
            run(img)

        if cv.getWindowProperty('image', cv.WND_PROP_VISIBLE) < 1:
            break

    cv.destroyAllWindows()
    return points


run(img)
