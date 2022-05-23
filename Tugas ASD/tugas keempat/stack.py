stack = []
def menu():
    while True :
        print('Menu Pilihan STACK'.center(34,' '))
        print(' ','='*29)
        empty()
        print(' ','='*29)
        print("[\t1. PUSH Data\t\t]")
        print("[\t2. POP Data\t\t]")
        print("[\t3. View Data\t\t]")
        print("[\t4. Clear Data\t\t]")
        print("[\t5. Keluar \t\t]")
        print(' ','='*29)
        pilihan = int(input('Choose Number : '))
        if pilihan == 1 :
            push()
        elif pilihan == 2 :
            pop()
        elif pilihan == 3 :
            view()
        elif pilihan == 4 :
            clear()
        elif pilihan == 5 :
            break

# PUSH / MENAMBAHKAN DATA STACK
def push():
    while True :
        tambah_data = input('Masukkan Data STACK : ')
        stack.append(tambah_data)
        lanjut = input("Lanjut Push Data? <Y/N> : ").upper()
        if lanjut == "Y" :
            pass
        else :
            break

# POP / MENGHAPUS STACK
def pop():
    while True :
        if stack == [] :
            print("\n")
            print("No Empty!".center(34,' '))
            print("\n")
            break
        else :    
            stack.pop()
            break
    
# EMPTY 
def empty():
    if stack == [] :
        print('Empty!'.center(34,' '))
    else :
        print("Data STACK :".center(34,' '))
        for i in stack:
            print("\tData STACK : [",i, "]")
        size()
        top()
            
# Clear / menghapus semua data stack
def clear():
    while True :
        lanjut = input("Ingin menghapus semua Data? <Y/N> :").upper()
        if lanjut == "Y":
            stack.clear()
            break
        else :
            break

# Total tumpukan STACK
def size():
    print("Total Data Stack :", len(stack))

# peek/top : Melihat data yang berada pada tumpukkan paling atas/terakhir
def top():
    print("Data Terakhir \t :", stack[-1])
        
def view():
    while True :
        if stack == [] :
            print('-'*34)
            print('\n')
            print('Empty!'.center(34,' '))
            print('\n')
            print('-'*34)
            lanjut = input('Press ENTER : ')
            if lanjut == lanjut :
                break
        else :
            print('\n')
            print('-'*34)
            print("Data STACK :".center(34,' '))
            for i in stack:
                print("\tData STACK : [",i, "]")
            size()
            top()
            print('-'*34)
            print('\n')
            lanjut = input('Press ENTER : ')
            if lanjut == lanjut :
                break


menu()

