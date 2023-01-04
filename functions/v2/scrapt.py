import instaloader

def scrapt(USERNAME) :

# Inisialisasi Instaloader
    L = instaloader.Instaloader()

# Ambil foto terbaru dari profil Instagram yang ditentukan
    USERNAME = USERNAME
    profile = instaloader.Profile.from_username(L.context, USERNAME)

# Tentukan pola nama file yang ingin Anda gunakan
    filename_pattern = "original"

# Iterasikan melalui setiap foto di profil tersebut dan download foto yang diinginkan
    i = 1
    for post in profile.get_posts():
   # Download foto yang sesuai dengan kriteria Anda
        if i <= 3:
            L.download_post(post, target=filename_pattern)
            i += 1



