tampungan_barang = []

# Garis
def garis():
    print('-'*40)

# Tambah barang
def tambah():
    garis()
    print('Tambah barang'.center(40,'='))
    garis()
    while True :
        barang = input('Masukkan barang : ')
        tampungan_barang.append(barang)
        pilihan = input("Tambahkan barang lagi? (y/n) : ")
        if pilihan == 'y' :
            garis()
            print("LIST BARANG".center(40,'='))
            garis()
            print("Kode".center(12, ' '), "Nama Barang".center(20, ' '), "\n")
            for i in tampungan_barang :
                print("+    ",(tampungan_barang.index(i)+1) ,"    |", (i).center(15, ' '),"+")        
        else : 
            menu()
            
# Menghapus barang
def hapus_barang():
    garis()
    print('Hapus barang'.center(40,'='))
    garis()    
    while True :
        hapus = input('Masukkan nama barang yang akan dihapus : ')
        if hapus in tampungan_barang :
            tampungan_barang.remove(hapus)
            lanjut = input('tekan y jika lanjut : ').upper()
            if lanjut == "y" :
                hapus_barang()
            else :
                menu()   
        else :
            print('Barang tidak tersedia')
            hapus_barang()

# mengedit barang :
def edit_barang() :
    garis()
    print("LIST BARANG".center(40,'='))
    garis()
    for i in tampungan_barang :
        print("+ Kode Barang ",(tampungan_barang.index(i)+1) ,"|", (i).center(15, ' '),"+")
    while True :
        print('MENU EDIT BARANG'.center(40,'='))
        caribarang = str(input('Masukkan nama barang yang mau di edit : '))
        if caribarang in tampungan_barang :
            ubah_ke = input('Ubah ke : ')
            tampungan_barang[tampungan_barang.index(caribarang)] = ubah_ke
            for i in tampungan_barang :
                print("+ Kode Barang ".center(28," "),(tampungan_barang.index(i)+1) ,"|", (i).center(15, ' '),"+")
            print("\n",'-'*50)
        else :
            print('barang tidak ditemukan!')
            pass
        lanjut()

# lanjut
def lanjut():
    lanjut = input('Lanjut (y/n) : ')
    if lanjut == 'y' :
        pass
    else :
        menu()

# Tampilkan barang
def tampilkan_barang():
    garis()
    print("LIST BARANG".center(40,'='))
    garis()
    for i in tampungan_barang :
        print("+ Kode Barang ",(tampungan_barang.index(i)+1) ,"|", (i).center(15, ' '),"+")
    exit = input('Enter untuk keluar : ')
    if exit == ' ':
        menu()
    else :
        menu()

# cek barang
def cek_barang():
    while True :
        print('MENU CEK BARANG'.center(40,'='))
        cek = input('Nama barang  : ')
        if cek in tampungan_barang :
            print(cek,'Tersedia!')
        else :
            print(cek,'Tidak tersedia!')
        lanjut = input('Cek lagi? (y/n) :')
        if lanjut == 'y' :
            cek_barang()
        else :
            menu()
            
# Cek indeks
def cek_index():
        while True :
            print('MENU CEK INDEKS BARANG'.center(40,'='))
            cek = input('Masukkan nama barang  : ')
            if cek in tampungan_barang :
                print('Barang berada pada indeks :', tampungan_barang.index(cek))
            else :
                print('Barang tidak ada!')
            lanjut = input('Cek lagi? (y/n) :').upper()
            if lanjut == 'y' :
                pass
            else :
                menu()

# menu
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
5. Cek nama barang
6. Index Barang
7. Keluar''')
        pilihan = input("Pilih menu \t:").lower()
        if pilihan == "1" or pilihan == "TAMBAH BARANG":
            tambah()
        elif pilihan == "2" or pilihan == "HAPUS BARANG":
            hapus_barang()
        elif pilihan == "3" or pilihan == "EDIT BARANG":
            edit_barang()
        elif pilihan == "4" or pilihan == "CEK BARANG":
            tampilkan_barang()
        elif pilihan == "5" or pilihan == "CEK BARANG":
            cek_barang()
        elif pilihan == "6" or pilihan == "INDEX BARANG":
            cek_index()
        else :
            garis()
            print(' TERIMAKASIH '.center(40,"+"))
            garis()
            break

        
menu()