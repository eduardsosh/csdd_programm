
#pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

import pytesseract
import PIL.Image
import cv2




myconfig1 = r"--psm 4 --oem 3" #psm 4 jo tas megina atrast dazada izmera tekstu oem 3 jo default
myconfig2 = r"--psm 11 --oem 3"
myconfig3 = r"--psm 13 --oem 3"

text1 = pytesseract.image_to_string(PIL.Image.open("plate3.jpg"), config=myconfig1)
text2 = pytesseract.image_to_string(PIL.Image.open("plate3.jpg"), config=myconfig2)
text3 = pytesseract.image_to_string(PIL.Image.open("plate3.jpg"), config=myconfig3)
print("Config1 rez: ")
print(text1)
print("Config2 rez: ")
print(text2)
print("Config3 rez: ")
print(text3)


