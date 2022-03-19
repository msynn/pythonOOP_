# PENAMPUNGAN DATA
nama_mahasiswa = []

def garis(ulang):
    print(ulang*'-')

# Inputan data mahasiswa
def inputdata():
    nama = input("Masukkan nama : ")
    kelas = input("Masukkan kelas : ")
    nim = input("Masukkan nim : ")
    angkatan = input("Masukkan angkatan : ")
    datamhs = [nama, kelas, nim, angkatan]
    nama_mahasiswa.append(datamhs)
    
# menu tampilan   
def menu():
    garis(50)
    print("PROGRAM PENGINPUTAN MAHASISWA".center('=',50))
    print("Pilih menu :")
    print("1. Input data mahasiswa")
    print("2. Menghapus data mahasiswa")
    print("3. Tampilkan data mahasiswa")
    print("4. save data")
    print("5. back to menu")
    print("6. Exit")
    garis(50)
    pilihan = int(input("Masukkan pilihan : "))
    if pilihan == 1 :
       pass 

def back_menu():
