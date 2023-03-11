# Home Surveillance Video Capture, Compression and Transmission Project
This project involves capturing, compressing, and transmitting surveillance video from a laptop webcam to an AWS S3 bucket. 
The code is written in Python using OpenCV, FFmpeg and the boto3 library. 

## Requirements
* Python 3.7 or higher
* OpenCV 4.0 or higher
* FFmpeg libraries
* AWS account with an S3 bucket set up
* boto3 library (for uploading to AWS S3)


## Installation

1. Clone the repository from GitHub:
```
git clone https://github.com/Varun-Naik/Home-Surveillance.git
```
2. Install the required packages:
```
pip install opencv-python
pip install boto3
```

3. Install FFmpeg libraries by following the steps mentioned in this [tutorial](https://phoenixnap.com/kb/ffmpeg-windows).
4. Set up your AWS credentials:

- Create an AWS account if you don't have one already.
- Set up an S3 bucket.
- Create an access key and a secret access key with the necessary permissions to access the bucket.
- Configure your AWS credentials by running aws configure in your terminal and entering your access key and secret access key.


## Usage
### Capture video using OpenCV
1. Run the `video_using_opencv.py` script to capture video from your camera using OpenCV:
````
python video_using_opencv.py
````
2. Press Esc to stop the video capture.
3. The captured video is saved in the specified format (.avi or .mp4) with the specified resolution and frame rate.
4. The captured video is automatically uploaded to your AWS S3 bucket using the `upload_to_s3.py` script
5. The uploaded video can be accessed from your AWS S3 bucket.

### Capture video using FFmpeg
1. Run the `videoWebcamFfmpeg.py` script to capture video from your camera using FFmpeg:
````
python videoWebcamFfmpeg.py
````
2. The captured video is saved in the specified format with the specified video codec, bitrate, 
frame rate, duration and CRF value.
3. The captured video is automatically uploaded to your AWS S3 bucket using the `upload_to_s3.py` script. 
4. The uploaded video can be accessed from your AWS S3 bucket.

## Credits
This project was created by Varun Naik. Feel free to use and modify the code for your own projects.
This project was done a part of the Multimedia Communications ELG 5121/CSI7163 course at uOttawa.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## References
1. [OpenCV video capture tutorial](https://web.archive.org/web/20210506132355/http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html#saving-a-video)
2. [How to record video with Python and OpenCV](https://www.learningaboutelectronics.com/Articles/How-to-record-video-Python-OpenCV.php)
3. [FFmpeg installation tutorial for Windows](https://phoenixnap.com/kb/ffmpeg-windows)

