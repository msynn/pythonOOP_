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
buah = ["anggur", "pepaya", "nangka", "strawberry", "manggis"]
# update value
buah[0] = "apel"
# remove value
del buah[2] # menghapus value dari index ke 2 = nangka
# tambah value
buah.append("melon")
for i in buah:
    print(i)
print("======================")

# Set
value = {1,2,3,4,5, "string1", "string2", "string3"}
value2 = {3,4,5,6,7,8,9}
union = (value | value2)
# update value
# remove value tidak memiliki indeks
value.remove(1) # menghapus value 1
value.remove("string1") # menghapus value string1
# tambah value
value.add("angka")
valuetambah = {"ini adalah value tambahan"}
value.update(valuetambah)
print(value)
print("======================")
intersection = (value & value2)
for i in union:
    print(i)
print("======================")
for i in intersection:
    print(i)
print("======================")

# Tuple
random = ("a", "b", "c", "d", "e")
# update value (tidak bisa)
# remove value (tidak bisa)
# tambah value (tidak bisa)
for i in random:
    print(i)
print("======================")

# Dictionar
data_diri = {"nama": "Rizki", "umur": "20", "alamat": "Jl. Kebon Kacang"}
# Menambahkan value
data_diri.update({"ID":"10217100"})
# Menghapus value
data_diri.pop("umur")
# update value
data_diri["nama"] = "Rizki Fadhillah"
item = data_diri.items()
for i,j in item:
    print(i,"\t:",j)
print("======================")