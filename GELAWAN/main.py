# Array
A = [True,True,True,True,False,False,False,False]
B = [True,True,False,False,True,True,False,False]
C = [True,False,True,False,True,False,True,False]
print('--- Input ---')
print(A)
print(B)
print(C)
print('--- --- --- ---')
# P = C => B
P = []
for i in range(len(C) and len(B)):
    if C[i] == True and B[i] == False:
        P.append(False)
    else :
        P.append(True)
print("--- P ---")
print(P)

# Negasi A
negasi_A = []
print('--- Negasi A ---')
for i in range(len(A)):
    negasi_A.append(not A[i])
print(negasi_A)
print('---------------')

# P ^ negasi_A
p_konjungsi_negasi_A = []
for i in range(len(P) and len(negasi_A)):
    p_konjungsi_negasi_A.append(P[i] and negasi_A[i])
print('--- P ^ negasi_A ---')
print(p_konjungsi_negasi_A)

# Q = P <-> (P ^ negasi_A)
Q = []
for i in range(len(P) and len(p_konjungsi_negasi_A)):
    if P[i] == True and p_konjungsi_negasi_A[i] == True:
        Q.append(True)
    elif P[i] == False and p_konjungsi_negasi_A[i] == False:
        Q.append(True)
    else :
        Q.append(False)
print('--- Q ---')
print(Q)
