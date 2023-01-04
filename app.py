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

@app.route("/file")
def manual():
    return render_template('index.html')

#UPLOAD MANUAL DATASET
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

@app.route("/v1")
def cari():
    return render_template('cari.php')

@app.route("/download/<USERNAME>")
def download(USERNAME):
  downloadig(USERNAME)
  rem_bg()
  mamba = hitung_mamba()
  earth = hitung_bumi()
  cake = hitung_cake()
  return render_template('berhasil.html',cake = cake, earth = earth, mamba= mamba, USERNAME = USERNAME)

@app.route("/v2")
def cari_v2():
    return render_template('scraper.php')

@app.route("/scaper/<USERNAME>")
def scrap(USERNAME):
  try:
    clear()
    scrapt(USERNAME)
    rename()
    rename_dua()
    rem_bg()
  except:
    rename()
    rename_dua()
    rem_bg()
  mamba = hitung_mamba()
  earth = hitung_bumi()
  cake = hitung_cake()
  clear()
  return render_template('berhasil.html',cake = cake, earth = earth, mamba= mamba, USERNAME = USERNAME)

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