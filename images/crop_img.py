"""
Crop the image in input and overwrite the result.

Positional arguments:
    - image file
    - top left x
    - top left y
    - width
    - height

For feet: 850 610 240 150
For arms: 850 300 240 150
For blur/no blur: 525 80 200 200
"""
from PIL import Image
import sys

img = Image.open(sys.argv[1])

if len(sys.argv) < 6:
    top_left = (850, 300)
    bottom_right = (top_left[0] + 240, top_left[1] + 150)
else:
    top_left = (int(sys.argv[2]), int(sys.argv[3]))
    bottom_right = (top_left[0] + int(sys.argv[4]), top_left[1] + int(sys.argv[5]))

area = top_left + bottom_right
cropped_img = img.crop(area)
#cropped_img.show()
cropped_img.save(sys.argv[1])
