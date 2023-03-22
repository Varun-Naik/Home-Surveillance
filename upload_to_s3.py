import boto3
from secretss import accessKey, secretKey

# upload files to AWS S3 bucket
s3 = boto3.client('s3')

bucket_name = "mmc-video-bucket"
file_path = 'E:\Programming files\Home-Surveillance\\basicvideo.mp4'
object_key = 'basicvideo.mp4'

s3.upload_file(file_path, bucket_name, object_key)
