# 1. Buatlah contoh codingan collections(List, Set, Tuple, dan dictionary)
# 2. Isilah masing-masing Collections tersebut dengan beberapa value/nilai,
#    kemudian tampilkan menggunakan perulangan
# 3. Cobalah update salah satu value dari masing - masing collections tersebut, 
#    jelaskan apa yang terjadi
# 4. Coba hapus salah satu value dari masing-masing Collections, 
#    jelaskan apa yang terjadi.
# 5. Coba tambahkan value dari masing-masing collections tersebut,
#    jelaskan apa yang terjadi.

# makanan = {"bakso", 
#            "soto", 
#            "nasi goreng", 
#            "sate", 
#            "sop buntut"}

# # Update data (tidak bisa)

# # menghapus value
# makanan.remove("soto")

# # menambahkan value
# makanan.add("bubur")
# makanan.update(["capcay"])

# for i in makanan :
#     print("menu makanan : ", i)
    
# print(type(makanan))

# tuple
mainan = ("bola", "tenis", "bola voli", "bola basket")

# type data tuple tidak bisa di update
# menghapus value (tidak bisa)
# penambahan value
mainan += ("bola badminton", "bola sepak")

for i in mainan :
    print(i)
    
    


nama={"nama":"fyan Rama", "kelas" : "informatika F"}

for i in nama :
    print(i, nama[i])