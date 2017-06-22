import cv2
import datetime
from time import sleep
import boto3
from botocore.client import Config
import socket
import os


BUCKET_NAME = 'ice911'
s3 = boto3.resource(
    's3',
    config=Config(signature_version='s3v4')
)


def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False


cam_index = 1
num_cams = 10
pics_taken = 0
desired_pictures = 1
interval_in_seconds = 10

while pics_taken < desired_pictures:
    while cam_index <= num_cams:
        cam = cv2.VideoCapture(cam_index)
        if cam.isOpened() and cam.read():
            s, img = cam.read()  # captures image
            now = datetime.datetime.now()
            if cam_index == 1:
                path = 'Pictures/Beaker3/TopCam/'
            elif cam_index == 2:
                img = cv2.flip(img, 0)
                path = 'Pictures/Beaker3/SideCam/'
            elif cam_index == 3:
                path = 'Pictures/Beaker1/TopCam/'
            elif cam_index == 4:
                img = cv2.flip(img, 0)
                path = 'Pictures/Beaker1/SideCam/'
            elif cam_index == 5:
                path = 'Pictures/Beaker2/TopCam/'
            elif cam_index == 6:
                img = cv2.flip(img, 0)
                path = 'Pictures/Beaker2/SideCam/'
            elif cam_index == 7:
                path = 'Pictures/Beaker4/TopCam/'
            elif cam_index == 8:
                img = cv2.flip(img, 0)
                path = 'Pictures/Beaker4/SideCam/'
            elif cam_index == 9:
                path = 'Pictures/Beaker5/TopCam/'
            elif cam_index == 10:
                img = cv2.flip(img, 0)
                path = 'Pictures/Beaker5/SideCam/'
            pic_name = "%d.%d.%d.%d.%d.%d.jpg" % (now.year, now.month, now.day, now.hour, now.minute, now.second)
            path = path + pic_name
            cv2.imwrite(path, img)  # writes image to folder
            if is_connected():
                data = open(path, 'rb')
                s3.Bucket(BUCKET_NAME).put_object(Key='Data/Material Decay Experiment, 6-19-17/%s' % path, Body=data)
                data.close()
                print("Image Uploaded")
                os.remove(path)
                print("Image Deleted")
        cam.release()
        cam_index += 1
        print(pics_taken)
        if pics_taken % 2 == 0: #choose how often to check for non-uploaded pics
            if is_connected():
                beakers = os.listdir('Pictures')
                for b in beakers:
                    cams = os.listdir('Pictures/%s' % b)
                    for c in cams:
                        path = 'Pictures/%s/%s' % (b, c)
                        if os.listdir(path):
                            files = os.listdir(path)
                            for f in files:
                                path = 'Pictures/%s/%s/%s' % (b, c, f)
                                print('path:', path)
                                data = open(path, 'rb')
                                s3.Bucket(BUCKET_NAME).put_object(Key='Data/Material Decay Experiment, 6-19-17/%s' % path,
                                                                  Body=data)
                                data.close()
                                print("Image Recovered")
                                os.remove(path)
                                print('Image Removed')
        pics_taken += 1
        cam_index = 1
        sleep(interval_in_seconds)

