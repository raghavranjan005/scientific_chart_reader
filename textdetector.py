import cv2
import pytesseract
from pytesseract import Output


image_path='image5.png'


img=cv2.imread(image_path)

custom_config=r'--oem 3 --psm 6'

custom_config1=r'--oem 3 --psm 3'

custom_config2=r'--oem 3 --psm 11'

text=pytesseract.image_to_string(img,config=custom_config2)
d=pytesseract.image_to_data(img,config=custom_config,output_type=Output.DICT)

print(text)

# n_boxes = len(d['text'])
# for i in range(n_boxes):
#     if int(d['conf'][i]) > 60:
#         (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#         img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# cv2.imshow('img', img)
# cv2.waitKey(0)

