# Home Surveillance Video Capture, Compression and Transmission Project
This project involves capturing, compressing, and transmitting surveillance video from a laptop webcam to an AWS S3 bucket. 
The code is written in Python using OpenCV and the boto3 library. 

## Requirements
* Python 3.7 or higher
* OpenCV 4.0 or higher
* AWS account with an S3 bucket set up
* boto3 library (for uploading to AWS S3)


## Installation

1. Clone the repository from GitHub:
```
git clone https://github.com/Varun-Naik/Home-Surveillance.git
```

1. Install the required packages:
```
pip install opencv-python
pip install boto3
```

3. Set up your AWS credentials:

- Create an AWS account if you don't have one already.
- Set up an S3 bucket.
- Create an access key and a secret access key with the necessary permissions to access the bucket.
- Configure your AWS credentials by running aws configure in your terminal and entering your access key and secret access key.


## Usage
1. Run the multipleVideo.py script to capture video from your camera:
````
python multipleVideo.py
````
2. Press Esc to stop the video capture.
3. The captured video is saved in the specified format (.avi or .mp4) with the specified resolution and frame rate.
4. The captured video is automatically uploaded to your AWS S3 bucket using the upload_to_s3.py script
however multipleVideo.py simultaneously uploads the video to AWS S3 after saving the video.
5. The uploaded video can be accessed from your AWS S3 bucket.

## Credits
This project was created by Varun Naik. Feel free to use and modify the code for your own projects.
This project was done a part of the Multimedia Communications ELG 5121/CSI7163 course at uOttawa.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## References
1. https://web.archive.org/web/20210506132355/http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html#saving-a-video
2. https://www.learningaboutelectronics.com/Articles/How-to-record-video-Python-OpenCV.php

