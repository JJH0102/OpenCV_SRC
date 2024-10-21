import cv2

def main():
    path = "/home/test/Desktop/OpenCV_SRC/OpenCV/cppTest/build/lena.bmp"
    img = cv2.imread(path + "/lena.bmp")
    cv2.imshow("image", img)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()