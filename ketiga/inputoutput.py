# Input output file

# w = write mode / mode menulis dan menghapus file lama, 
#     jika tidak ada maka akan dibuat file baru open('data.txt', 'w')
# r = read mode / mode membaca file 
# a = append mode / mode menambahkan data ke file
# r+ = read and write mode / mode membaca dan menulis file


# Membuat file txt
file = open('data.txt', 'w')

file.write("ini adalah data pertama\n")
file.write("ini adalah data kedua\n")
file.write("ini adalah data ketiga\n")
file.write("ini adalah data keempat\n")

file.close()


# Membaca file txt

file2 = open('data.txt', 'r')

print(file2.read())

# Appending mode

file3 = open('data.txt', 'a')

file3.write("Baris ini dibuat dengan menggunakan mode append")

file3.close()