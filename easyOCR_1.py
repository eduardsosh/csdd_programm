import easyocr
import cv2
#from matplotlib import pyplot as plt
import numpy as np

import warnings
warnings.filterwarnings("ignore", category=UserWarning) 


def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)


image_path = 'carimg5.jpg'
reader = easyocr.Reader(['en'], gpu=False)
result = reader.readtext(image_path, detail=0)
print(result)

elon_array = np.array(result)

print(elon_array)

for i in elon_array:
    if len(i) <8 and len(i) > 1 and "-" in i or ":" in i or " " in i:
        print(i)
    
    
    





        
        

    






