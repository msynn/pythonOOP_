# For loop
print("for loop")
kumpulan_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for angka in kumpulan_angka :
    print(f"Angka ke {angka}")
    
# for loop and range
print("\n\nfor loop and range")
kumpulan_angka = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
panjang = len(kumpulan_angka)
for i in range(panjang):
    print(f"Angka ke {i+1} adalah {kumpulan_angka[i]}")
    
# while
print("\n\nwhile loop")
kumpulan_angka = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
i = 0
while i < panjang:
    print(f"Angka ke {i+1} adalah {kumpulan_angka[i]}")
    i += 1
    
# List comprehension
print("\n\nList comprehension")
data = ["agung", "budi", "caca", "didi", "ega", "fafa", "gaga", "haha", "iaia", "jaja"]

[print(f"nama = {i}") for i in data]

print("\n\nList comprehension 2")

angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

# enumerate
print("\n\nEnumerate")
data = ["agung", "budi", "caca", "didi", "ega", "fafa", "gaga", "haha", "iaia", "jaja"]
for index, data in enumerate(data):
    print(f"index = {index} dan nama = {data}")