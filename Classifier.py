import json
import pytesseract
import cv2
import numpy as np
from PIL import Image
import ftfy
from aadhar_read import aadhaar_read_data
from pan_read import pan_read_data
import io


def classifier(filename):
    # filename = "cropped1.png"

    img = cv2.imread(filename)


    img = cv2.resize(img, None, fx=2, fy=2,interpolation=cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    var = cv2.Laplacian(img, cv2.CV_64F).var()
    print(var)
    if var < 10:
        print("Image is Too Blurry....")
        k= input('Press Enter to Exit.')
        exit(1)



    text = pytesseract.image_to_string(Image.open(filename), lang = 'eng')

    text_output = open('output.txt', 'w', encoding='utf-8')
    text_output.write(text)
    text_output.close()

    file = open('output.txt', 'r', encoding='utf-8')
    text = file.read()

    text = ftfy.fix_text(text)
    text = ftfy.fix_encoding(text)



    if "income" in text.lower() or "tax" in text.lower() or "account" in text.lower() or "number" in text.lower():
        data = pan_read_data(text)
    elif "male" in text.lower() or "female" in text.lower() or "government" in text.lower():
        data = aadhaar_read_data(text)
    elif "election" in text.lower() or "commission" in text.lower() or "identity" in text.lower() or "card" in text.lower():
        data = 'Voter Card'
    elif "election" in text.lower() or "commission" in text.lower() or "identity" in text.lower() or "card" in text.lower():
        data = 'Voter Card'
    elif "republic" in text.lower() or "india" in text.lower() or "passport no." in text.lower() or "country code" in text.lower():
        data = 'Passport'

    # try:
    #     to_unicode = str
    # except NameError:
    # to_unicode = str
    # with io.open('info.json', 'w', encoding='utf-8') as outfile:
    #     data = json.dumps(data, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
    #     outfile.write(to_unicode(data))



    # with open('info.json', encoding = 'utf-8') as data:
    #     data_loaded = json.load(data)


    # if data_loaded['ID Type'] == 'PAN':
    #     print("\n---------- PAN Details ----------")
    #     print("\nPAN Number: ",data_loaded['PAN'])
    #     print("\nName: ",data_loaded['Name'])
    #     print("\nFather's Name: ",data_loaded['Father Name'])
    #     print("\nDate Of Birth: ",data_loaded['Date of Birth'])
    #     print("\n---------------------------------")
    # elif data_loaded['ID Type'] == 'ADHAAR':
    #     print("\n---------- ADHAAR Details ----------")
    #     print("\nADHAAR Number: ",data_loaded['Adhaar Number'])
    #     print("\nName: ",data_loaded['Name'])
    #     print("\nDate Of Birth: ",data_loaded['Date of Birth'])
    #     print("\nSex: ",data_loaded['Sex'])
    #     print("\n------------------------------------")
    # k = input("\n\nPress Enter To EXIT")
    # exit(0)




