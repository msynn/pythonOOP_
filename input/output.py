#  membaca file yang sudah ada
fread = open('data.txt')

count = 0
for line in fread:
    count += 1

print(count)



# membuat dan menulis file baru
fwrite = open('data.txt', 'w')

n = 1
for i in range(2, 50):
    n += 1
    fwrite.write(str(n) + '\n')

fwrite.close()


# file sebagai input / output
while True :
    fname = input("Nama file input : ")
    
    try :
        fread = open(fname)
        break
    except:
        print('Tidak ada file dengan nama itu, tolong cek lagi. \nNama file input : ')
        
nama = []
for line in fread:
    nama.append(line.strip())

nama = sorted(nama)

fwrite = open('output_' + fname, 'w')

for item in nama:
    fwrite.write(item + '\n')

fwrite.close()