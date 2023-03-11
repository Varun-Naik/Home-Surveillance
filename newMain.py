import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#writer = cv2.VideoWriter('basicvideo.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 30, (width, height)) #WORKS
#writer = cv2.VideoWriter('basicvideo.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (width, height))
#writer = cv2.VideoWriter('basicvideo.avi', cv2.VideoWriter_fourcc(*'XVID'), 20, (width, height)) #WORKS

writer = cv2.VideoWriter('basicvideo.mkv', cv2.VideoWriter_fourcc(*'H264'), 30, (width, height)) #works

while True:
    ret, frame = cap.read()

    writer.write(frame)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
writer.release()
cv2.destroyAllWindows()
