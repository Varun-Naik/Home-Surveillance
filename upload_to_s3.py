import boto3
from secretss import accessKey, secretKey

# upload files to AWS S3 bucket
s3 = boto3.client('s3',
                  aws_access_key_id=accessKey,
                  aws_secret_access_key=secretKey)

bucket_name = 'mmc-video-bucket'
file_path = 'E:\Programming files\Home-Surveillance\output.mp4'
object_key = 'output.mp4'

s3.upload_file(file_path, bucket_name, object_key)
