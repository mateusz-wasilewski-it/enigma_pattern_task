#!/usr/bin/python
from Database import Database
from Flicker import FlickerConnection
from helper import url_to_image
import sys
import cv2
import numpy as np

flicker = FlickerConnection("45923a7bfe1c74e203ec20b7a8ecb150", "6b5b680a83194751")
db = Database()
db.createTable()

if len(sys.argv) == 3:
    keyword = sys.argv[1]
    num_of_images = sys.argv[2]
    urls = flicker.get_photos_as_url(str(keyword), int(num_of_images))
else:
    keyword = None
    num_of_images = None
    urls = flicker.get_photos_as_url()

for url in urls:
    db.add_image(url)

urls = db.select_all()
red_pixels = 0
most_red_url = ""
for url in urls:
    temp = url_to_image(url)
    red_mask = cv2.inRange(temp,(0, 0, 130) , (60, 60, 255))
    temp_red_pixels = cv2.countNonZero(red_mask) / np.size(temp) * 100 #percant

    if temp_red_pixels > red_pixels:
        red_pixels = temp_red_pixels
        most_red_url = url

cv2.imshow("the most red", url_to_image(most_red_url))
cv2.waitKey()


db.close()