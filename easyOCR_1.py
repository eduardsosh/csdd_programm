import easyocr
import cv2
#from matplotlib import pyplot as plt
import numpy as np

import warnings #atbrivojas no warningiem

warnings.filterwarnings("ignore", category=UserWarning) 


def has_numbers(inputString): #parbauda vai string ir tikai skaitli.
    return any(char.isdigit() for char in inputString)


image_path = 'carimg5.jpg' #!!!!!!!!!sheit ir bildes path

reader = easyocr.Reader(['en'], gpu=False)
result = reader.readtext(image_path, detail=0)
print(result)

elon_array = np.array(result) #List to array lai var stradat ar array nevis list

print(elon_array) #lai parbauditu

for i in elon_array: # ejam cauri un meklejam to ko vajag
    if len(i) <8 and len(i) > 1 and "-" in i or ":" in i or " " in i:
        print(i) #izvadam atrasto pec filtriem
    
    
    





        
        

    






