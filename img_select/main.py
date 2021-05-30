import cv2 as cv

drawing = False
coordinates = []

def draw_rect(event, x, y, flags, params):
    global ix, iy, drawing, img, img2

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        print(x, y)

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            a, b = x, y
            if a != x & b != y:
                img = img2.copy()
                cv.rectangle(img, (ix, iy), (x,y), (255, 0, 0), 2)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if ix != x and iy != y:
            cv.rectangle(img, (ix, iy), (x,y), (255, 0, 0), 2)
            img2 = img.copy()
            point = (ix, iy, x, y)
            #print(point)
            coordinates.append(point)  # save coordinates
            # if the points exist -> print them
            p1 = '(' + str(ix) + ', ' + str(iy) + ')'
            p2 = '(' + str(x) + ', ' + str(y) + ')'

            # display coordinates can be turned off/on
            # coords should fit the screen -> do later,
            cv.putText(img, p1, (ix + 20, iy + 20), cv.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 255), cv.LINE_AA)
            cv.putText(img, p2, (x + 20, y + 20), cv.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 255), cv.LINE_AA)

    return coordinates


img = cv.imread('img.png')  # take the first image from the batch
reset = img.copy()
width = img.shape[0]  # img width and height
height = img.shape[1]
img2 = img.copy()

cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.setMouseCallback('image', draw_rect)

while True:
    # res = cv.resize(img, (1280, 800))
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('q'):  # quit
        break
    elif k == ord('r'):
        img = reset.copy()
        img2 = img.copy()
        # for i in coordinates:
        #     print(i)
        coordinates.clear()

    if cv.getWindowProperty('image', cv.WND_PROP_VISIBLE) < 1:
        break

cv.destroyAllWindows()
