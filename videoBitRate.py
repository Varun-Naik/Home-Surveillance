import subprocess

# Set the input and output file names
input_file = 'mp4_sample_video.mp4'
output_file = 'output.avi'

# Set the video codec and bitrate
codec = 'libxvid'
bitrate = '1M'

# Call ffmpeg to convert the input video to the output video with the specified codec and bitrate
ffmpeg_path = 'C:/ffmpeg/bin/ffmpeg.exe'
subprocess.call([ffmpeg_path, '-i', input_file, '-c:v', codec, '-b:v', bitrate, output_file])
