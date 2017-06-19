import os

print(os.getcwd())

# print(os.listdir('Pictures'))
# print(os.listdir('Pictures/Beaker1'))

for beaker in os.listdir('Pictures'):
    path1 = 'Pictures/%s' % beaker
    for cam in os.listdir(path1):
        path2 = 'Pictures/%s/%s' % (beaker, cam)
        print(os.listdir(path2))

