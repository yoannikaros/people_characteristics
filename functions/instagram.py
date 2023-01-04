import instaloader
import urllib.request
import os

def downloadig(USERNAME):

# Inisialisasi objek instaloader
    L = instaloader.Instaloader()

# Username yang akan di-download fotonya
    USERNAME = USERNAME

# Ambil profil pengguna
    profile = instaloader.Profile.from_username(L.context, USERNAME)

# Ambil media terbaru pengguna
    posts = list(profile.get_posts())

# Lakukan looping 3 kali
    for i in range(3):

# Ambil URL foto pada objek ke-i
        img_url = posts[i].url
        image_url = img_url

# Lakukan sesuatu dengan img_url di sini
        filename = f'insta_{i}.jpg'
        filepath = os.path.join('static/original', filename)
        urllib.request.urlretrieve(image_url, filepath)
