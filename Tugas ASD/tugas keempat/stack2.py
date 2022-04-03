# Stack
def menu():
    while True :
        print('\n')
        print('Menu Pilihan STACK'.center(34,' '))
        print(' ','='*29)
        empty()
        print(' ','='*29)
        print("[\t1. PUSH Data\t\t]")
        print("[\t2. POP Data\t\t]")
        print("[\t3. Clear Data\t\t]")      
        print(' ','='*29)
        pilihan = input('Choose Number : ')
        if pilihan == '1' :
            push()
        elif pilihan == '2' :
            pop()
        elif pilihan == '3' :
            clear()
        else :
            pass

# PUSH berfungsi untuk memasukkan data
def push():
    while True:
        if stack == stack_awal:
            print('\n')
            print('Full!'.center(34,' '))
            print('\n')
            print('-'*34)
            print("Tekan <Y> Jika ingin menambah STACK!")
            print("Tekan <N> untuk keluar!")
            print('-'*34)
            out = input('Tekan <Y/N> :').upper()
            if out == 'Y':
                print('-'*34)
                baru = input("Masukkan Data STACK baru : ")
                if baru in stack_awal :
                    print("DATA SUDAH ADA!")
                    pass
                else :
                    stack.append(baru)
                    stack_awal.append(baru)
                    print(f'\nData {baru} Telah ditambahkan!')
            elif out == out :
                return          
        else :
            print("Tekan <Y> Jika ingin menambah STACK!")
            print("Tekan <N> untuk PUSH!")
            print("Selain itu Kembali ke menu!")
            print('-'*34)
            out = input('Choose :').upper()
            if out == 'Y':
                print('-'*34)
                baru = input("Masukkan Data STACK baru : ")
                if baru in stack_awal :
                    print("DATA SUDAH ADA!")
                    pass
                else :
                    if stack == stack_awal :
                        print('\n')
                        print('Full!'.center(34,' '))
                        print('\n')
                    else :
                        stack.append(baru)
                        stack_awal.append(baru)
                        print(f'\nData {baru} Telah ditambahkan!')
            elif out == 'N' :
                if tampungan_stack == [] :
                    print('\n')
                    print('Full!'.center(34,' '))
                    print('\n')
                else :
                    stack.append(tampungan_stack[-1])
                    tampungan_stack.pop()
                    return
            else :
                return

# POP berfungsi untuk mengeluarkan data terakhir (atas)
def pop():
    if stack == [] :
        print('\n')
        print('Empty!'.center(34,' '))
        print('\n')            
        out = input('Press ENTER untuk keluar :')
        if out == out :
            return  
    else :
        print('\n')
        print('Data berhasil di POP!'.center(34,' '))            
        tampungan_stack.append(stack[-1]) 
        stack.pop()
        return
    
# EMPTY 
def empty():
    if stack == [] :
        print('Empty!'.center(34,' '))
    else :
        print("Data STACK :".center(34,' '))
        for i in stack:
            print("Data STACK",(stack.index(i)+1),": [",i, "]")
        print("-"*34)
        size()
        top()
        print('\n')

# Total tumpukan STACK
def size():
    print("Total Data Stack :", len(stack))

# peek/top : Melihat data yang berada pada tumpukkan paling atas/terakhir
def top():
    print("Data Terakhir \t :", stack[-1])

# membersihkan semua stack dan mengulangi inputan
def clear():
    print('Data Anda Akan Terhapus'.center(34,' '))
    pilihan = input('Lanjut <Y/N> : ').upper()
    if pilihan == 'Y':
        tampungan_stack.clear()
        stack_awal.clear()
        stack.clear()     
        print('\n')
        print('Data has been Cleared!'.center(34,' '))
        print('\n')
        ulang = input('Press ENTER : ')
        if ulang == ulang :
            awal() 
    else :
        return
    
    
tampungan_stack = []
stack_awal = []
stack = []
def awal():
    print('-'*34)
    print(" PENGINPUTAN DATA STACK ".center(34,'='))
    print('-'*34)
    while True :
        inputan = input("Masukkan data STACK : ")
        if inputan in stack :
            print('DATA SUDAH ADA!')
            pass
        else :
            stack.append(inputan)
            stack_awal.append(inputan)
            lanjut = input("Lanjut <Y/N> : ").upper()
            if lanjut == 'Y' :
                pass
            else :
                menu()
                
awal()