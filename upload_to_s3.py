import boto3

s3 = boto3.client('s3',
    aws_access_key_id='AKIA54ZHVIHWKDTM3N7M',
    aws_secret_access_key='M8y42VvpzjKf3LJ2FSTiNuIUKFWFHJlfl6OBiZOr')

bucket_name = 'mmc-video-bucket'
file_path = 'E:\Programming files\Home-Surveillance\mp4_sample_video.mp4'
object_key = 'mp4_sample_video.mp4'

s3.upload_file(file_path, bucket_name, object_key)
