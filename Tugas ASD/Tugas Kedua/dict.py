# 1. Buatlah contoh codingan collections(List, Set, Tuple, dan dictionary)
# 2. Isilah masing-masing Collections tersebut dengan beberapa value/nilai,
#    kemudian tampilkan menggunakan perulangan
# 3. Cobalah update salah satu value dari masing - masing collections tersebut, 
#    jelaskan apa yang terjadi
# 4. Coba hapus salah satu value dari masing-masing Collections, 
#    jelaskan apa yang terjadi.
# 5. Coba tambahkan value dari masing-masing collections tersebut,
#    jelaskan apa yang terjadi.

datadiri = {"nama" : "Fyan Ramadhan", "umur" : 19, "tinggi" : 175.5, "hobi" : "bermain game"}

# update
datadiri["tinggi"] = "seratus tujuh puluh"

# menghapus
datadiri.pop("hobi")

# Menambahkan value
datadiri["cita2"] = "polisi"
 
for i in datadiri :
    print(f"{i} \t : {datadiri[i]}") 
    
