# Camera name = USB2.0 HD UVC WebCam
import subprocess

# Set the output file name
output_file = 'output.mp4'

# Set the video codec, bitrate, and frame rate
# codec = 'libxvid'
codec = 'libx264'
bitrate = '1M'
framerate = 30

# Set the duration of the captured video
duration = 4  # 10 seconds

# Set the encoding preset
# can be 'ultrafast', 'superfast', 'veryfast', 'faster', 'fast', 'medium', 'slow', 'slower', 'veryslow'
#preset = 'veryslow'

# Set the CRF value (ranges from 0 to 51, with lower values indicating higher quality and larger file sizes)
crf = 23

# Call ffmpeg to capture webcam video and save it to the output file with the specified codec, bitrate, frame rate,
# and duration
ffmpeg_path = 'C:/ffmpeg/bin/ffmpeg.exe'

# for Xvid codec
#subprocess.call([ffmpeg_path, '-f', 'dshow', '-i', 'video=USB2.0 HD UVC WebCam', '-c:v', codec, '-b:v', bitrate, '-r',
#                 str(framerate), '-t', str(duration), output_file])
# with preset
#subprocess.call([ffmpeg_path, '-f', 'dshow', '-i', 'video=USB2.0 HD UVC WebCam', '-c:v', codec, '-b:v', bitrate,
#                '-r', str(framerate), '-preset', preset, '-t', str(duration), output_file])
# with crf value
subprocess.call([ffmpeg_path, '-f', 'dshow', '-i', 'video=USB2.0 HD UVC WebCam', '-c:v', codec, '-b:v', bitrate,
                 '-r', str(framerate), '-crf', str(crf), '-t', str(duration), output_file])