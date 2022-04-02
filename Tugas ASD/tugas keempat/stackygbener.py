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
        print("[\t4. Keluar \t\t]")
        print(' ','='*29)
        pilihan = int(input('Choose Number : '))
        if pilihan == 1 :
            push()
        elif pilihan == 2 :
            pop()
        elif pilihan == 3 :
            clear()
        else :
            pass

def push():
    while True:
        if stack == stack_awal:
            print('\n')
            print('Full!'.center(34,' '))
            print('\n')
            out = input('Press ENTER untuk keluar :')
            if out == out :
                return          
        else :
            stack.append(tampungan_stack[-1])
            tampungan_stack.pop()
            return

def pop():
    if stack == [] :
        print('\n')
        print('Empty!'.center(34,' '))
        print('\n')            
        out = input('Press ENTER untuk keluar :')
        if out == out :
            return  
    else :
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
            print("\tData STACK : [",i, "]")
        size()
        top()

# Total tumpukan STACK
def size():
    print("Total Data Stack :", len(stack))

# peek/top : Melihat data yang berada pada tumpukkan paling atas/terakhir
def top():
    print("Data Terakhir \t :", stack[-1])

# membersihkan semua stack dan mengulangi inputan
def clear():
    tampungan_stack.clear()
    stack_awal.clear()
    stack.clear()
    print('\n')
    print('Data has been Cleared!'.center(34,' '))
    print('\n')
    ulang = input('Press ENTER : ')
    if ulang == ulang :
        awal() 
    
    
tampungan_stack = []
stack_awal = []
stack = []
def awal():
    while True :
        inputan = input("Masukkan data STACK : ")
        stack.append(inputan)
        stack_awal.append(inputan)
        lanjut = input("Lanjut <Y/N> : ").upper()
        if lanjut == 'Y' :
            pass
        else :
            menu()
            
awal()