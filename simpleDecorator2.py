def info(func):
    def wrapper():
        print("-" * 30)
        func()
        print("-" * 30)
    return wrapper

@info
def judul():
    print("Mobile Legends BANG - BANG")
    
judul()