# Program List barang
from tkinter import CENTER


print("\n\nMasukkan barang\n")

list_barang = []

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
        break
