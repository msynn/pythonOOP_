# Pake dictionary
diketahui = {"Nama": "Fyan Ramadhan", "NIM": "D0221090", "Gaji Pokok": 1000000, "gaji lembur\jam": 5000, "lama Lembur": 90, "Pajak": 0.09}

gajiLembur = diketahui["gaji lembur\jam"] * diketahui["lama Lembur"]
totalPajak = diketahui["Gaji Pokok"] * diketahui["Pajak"]
gajiBersih = diketahui["Gaji Pokok"] + gajiLembur - totalPajak
print(f"Gaji Bersih = {gajiBersih}")


# Pake variabel biasa
nama = "Sadly Ramli"
nim = "D0217011"
gajiPokok = 1000000
gajiLembur = 5000
lamaLembur = 11 #Sesuai 2 angka dibelakang NIM
pajak = 0.09

totalPajak = gajiPokok * pajak
gajiKotor = gajiPokok - totalPajak
gajiBersih = gajiKotor + (gajiLembur * lamaLembur)


print(f"Nama\t\t: {nama}")
print(f"NIM\t\t: {nim}")
print(f"Gaji Pokok\t: {gajiPokok}")
print(f"Gaji Lembur\t: {gajiLembur}")
print(f"Lama Lembur\t: {lamaLembur}")
print(f"Pajak\t\t: {pajak}")
print(f"Total Pajak\t: {totalPajak}")
print(f"Gaji Kotor\t: {gajiKotor}")
print(f"Gaji Bersih\t: {gajiBersih}")