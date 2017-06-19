import boto3, socket, cv2, os
from botocore.client import Config


ACCESS_KEY_ID = 'AKIAIPOFPDWJWMYM6TFQ'
ACCESS_SECRET_KEY = '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'
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

cam = cv2.VideoCapture(10)
if cam.isOpened() and cam.read():
    s, img = cam.read()
    path = 'C:/Users/Laurel/PyCharmProjects/RateOfDissolvingExperiment/test_save.jpg'
    cv2.imwrite(path, img)
    print('Image saved')
    if is_connected():
        data = open(path, 'rb')
        s3.Bucket(BUCKET_NAME).put_object(Key='Data/Material Decay Experiment, 6-19-17/%s' % path , Body=data)
        data.close()
        print ("Image Uploaded")
        os.remove(path)
        print("Image Deleted")





# if is_connected():
#     data = open(path+pic_name, 'rb')
#     key = 'RateOfDissolving/%s%s' %(path, picname)
#     s3.Bucket(BUCKET_NAME).put_object(Key=key, Body=data) #replace data with img?
#     print ("Image Uploaded")
# else:
#     cv2.imwrite(path + pic_name, img)
#     print("Image Saved")
