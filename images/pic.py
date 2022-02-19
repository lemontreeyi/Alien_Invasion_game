import cv2


def show_img(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img = cv2.imread("images/alien.png")
pic = cv2.resize(img, (50, 60))
cv2.imwrite("images/alien2.png",pic)
