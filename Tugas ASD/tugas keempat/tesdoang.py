tampungan = []

def menu():
    while True :
        print("PROGRAM INPUTAN BARANG")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Lihat Barang")
        print("4. Edit Barang")
        print("5. Exit")

        pilihan = input('Choose Number : ')
        if pilihan == '1':
            tambah_barang()
        elif pilihan == '2':
            hapus()
        
    
    
def garis():
    print("-"*34)
    
def tambah_barang():
    garis()
    print(" Menu Tambah Barang ".center(34,'='))
    garis()
    while True :
        barang = input("Masukkan Barang : ")
        tampungan.append(barang)
        for i in tampungan :
            print(f"{tampungan.index(i)+1} ---- {i}")
        lanjut = input("Lanjut (Y/N) : ").lower()
        if lanjut == 'y':
            pass
        else:
            break
        
def hapus():
    garis()
    print(" Menu hapus Barang ".center(34,'='))
    garis()   
    while True : 
        delete = input("Masukkan nama barang yang akan dihapus : ")       
        if delete in tampungan :
            tampungan.remove(delete)
            lanjut = input('Lanjut hapus? <Y/N> : ').lower()
            if lanjut == 'y':
                pass
            else :
                break
        elif delete not in tampungan :
            print("Barang Tidak Tersedia!")
            pass
        
menu()