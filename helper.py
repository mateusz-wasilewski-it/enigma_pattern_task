import numpy as np
import urllib
from urllib.request import urlopen
import cv2

def url_to_image(url):
	resp = urllib.request.urlopen(url)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	cv2_image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	return cv2_image