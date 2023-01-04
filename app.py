import os
from datetime import time

from flask import Flask, render_template,request

from functions.removebg import rem_bg
from functions.mamba import hitung_mamba
from functions.cake import hitung_cake
from functions.earth import hitung_bumi
from functions.instagram import downloadig
from functions.v2.remove import clear
from functions.v2.rename import rename
from functions.v2.scrapt import scrapt
from functions.v2.changename import rename_dua

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('option.html')

#UPLOAD MANUAL
@app.route("/file")
def manual():
    return render_template('index.html')

#PROSES UPLOAD MANUAL
@app.route('/upload', methods=['POST'])
def upload():
    # get the image files from the request
    image0 = request.files['image0']
    image1 = request.files['image1']
    image2 = request.files['image2']

    # save the image files to the static/manual folder with the new names
    image0.save('static/nobackground/nobg_0.png')
    image1.save('static/nobackground/nobg_1.png')
    image2.save('static/nobackground/nobg_2.png')
    mamba = hitung_mamba()
    earth = hitung_bumi()
    cake = hitung_cake()
    USERNAME = "Hasil yang kami dapat"
    return render_template('berhasil.html',cake = cake, earth = earth, mamba= mamba,USERNAME=USERNAME)

def allowed_file(filename):
    # allow only image files with the following extensions
    ALLOWED_EXTENSIONS = ['png']
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#PENCARIAN AKUN IG VERSI 1
@app.route("/v1")
def cari():
    return render_template('cari.php')

#PROSES PENCARIAN AKUN IG VERSI 1
@app.route("/download/<USERNAME>")
def download(USERNAME):
  #AMBIL URL DARI AKUN IG SEBANYAK 3X
  downloadig(USERNAME)
  #REMOVE BACKGORUND NYA
  rem_bg()
  #MENGHITUNG
  mamba = hitung_mamba()
  earth = hitung_bumi()
  cake = hitung_cake()
  return render_template('berhasil.html',cake = cake, earth = earth, mamba= mamba, USERNAME = USERNAME)

#PENCARIAN AKUN IG VERSI 2
@app.route("/v2")
def cari_v2():
    return render_template('scraper.php')

#PROSES PENCARIAN AKUN IG VERSI 2
@app.route("/scaper/<USERNAME>")
def scrap(USERNAME):
  try:
   #hapus folder original
    clear()
    #download gambar ig sebayak 3x
    scrapt(USERNAME)
    # hasil download itu dirubah namanya serta pindah folder dari original ke static/original
    rename()
   
    rename_dua()
    #menghapus background
    rem_bg()
  except:
    rename()
    rename_dua()
    rem_bg()
  #MENGHITUNG
  mamba = hitung_mamba()
  earth = hitung_bumi()
  cake = hitung_cake()
  clear()
  return render_template('berhasil.html',cake = cake, earth = earth, mamba= mamba, USERNAME = USERNAME)

#MENGHITUNG
@app.route("/mamba")
def mamba():
    return render_template('mamba.html')

@app.route("/cake")
def cake():
    return render_template('cake.html')

@app.route("/earth")
def earth():
    return render_template('earth.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('scraper.php'), 404

@app.errorhandler(500)
def page_notfound(error):
    return render_template('scraper.php'), 500

if __name__ == '__main__':
    app.run(debug=True)
