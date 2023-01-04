from rembg import remove
from PIL import Image
import os

def rem_bg () :

    for i in range(3):
        # Baca file 'hasil/insta_i.jpg'
        filename = f'insta_{i}.jpg'
        filepath = os.path.join('static/original', filename)
        im = Image.open(filepath)

        # Proses gambar dengan fungsi remove
        output = remove(im)

        # Simpan gambar ke direktori 'result' dengan nama 'nobg_i.png'
        outfilename = f'nobg_{i}.png'
        outfilepath = os.path.join('static/nobackground', outfilename)
        output.save(outfilepath)