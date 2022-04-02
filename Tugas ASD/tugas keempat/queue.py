stack = []
def menu():
    while True :
        print('Menu Pilihan QUEUE'.center(34,' '))
        print(' ','='*29)
        empty()
        print(' ','='*29)
        print("[\t1. Enqueue Data\t\t]")
        print("[\t2. Dequeue Data\t\t]")
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
            empty()
            keluar = input('Press Enter : ')
            if keluar == ' ':
                break
            else :
                break
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
        print("Total Data\t:", len(stack))
        print("Data Terakhir\t:", stack[-1])
            
# Clear / menghapus semua data stack
def clear():
    while True :
        lanjut = input("Ingin menghapus semua Data? <Y/N> :").upper()
        if lanjut == "Y":
            stack.clear()
            break
        else :
            break
        
menu()

