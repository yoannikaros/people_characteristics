import cv2
import numpy as np
import os

def hitung_cake () :

    nilai_cake = []
# Read
    for i in range(3):
        img = cv2.imread(f"static/nobackground/nobg_{i}.png")

# convert to hsv
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Data Cake
        MERAH = cv2.inRange(hsv, (160, 100, 200), (180, 255, 255))   #cerah
        MERAHMUDA = cv2.inRange(hsv, (0, 100, 100), (10, 255, 255))  # cerah
        ORANGE = cv2.inRange(hsv, (5, 100, 100), (25, 255, 255))  #cerah
        KUNING = cv2.inRange(hsv, (20, 100, 100), (30, 255, 255)) #cerah
        HIJAU = cv2.inRange(hsv, (50, 100, 100), (70, 255, 255))  #cerah

        BIRU = cv2.inRange(hsv, (100, 100, 100), (120, 255, 255)) #cerah
        UNGU = cv2.inRange(hsv, (140, 100, 100), (165, 255, 255))
        PINK = cv2.inRange(hsv, (145, 80, 100), (160, 255, 255))

# Calculate Merah
        MERAHMUDA_Cal = np.average(MERAHMUDA)
        Hasil_MerahMuda = (MERAHMUDA_Cal / 100) * 300

# Calculate Merah mUDA
        Merah_Cal = np.average(MERAH)
        Hasil_Merah = (Merah_Cal / 70) * 300

# Calculate Orange
        Orange_Cal = np.average(ORANGE)
        Hasil_Orange = (Orange_Cal / 70) * 300

# Calculate Kuning
        Kuning_Cal = np.average(KUNING)
        Hasil_kuning = (Kuning_Cal / 70) * 300

# Calculate Hijau
        Hijau_Cal = np.average(HIJAU)
        Hasil_hijau = (Hijau_Cal / 70) * 300

# Calculate Biru
        Biru_Cal = np.average(BIRU)
        Hasil_biru = (Biru_Cal / 70) * 300

# Calculate Ungu
        ungu_Cal = np.average(UNGU)
        Hasil_ungu = (ungu_Cal / 70) * 300

# Calculate Pink
        Pink_Cal = np.average(PINK)
        Hasil_pink = (Pink_Cal / 70) * 300

#Calculate
        Jumlah =round( Hasil_Merah + Hasil_Orange + Hasil_biru + Hasil_hijau + Hasil_ungu + Hasil_pink + Hasil_kuning + Hasil_MerahMuda)
        nilai_cake.append(Jumlah)

# Menampilakan nilai
        #print(f"Cake {i} :", round(Jumlah), "%")

# final mask and masked
        mask1 = cv2.bitwise_or(MERAH,KUNING,ORANGE,HIJAU)
        mask2 = cv2.bitwise_or(BIRU,UNGU,PINK)
        target = cv2.bitwise_and(img,img, mask=mask1 + mask2)

# Save
        outfilename = f'masking_cake_{i}.png'
        outfilepath = os.path.join('static/masking/cake', outfilename)
        cv2.imwrite(outfilepath, target)

#Hasil Hitungan
    jumlah = round(sum(nilai_cake) / 3)
    if jumlah > 100:
        print("Cake: 100 %")
        return 100
    else:
        print("Cake :",jumlah, "%")
        return  jumlah

