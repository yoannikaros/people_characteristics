
import os
import shutil

def rename() :

# Hapus
    folder = 'static/original'
    shutil.rmtree(folder)
    shutil.move("original", "static")

# Menentukan nama folder
    folder = 'static/original'

# Membuat daftar semua file di dalam folder
    files = os.listdir(folder)

# Menelusuri daftar file
    for file in files:
   # Menghapus file yang tidak memiliki ekstensi .jpg
        if not file.endswith('.jpg'):
            os.remove(os.path.join(folder, file))

# Menentukan direktori yang ingin diubah namanya
    direktori = 'static/original'

# Mengambil nama-nama file di direktori tersebut
    files = os.listdir(direktori)

# Melakukan loop untuk setiap file
    for i, file in enumerate(files):
# Memeriksa apakah file tersebut merupakan gambar
        if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.gif'):
# Membuat nama baru untuk file tersebut
            new_name = 'insta_{}.jpg'.format(i+1)
# Melakukan rename file tersebut
            os.rename(os.path.join(direktori, file), os.path.join(direktori, new_name))


