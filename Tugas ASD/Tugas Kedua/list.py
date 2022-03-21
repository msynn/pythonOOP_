# 1. Buatlah contoh codingan collections(List, Set, Tuple, dan dictionary)
# 2. Isilah masing-masing Collections tersebut dengan beberapa value/nilai,
#    kemudian tampilkan menggunakan perulangan
# 3. Cobalah update salah satu value dari masing - masing collections tersebut, 
#    jelaskan apa yang terjadi
# 4. Coba hapus salah satu value dari masing-masing Collections, 
#    jelaskan apa yang terjadi.
# 5. Coba tambahkan value dari masing-masing collections tersebut,
#    jelaskan apa yang terjadi.

# List
buah = ["apel", "jeruk", "mangga", "melon", "nangka"]

# Update value
buah[0] = "Lemon"

# # menghapus value
# # indexnya
buah.pop(3)
# # itemnya
buah.remove(nangka)
# # indexnya
del buah[0]

# Menambahkan value
buah.append("nanas")
buah.insert(0, "jambu")

for buah_buahan in buah :
    print(f"ini buah {buah.index(buah_buahan)+1}: {buah_buahan}")
    


tupel = (1,2,3)
tupel += (7,8,9)
print(tupel)