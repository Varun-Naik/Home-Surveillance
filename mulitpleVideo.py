import numpy as np
import os
import cv2
import boto3

# filename = 'avi_sample_video.avi'
filename = 'mp4_sample_video.mp4'
frames_per_second = 24.0
# res = '480p'
res = '720p'


# Set resolution for the video capture
# Function adapted from https://kirr.co/0l6qmh
def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)


# Standard Video Dimensions Sizes
STD_DIMENSIONS = {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160),
}


# grab resolution dimensions and set video capture to it.
def get_dims(cap, res='1080p'):
    width, height = STD_DIMENSIONS["480p"]
    if res in STD_DIMENSIONS:
        width, height = STD_DIMENSIONS[res]
    ## change the current caputre device
    ## to the resulting resolution
    change_res(cap, width, height)
    return width, height


# Video Encoding, might require additional installs
# Types of Codes: http://www.fourcc.org/codecs.php
VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    # 'mp4': cv2.VideoWriter_fourcc(*'H264'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}


# Default extension returned is avi. This fun. is used to select the codec acc. to the extension
def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
        return VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']


cap = cv2.VideoCapture(0)
out = cv2.VideoWriter(filename, get_video_type(filename), 25, get_dims(cap, res))

while True:
    ret, frame = cap.read()
    out.write(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

# upload files to AWS S3 bucket
s3 = boto3.client('s3',
                  aws_access_key_id='AKIA54ZHVIHWKDTM3N7M',
                  aws_secret_access_key='M8y42VvpzjKf3LJ2FSTiNuIUKFWFHJlfl6OBiZOr')

bucket_name = 'mmc-video-bucket'
file_path = 'E:\Programming files\Home-Surveillance\mp4_sample_video.mp4'
object_key = 'mp4_sample_video.mp4'

s3.upload_file(file_path, bucket_name, object_key)
