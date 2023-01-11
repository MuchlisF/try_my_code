import os
import random
import string

template_data = {
    'judul' : 'judul',
    'penulis' : 'penulis',
    'tahun_terbit' : 0000,
    'penerbit' : 'penerbit'
}
data_buku = {}

def header():
    os.system('clear')
    print('Selamat Datang Di Program Data Perpustakaan')
    print('''===== Silahkan Pilih Menu =====
    1. Tambah Data Buku
    2. Hapus Data Buku
    3. Cek Daftar Buku
    0. Keluar\n''')

while True:
    header()
    
    isInput = int(input("Masukkan opsi : "))
    
    if isInput == 1:
        while True :
            os.system('clear')
            print('== Masukkan Data Buku ==')
            buku = dict.fromkeys(template_data.keys())
            buku['judul'] = (input('Judul Buku : '))
            buku['penulis'] = (input('Penulis : '))
            buku['tahun_terbit'] = int(input('Tahun Terbit : '))
            buku['penerbit'] = (input('Penerbit : '))
            print()
            KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
            data_buku.update({KEY:buku})
    
            print(f"{'KEY':<8} {'JUDUL':<24} {'PENULIS':<16} {'TAHUN_TERBIT':<4} {'PENERBIT':<18}")
            print('='*74)
            for buku in data_buku:
                KEY = buku
                JUDUL = data_buku[KEY]['judul']
                PENULIS = data_buku[KEY]['penulis']
                TAHUN_TERBIT = data_buku[KEY]['tahun_terbit']
                PENERBIT = data_buku[KEY]['penerbit']
                print(f"{KEY:<8} {JUDUL:<24} {PENULIS:<16} {TAHUN_TERBIT:<12} {PENERBIT:<18}")
            
            isDone = (str(input('Apakah anda sudah selesai ? y/n : ')))
            if isDone == 'y':
                break

    elif isInput == 2 :
        while True :
            os.system('clear')
            print('== Masukkan Data Buku Yang Akan Dihapus ==')
            data_buku.items()
            
            print(f"{'KEY':<8} {'JUDUL':<24} {'PENULIS':<16} {'TAHUN_TERBIT':<4} {'PENERBIT':<18}")
            print('='*74)
            for buku in data_buku:
                KEY = buku
                JUDUL = data_buku[KEY]['judul']
                PENULIS = data_buku[KEY]['penulis']
                TAHUN_TERBIT = data_buku[KEY]['tahun_terbit']
                PENERBIT = data_buku[KEY]['penerbit']
                print(f"{KEY:<8} {JUDUL:<24} {PENULIS:<16} {TAHUN_TERBIT:<12} {PENERBIT:<18}")
            
            buku_dihapus = input('Masukkan key data yang dihapus : ')
            data_buku.pop(buku_dihapus)
            
            os.system('clear')
            print('Data telah dihapus\n')
            
            isDone = (str(input('Apakah anda sudah selesai ? y/n : ')))
            if isDone == 'y':
                break

    elif isInput == 3:
        os.system('clear')
        print('== Daftar Buku ==')
        data_buku.items()
        
        print(f"{'KEY':<8} {'JUDUL':<24} {'PENULIS':<16} {'TAHUN_TERBIT':<4} {'PENERBIT':<18}")
        print('='*74)
        for buku in data_buku:
            KEY = buku
            JUDUL = data_buku[KEY]['judul']
            PENULIS = data_buku[KEY]['penulis']
            TAHUN_TERBIT = data_buku[KEY]['tahun_terbit']
            PENERBIT = data_buku[KEY]['penerbit']
            print(f"{KEY:<8} {JUDUL:<24} {PENULIS:<16} {TAHUN_TERBIT:<12} {PENERBIT:<18}")
        
        isDone = (str(input('Apakah anda sudah selesai ? y/n : ')))
        if isDone == 'y':
            pass

    else :
        break

os.system('clear')
print('='*40, '\n    Terima Kasih Atas Kunjungan Anda\n','='*38)