import cv2
import numpy as np
import os

def hitung_bumi () :

    nilai_earth = []

# Read
    for i in range(3):
        img = cv2.imread(f"static/nobackground/nobg_{i}.png")

# convert to hsv
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#Data Earth

        COKLAT_KHAKI = cv2.inRange(hsv, (25, 30, 30), (35, 255, 255))
        CREAM = cv2.inRange(hsv, (0, 0, 200), (180, 30, 255))
        COKLAT = cv2.inRange(hsv, (10, 100, 100), (15, 255, 255))

# Calculate
        coklat_HITUNG = np.average(COKLAT)
        HASIL_COKLAT= (coklat_HITUNG / 70) * 300

        CREAM_HITUNG = np.average(CREAM)
        HASIL_CREAM  = (CREAM_HITUNG / 70) * 300

        CKH_HITUNG = np.average(COKLAT_KHAKI)
        HASIL_CKH  = (CKH_HITUNG / 70) * 300


#Calculate
        Jumlah =  round( HASIL_CKH + HASIL_COKLAT + HASIL_CREAM)
        nilai_earth.append(Jumlah)

# Menampilkan seluruh nilai
        # print(f"Earth {i} :", round(Jumlah), "%")

# final mask and masked
        mask1 = cv2.bitwise_or(CREAM,COKLAT)
        target = cv2.bitwise_and(img,img, mask=mask1)

# Save
        outfilename = f'masking_earth_{i}.png'
        outfilepath = os.path.join('static/masking/earth', outfilename)
        cv2.imwrite(outfilepath, target)

#Hasil Hitungan
    jumlah = round(sum(nilai_earth) / 3)
    if jumlah > 100:
        print("Earth: 100 %")
        return 100
    else:
        print("Earth :",jumlah, "%")
        return jumlah