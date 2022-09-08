

import pytesseract
import PIL.Image
import cv2




myconfig = r"--psm 3 --oem 3"

text = pytesseract.image_to_string(PIL.Image.open("dsc_2049_60809-564c6f63611b8.jpg"), config=myconfig)
print(text)
#print("starting")