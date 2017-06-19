import boto3
from botocore.client import Config
import socket

ACCESS_KEY_ID = ''
ACCESS_SECRET_KEY = ''
BUCKET_NAME = 'ice911'
s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)

def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

data = open('download.jpg', 'rb')
s3.Bucket(BUCKET_NAME).put_object(Key='Data/RateOfDissolving/download.jpg', Body=data) #replace data with img?
print ("Image Uploaded")

#
# if is_connected():
#     data = open(path+pic_name, 'rb')
#     key = 'RateOfDissolving/%s%s' %(path, picname)
#     s3.Bucket(BUCKET_NAME).put_object(Key=key, Body=data) #replace data with img?
#     print ("Image Uploaded")
# else:
#     cv2.imwrite(path + pic_name, img)
#     print("Image Saved")
