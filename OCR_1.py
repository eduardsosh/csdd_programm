
#pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

import pytesseract
import PIL.Image
import cv2




#myconfig = r"--psm 3 --oem 3"

text = pytesseract.image_to_string(PIL.Image.open("textimg.png"))
print(text)


#print("starting")