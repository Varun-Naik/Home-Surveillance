import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('compressed_video.mp4', fourcc, 20.0, (width, height))

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     compressed_frame = np.compress(True, np.array(frame))
#     out.write(compressed_frame)

# You can modify the loop to capture frames for 10 seconds
start_time = time.time()

while (time.time() - start_time) < 4:
    ret, frame = cap.read()
    if not ret:
        break
    # compressed_frame = np.compress(True, np.array(frame))
# compressed_frame = np.compress(True, np.array(frame))
# frame is a 2-D NumPy array representing an image, you can flatten it into 1D array before compressing as follows:
    flattened_frame = np.ravel(frame)
    print(f"Frame shape: {frame.shape}")
    print(f"Flattened frame shape: {flattened_frame.shape}")

# Apply np.compress() to the flattened array
    condition = np.ones(len(flattened_frame), dtype=bool)
    compressed_frame = np.compress(condition, flattened_frame)
    print(f"Compressed frame shape: {compressed_frame.shape}")
    out.write(compressed_frame)

cap.release()
out.release()
cv2.destroyAllWindows()
