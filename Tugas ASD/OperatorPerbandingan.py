nama = "Fyan Ramadhan"
gaji_pokok = 1000000
gaji_lembur_perjam = 5000
lama_lembur = 11
pajak = 0.09
potongan = gaji_pokok * pajak
gaji_kotor =  gaji_pokok + (lama_lembur * gaji_lembur_perjam)
gaji_bersih = gaji_kotor - potongan
print(gaji_bersih)