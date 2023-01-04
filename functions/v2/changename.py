
import os
def rename_dua() :
    import os

    # Menentukan nama folder
    folder = 'static/original'

    # Membuat daftar semua file di dalam folder
    files = os.listdir(folder)

    # Menelusuri daftar file
    for file in files:
        # Mengganti nama file yang sesuai dengan kriteria
        if file.startswith('insta_3.jpg'):
            os.rename(os.path.join(folder, file), os.path.join(folder, file.replace('insta_3.jpg', 'insta_0.jpg')))



