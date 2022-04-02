data = [1,2,3,4]
data2 = []
print("Tampungan :", data)
print("Stack : ",data2)

data2.append(data[-1])
data.pop()
print("Tampungan :", data)
print("Stack : ",data2)

data.append(data2[-1])
data2.pop()
print("Tampungan :", data)
print("Stack : ",data2)