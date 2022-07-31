from typing import List

text='lidar sensing in autonomous system'


d = dict()

for line in text:

    line = line.lower()
    words = line.split('lidar sensing in autonomous system')
for words in words:
         if words in d:
             d[words] = d[words] + 1
         else:
             d[words] = 1
for key in list(d.keys()):
       print(key,  'lidar sensing in autonomous system', d[key])