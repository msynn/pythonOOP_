# Stack
def menu():
    while True :
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
            return

def pop():
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

tampungan_stack = []
stack_awal = []
stack = []
while True :
    inputan = input("Masukkan data STACK : ")
    stack.append(inputan)
    stack_awal.append(inputan)
    lanjut = input("Lanjut <Y/N> : ").upper()
    if lanjut == 'Y' :
        pass
    else :
        menu()
        
