# Membuat program barang
tampungan_barang = []

def tambah():
    print('MENU TAMBAH BARANG'.center(50,"-"))
    while True :
        barang = input('Masukkan barang\t: ')
        harga = int(input('Masukkan harga\t: '))
        barang_dan_harga = [barang,harga]
        tampungan_barang.append(barang_dan_harga)
        pilihan = input("Tambahkan barang lagi? (y/n) : ")
        if pilihan == 'y' :
            print('-'*50)
            print("LIST BARANG".center(50,'='))
            print('-'*50,"\n")
            for i in tampungan_barang :
                print("+ Kode Barang ",(tampungan_barang.index(i)+1) ,"|", (i[0]).center(15, ' ') ,"|", (i[1]), "+")
            print("\n",'-'*50)
        elif pilihan == 'n' :
            menu()
        else :
            print('Invalid sintax')
            break


# Menghapus Barang     
def menghapus():
    print('-'*50)
    print('Menghapus barang'.center(50,'='))
    print('-'*50)
    delete = input('Kode barang\t: ')
    if delete in tampungan_barang :
        tampungan_barang.remove()
    else :
        print('Kode barang tidak ada!'.center(50,'-'))
    # Exit
    pilihan = input('Lanjut menghapus barang? (y/n) : ')
    if pilihan == 'y' :
        pass
    elif pilihan == 'n' :
        menu()
 
# Cek barang        
def cek_barang():
    print('-'*50)
    print("LIST BARANG".center(50,'='))
    print('-'*50,"\n")
    for i in tampungan_barang :
        print("+ Kode Barang ",(tampungan_barang.index(i)+1) ,"|", (i[0]).center(15, ' ') ,"|", (i[1]), "+")
    print("\n",'-'*50)
    
    # Edit
    print("1. Edit Nama barang")
    print("2. Edit Harga barang")
    print("3. Kembali ke menu!")
    pilihan = input("Masukkan Pilihan : ")
    if pilihan == "1":
        print("Edit Nama Barang".center(50,'-'))
        edit = input("Masukkan nama barang yang akan di edit : ")
        if edit in tampungan_barang[0]:
            edit_jadi = input("Ubah ke : ")
            tampungan_barang[edit] = edit_jadi
        else:
            print('barang tidak ditemukan!')
    elif pilihan == "2":
        print("Edit Harga Barang".center(50,'-'))
        edit = input("Masukkan nama barang yang akan di edit : ")
        if edit in tampungan_barang[1]:
            edit_jadi = int(input("Ubah ke : Rp. "))
            tampungan_barang[int(edit)] = edit_jadi       
    else :
        menu()
            
def menu():
    print('-'*50)
    print("PROGRAM BARANG".center(50,'='))
    print('-'*50)
    print("1. Memasukan barang")
    print("2. Menghapus barang")
    print("3. Cek Barang")
    pilihan = int(input("Pilih menu \t:"))
    if pilihan == 1 :
        tambah()
    elif pilihan == 2:
        menghapus()
    elif pilihan == 3:
        cek_barang()

menu()