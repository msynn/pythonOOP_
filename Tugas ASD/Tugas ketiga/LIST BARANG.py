# Tampungan barang
tampungan_barang = []

def menu():
    print('-'*40)
    print(" PROGRAM BARANG ".center(40,'='))
    print('-'*40)
    
    print('''
1. Tambah barang
2. Hapus barang
3. Cek barang
4. Edit
5. Cek Ketersediaan barang
6. Cek Index
7. Keluar

          ''')
    print('-'*40)
    pilihan = input('Masukkan kode menu : ')
    if pilihan == '1' :
        tambah_barang()
    elif pilihan == '2':
        hapus_barang()
    elif pilihan == '3':
        cek_barang()
    elif pilihan == '4':
        edit()
    elif pilihan == '5':
        cek_ketersediaan_brg()
    elif pilihan == '6':
        cek_index()
    else :
        print('+ TERIMAKASIH +'.center(40,' '))
    
    
        
# TAMBAH BARANG
def tambah_barang():    
    print('-'*40)
    print(" TAMBAH BARANG ".center(40,'='))
    print('-'*40)
    while True :    
        tambah_brg = input('Masukkan nama barang : ')
        tampungan_barang.append(tambah_brg)
        print("\nLIST BARANG")
        for i in tampungan_barang:
            print("Barang : ",i)
        lanjut = input('Lanjut menambahkan barang (y/n) : ')
        if lanjut == 'y':
            pass
        else :
            menu()
 
# HAPUS BARANG           
def hapus_barang():
    print('-'*40)
    print(" HAPUS BARANG ".center(40,'='))
    print('-'*40)
    
    while True :
        hapus_brg = input('Masukkan nama barang yang akan dihapus : ')
        if hapus_brg in tampungan_barang:
            tampungan_barang.remove(hapus_brg)
            print("\nBARANG TERSISA")
            for i in tampungan_barang:
                print("Barang : ",i)
            lanjut = input('Lanjut menghapus barang (y/n) : ')
            if lanjut == 'y':
                pass
            else :
                menu()
        else :
            print('''
MAAF BARANG YANG INGIN
ANDA HAPUS TIDAK TERSEDIA!
''')
            pass
        
      
# CEK BARANG
def cek_barang():
    print("\nBARANG TERSISA")
    print("KODE BARANG".center(15, ' '), "NAMA BARANG".center(20,' '))
    for i in tampungan_barang:
        print("+     ",tampungan_barang.index(i)+1,"          |", (i).center(15,' '), " +")
    keluar = input('Tekan Enter untuk kembali ke menu :')
    if keluar == " ":
        menu()
    else :
        menu()

def edit():  
    print('-'*40)
    print(" EDIT BARANG ".center(40,'='))
    print('-'*40)
    print('\n')
    print("KODE BARANG".center(15, ' '), "NAMA BARANG".center(20,' '))
    for i in tampungan_barang:
        print("+     ",tampungan_barang.index(i)+1,"       |", (i).center(15,' '), " +")
    print('-'*40,'\n')
    
    while True :
        edit = input('Masukkan nama barang yang ingin di edit : ')
        if edit in tampungan_barang:
            ubah = input('Ubah nama barang ke :')
            tampungan_barang[tampungan_barang.index(edit)] = ubah
            print('\n')
            print("KODE BARANG".center(15, ' '), "NAMA BARANG".center(20,' '))
            for i in tampungan_barang:
                print("+     ",tampungan_barang.index(i)+1,"       |", (i).center(15,' '), " +")
            print('-'*40,'\n')
            lanjut = input('Lanjut mengedit barang (y/n) : ')
            if lanjut == 'y':
                pass
            else :
                menu()
            
        else :
            print("\nBARANG TIDAK TERSEDIA!\n")
            pass
        
def cek_ketersediaan_brg():
    print('-'*40)
    print(" CEK KETERSEDIAAN BARANG ".center(40,'='))
    print('-'*40)
    print('\n')
    while True :
        cek_brg = input('Masukkan nama barang : ')
        if cek_brg in tampungan_barang:
            print(cek_brg, ' Tersedia!')
            lanjut = input('Lanjut mengecek barang (y/n) : ')
            if lanjut == 'y':
                pass
            else :
                menu()
            
        else :
            print(cek_brg, 'Tidak Tersedia!')
            pass
        
def cek_index():
    print('-'*40)
    print(" CEK INDEKS BARANG ".center(40,'='))
    print('-'*40)
    print('\n')
    while True :
        cek_brg = input('Masukkan nama barang : ')
        if cek_brg in tampungan_barang:
            print(cek_brg, 'berada pada indeks ke : ', tampungan_barang.index(cek_brg))
            lanjut = input('Lanjut mengecek indeks barang (y/n) : ')
            if lanjut == 'y':
                pass
            else :
                menu()
            
        else :
            print(cek_brg, 'Tidak Tersedia!')
            pass
    
        
menu()