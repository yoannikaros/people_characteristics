import shutil
import os

def clear () :

    try:
    # Hapus
        folder = 'original'
        shutil.rmtree(folder)
    # Hapus
        folderku = 'static/original'
        shutil.rmtree(folderku)
    #Buat baru
        foldernya = 'static/original'
        os.makedirs(foldernya)
    except:
    # Hapus
        folderku = 'static/original'
        shutil.rmtree(folderku)
    #Buat baru
        foldernya = 'static/original'
        os.makedirs(foldernya)
