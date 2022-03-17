# Contoh soal
# Mencari gaji bersih
nama = "Fyan Ramadhan"
gaji_pokok = 1000000
gaji_lembur_perjam = 5000
lama_lembur = 11
pajak = 0.09

potongan = gaji_pokok * pajak
total_gajiLembur = gaji_lembur_perjam * lama_lembur
gaji_kotor = gaji_pokok + total_gajiLembur
gaji_bersih = gaji_kotor - potongan

print("Nama\t\t\t:", nama)
print("Gaji pokok\t\t :", gaji_pokok)
print("total gaji lembur\t:", total_gajiLembur)
print("potongan\t\t:", potongan)
print("Gaji bersih \t\t:", gaji_bersih)