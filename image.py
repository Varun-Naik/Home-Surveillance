import cv2


def main():
    capture = cv2.VideoCapture(0)
    _, image = capture.read()
    cv2.imwrite('image.jpg', image)


if __name__ == '__main__':
    main()