def info(func):
    def wrapper():
        print("-" * 30)
        func()
        print("-" * 30)
    return wrapper

def judul():
    print("Mobile Legends BANG - BANG")

output = info(judul)
print(output())