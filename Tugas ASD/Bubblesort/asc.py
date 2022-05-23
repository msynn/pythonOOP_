angka = [2,6,4,78,12,34,56,89,77,54,3,5,9,10,15,25]

def mengurutkan(data):
    for i in range (len(data)-1,0,-1):
        for j in range (0,len(data)-1):
            if (data[j] > data[j+1]):
                data[j],data[j+1] = data[j+1],data[j]
        print(data)
        
        
