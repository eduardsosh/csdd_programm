from cgitb import text
from types import NoneType
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
import requests
from bs4 import BeautifulSoup

import warnings #atbrivojas no warningiem
warnings.filterwarnings("ignore", category=UserWarning) 


img = cv2.imread('carimg4.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
count = 0
result = 0

    
count= count+1
bfilter = cv2.bilateralFilter(gray, 11,17,17)
plt.imshow(cv2.cvtColor(bfilter,cv2.COLOR_BGR2RGB))
plt.show()
edged = cv2.Canny(bfilter,100*count,100*count)
plt.imshow(cv2.cvtColor(edged,cv2.COLOR_BGR2RGB))
plt.show()

keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(keypoints)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    

    
print(count)
location = None
for contour in contours:
    approx = cv2.approxPolyDP(contour, 10, True)
    if len(approx) == 4:
        location = approx
        break

print(location)
    

    
mask = np.zeros(gray.shape, np.uint8)
new_image = cv2.drawContours(mask, [location], 0,255, -1)
new_image = cv2.bitwise_and(img, img, mask=mask)

plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
plt.show()
(x,y) = np.where(mask==255)
(x1, y1) = (np.min(x), np.min(y))
(x2, y2) = (np.max(x), np.max(y))
    
cropped_image = img[x1:x2+1, y1:y2+1]
    
    #plt.imshow(cv2.cvtColor(cropped_image,cv2.COLOR_BGR2RGB))
    
    
    #plt.show()

plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
plt.show()
reader = easyocr.Reader(['en'])
result = reader.readtext(cropped_image)
print(result)


if len(result) !=0:
    text = result[0][-2]
    font = cv2.FONT_HERSHEY_SIMPLEX
    res = cv2.putText(img, text=text, org=(approx[0][0][0], approx[1][0][1]+60), fontFace=font, fontScale=1, color=(0,255,0), thickness=2, lineType=cv2.LINE_AA)
    res = cv2.rectangle(img, tuple(approx[0][0]), tuple(approx[2][0]), (0,255,0),3)
    plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
    plt.show()
else:
    print("Cant find text")
    print(result)


"""""
def has_numbers(inputString): #parbauda vai string ir tikai skaitli.
    return any(char.isdigit() for char in inputString)


image_path = 'carimg4.jpg' #!!!!!!!!!sheit ir bildes path

reader = easyocr.Reader(['en'], gpu=False)
result = reader.readtext(image_path, detail=0)
print(result)

elon_array = np.array(result) #List to array lai var stradat ar array nevis list

print(elon_array) #lai parbauditu
text1 = "aaa"
for i in elon_array: # ejam cauri un meklejam to ko vajag
    if "-" in i:
        text1 = i
        print(i) #izvadam atrasto pec filtriem
"""      
        
loginurl=('https://e.csdd.lv/login/?action=doLogin')
secureurl=('https://e.csdd.lv/')
searchurl=('https://e.csdd.lv/tadati/')

payload= {
    'email': 'eduardsosh@gmail.com',
    'psw': 'Parole123-1',
}
plate= {
    'rn':text
}

with requests.session() as s:
    cookies = requests.utils.cookiejar_from_dict(requests.utils.dict_from_cookiejar(s.cookies))
    s.post(loginurl, data=payload)
    r = s.post(searchurl, data=plate)
    soup = BeautifulSoup(r.content, 'html.parser')
    tabula = soup.find('table', class_ = 'table-list')
for row in tabula.find_all("tr")[1:]:
    print([cell.get_text(strip=True) for cell in row.find_all("td")])




        
        

    






