list_barang = []
def Backtomenu():
    pilihan = int(input("Tekan 1 untuk kembali ke menu :"))
    print("MENU")
    print("1. Memasukan barang")
    print("2. Menghapus barang")
    print("3. Cek Barang")
    pilihan = int(input("Pilih menu \t:"))
    if pilihan == 1 :
        masukkanBarang()
    elif pilihan == 2:
        remove()
    elif pilihan == 3:
        cekBarang()
  
    
def masukkanBarang():
    print("\n\nMasukkan barang\n")
    while True :
        barang = input("Nama barang \t : ")
        harga = int(input("Harga barang \t : "))

        barang_baru = [barang, harga]
        list_barang.append(barang_baru)
        
        
        print("="*30)
        print(" Daftar Barang ".center(30, "="))
        print("="*30)
        print(" No.\t| Nama Barang | Harga Barang |")
        for index,barangnew in enumerate(list_barang):
            print(f" {index+1} \t| {barangnew[0]} \t\t| {barangnew[1]} \t\t|")
            
        print("\n\n","="*30)
        lanjut = input("Apakah anda ingin menambahkan barang lagi (y/n) : ")
        if lanjut == "n" :
            Backtomenu()
          
def remove():
    while True :
        pilihan = int(input("Pilih nomor barang yang akan dihapus : "))
        del list_barang[pilihan - 1]
    
        print("\n\n","="*30)
        lanjut = input("Apakah anda ingin menghapus barang lagi? (y/n) : ")
        if lanjut == "n" :
            Backtomenu()
    
def cekBarang():
    print("="*30)
    print(" Daftar Barang ".center(30, "="))
    print("="*30)
    print(" No.\t| Nama Barang | Harga Barang |")
    for index,barangnew in enumerate(list_barang):
        print(f" {index+1} \t| {barangnew[0]} \t\t| {barangnew[1]} \t\t|")

# Program List barang

print("MENU")
print("1. Memasukan barang")
print("2. Menghapus barang")
print("3. Cek Barang")
pilihan = int(input("Pilih menu \t:"))
if pilihan == 1 :
    masukkanBarang()
elif pilihan == 2:
    remove()
elif pilihan == 3:
    cekBarang()










