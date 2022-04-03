from collections import deque

antrian = deque([])

def menu():
    while True :
        print('-'*34)
        print(' QUEUE '.center(34,'='))
        print('-'*34)
        if antrian == deque([]) :
            print('Antrian Kosong!'.center(34,' '))
        else :
            if len(antrian) <= 5 :
                print('Antrian Sudah Ada!')
            else :
                print("Antrian MAX!")
            size()
            print("Antrian Terakhir:",antrian[-1])
        print('-'*34)
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. View Queue")
        print("4. Exit")
        pilihan = input('Choose Number : ')
        if pilihan == '1':
            full()
        elif pilihan == '2':
            dequeue()
        elif pilihan == '3':
            view()
        elif pilihan == '4':
            break
        else :
            print('\n')
            print("Invalid Code!".center(34,' '))
            print('\n')
            press = input('Press ENTER !')
            if press == press :
                pass

def view():
    print('Antrian :')
    for i in antrian:
        print(f"-\t{antrian.index(i)+1}.\t| {i} |")

def full():
    if len(antrian) >= 5 :
        print('-'*34)
        print('Antrian FULL!')
        print('-'*34)
        press = input(' Press ENTER !')
        if press == press :
            return
    else :
        enqueue()
          
        
def enqueue():
    print("-"*34)
    print(" Menu Enqueue ".center(34,'='))
    print('- Antrian MAX 5 -'.center(34,' '))
    print("-"*34)
    while True:
        add = input("Masukkan Antrian : ")
        antrian.append(add)
        print('-'*34)
        print(f" '{add}' Telah Ditambahkan ke Antrian!")
        print('-'*34)
        press = input('Press ENTER !')
        if press == press :
            return
            
def dequeue():
    if len(antrian) == 0 :
        print('\n')
        print("Antrian Kosong!".center(34,' '))
        print('\n')
        return
    else :
        antrian.popleft()
        print("Antrian Terdepan sudah diambil!")
        press = input('Press ENTER !')
        if press == press :
            return

def size():
    print("Jumlah Antrian\t:", len(antrian))

menu()