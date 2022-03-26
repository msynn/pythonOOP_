barang = []

def menu():
    A = True
    while A == True :
        print('MENU UTAMA')
        print('1. Tambah barang')
        print('2. Hapus barang')
        print('3. Cek barang')
        print('4. Edit barang')
        print('5. Cek ketersediaan barang')
        print('6. Cek Indeks barang')
        print('7. Keluar')
        pilih = input('pilih kode menu : ')
        if pilih == "1":
            tambah()
        elif pilih == "2":
            hapus()
        elif pilih == "3":
            cek()
        elif pilih == "4":
            edit()
        elif pilih == "5":
            cek_ketersediaan()
        elif pilih == "6":
            cek_indeks()
        elif pilih == "7":
            print("TERIMAKASIH")
            A = False
            exit = input("Tekan enter ")
            if exit == " ":
                break
            else :
                break            
        else :
            print("TERIMAKASIH")
            A = False
            break
     
# Fungsi Tambah barang        
def tambah():
    print('MENU ADD')
    while True :
        inputan = input('Masukkan barang : ')
        barang.append(inputan)
        print("BARANG :")
        for i in barang :
            print(i)
        lanjut = input('Lanjut (y/n) : ')
        if lanjut == 'y' :
            pass
        else :
            break

# Fungsi hapus barang
def hapus():
    print('MENU DELETE')
    while True :
        delete = input('Masukkan barang yang ingin dihapus :')
        if delete in barang:
            barang.remove(delete)
            lanjut = input('Lanjut (y/n) : ')
            if lanjut == 'y' :
                pass
            else :
                break
        else :
            print('Barang Tidak ada!')
            pass

def edit():
    print('MENU EDIT')
    print("BARANG :")
    for i in barang :
        print(i)
    while True :
        edit_brg = input('Masukkan barang yang ingin diedit : ')
        if edit_brg in barang :
            ubah = input('Ubah menjadi\t:')
            barang[barang.index(edit_brg)] = ubah
            lanjut = input('Lanjut (y/n) : ')
            if lanjut == 'y' :
                pass
            else :
                break

def cek():
    print("BARANG :")
    for i in barang :
        print(i)
    exit = input('Tekan enter ')
    if exit == " ":
        menu()
    else :
        menu()

def cek_ketersediaan():
    print("MENU CEK KETERSEDIAAN BARANG")
    while True :
        cek = input("Masukkan nama barang : ")
        if cek in barang:
            print(cek, 'Tersedia!')
            lanjut = input('Lanjut (y/n) : ')
            if lanjut == 'y' :
                pass
            else :
                break
        else :
            print("Barang Tidak Tersedia!")
            break
        
def cek_indeks():
    print("MENU CEK INDEKS BARANG")
    while True :
        cek = input("Masukkan nama barang : ")
        if cek in barang:
            print(cek, 'Tersedia pada indeks', barang.index(cek))
            lanjut = input('Lanjut (y/n) : ')
            if lanjut == 'y' :
                pass
            else :
                break
        else :
            print("Barang Tidak Tersedia!")
            break

            
menu()