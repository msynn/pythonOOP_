tampungan = []

def menu():
    while True :
        print('-'*40)
        print("PROGRAM BARANG".center(40,'='))
        print('-'*40)
        print('''
1. Tambah Barang
2. Hapus Barang
3. Edit Barang
4. Cek Barang
5. Cek Barang apakah sudah ada dalam list
6. Index Barang
7. Keluar''')
        pilihan = int(input("Pilih menu \t:"))
        if pilihan == 1 :
            tambah()
        elif pilihan == 2 :
            hapus()
        elif pilihan == 3 :
            edit_brg()

def tambah():
    while True :
        print('-'*40)
        print(" TAMBAH BARANG ".center(40,'='))
        print('-'*40,"\n")
        tambah_brg = input("Masukkan nama barang : ")
        tampungan.append(tambah_brg)
        print('-'*40)
        for i in tampungan :
            print("Nomor", "Nama Barang".center(20,' '))
            print("  ",tampungan.index(i)+1),"  ", (i).center(20,' ')
        print('-'*40)
        lanjut = input('Tekan y jika lanjut : ')
        if lanjut == "y" :
             tambah()
        else :
            menu()

def hapus():
    print('-'*40)
    print(" TAMBAH BARANG ".center(40,'='))
    print('-'*40,"\n")
    
    
    hps_brg = input('Masukkan nama brg : ')
    if hps_brg in tampungan:
        tampungan.remove(hps_brg)
        print('-'*40)
        for i in tampungan :
            print("Nomor", "Nama Barang".center(20,' '))
            print("  ",tampungan.index(i)+1),"  ", (i).center(20,' ')
        print('-'*40)
        
        # Untuk lanjut atau kembali
        lanjut = input('Tekan y jika lanjut : ')
        if lanjut == "y" :
             hapus()
        else :
            menu()
    # Jika brg tdk ada
    else :
        print('Barang tidak ditemukan!')
        hapus()


# edit barang  
def edit_brg ():
    print('-'*40)
    print(" EDIT BARANG ".center(40,'='))
    print('-'*40,"\n")
    print('-'*40)
    for i in tampungan :
        print("Nomor", "Nama Barang".center(20,' '))
        print("  ",tampungan.index(i)+1),"  ", (i).center(20,' ')
    print('-'*40)
    edit = input("Nama Barang (edit) : ")
    if edit in tampungan :
        ubah_ke = input('Ubah ke : ')
        tampungan[edit] = ubah_ke[0]
        print('-'*40,"\n")
        for i in tampungan :
            print("Nomor".center(15," "), "Nama Barang".center(20,' '))
            print((tampungan.index(i)+1).center(15,' '), {i}.center(20,' '))
        print('-'*40)
    
menu()