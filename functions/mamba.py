import cv2
import numpy as np
from PIL import Image
import os


def hitung_mamba () :

# Merubah warna background
    for i in range(3):
        fill_color = (120, 8, 220)  # your new background color
        im = Image.open(f"static/nobackground/nobg_{i}.png")
        im = im.convert("RGBA")  # it had mode P after DL it from OP
        if im.mode in ('RGBA', 'LA'):
            background = Image.new(im.mode[:-1], im.size, fill_color)
            background.paste(im, im.split()[-1])  # omit transparency
            im = background

# Ubah warna latar belakang menjadi hitam
        im = im.convert("RGB")

# Simpan gambar yang telah diubah
        im.save(f"static/masking/mamba/purple-bg/background_{i}.png")

# Menampung Nilai Mamba
    awal = []
    for i in range(3):
        img = cv2.imread(f"static/masking/mamba/purple-bg/background_{i}.png")
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Color
        HITAM = cv2.inRange(hsv, (0, 0, 0), (180, 255, 50))
        ABU = cv2.inRange(hsv, (0, 0, 0), (0, 0, 0))

# Calculate
        HITAM_CAL = np.average(HITAM)
        HASIL_HITAM = (HITAM_CAL / 70) * 200

        ABU_CAL = np.average(ABU)
        HASIL_ABU= (ABU_CAL / 70) * 200

# Hasil
        Jumlah_Mamba = round( HASIL_HITAM + HASIL_ABU)
        awal.append(Jumlah_Mamba)

# Menampilkan ketiga nilai
        # print(f"Mamba {i} :", round(Jumlah_Mamba), "%")

# Masking

        mask2 = cv2.bitwise_or(HITAM, ABU)
        target = cv2.bitwise_and(img,img, mask= mask2)

#Save
        outfilename = f'masking_mamba_{i}.png'
        outfilepath = os.path.join('static/masking/mamba', outfilename)
        cv2.imwrite(outfilepath, target)

#Hasil Hitungan
    jumlah = round(sum(awal) / 3)

    if jumlah > 100:
        print("Mamba: 100 %")
        return 100
    else:
        print("Mamba :",jumlah, "%")
        return jumlah