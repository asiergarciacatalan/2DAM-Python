lista = [5, 12, 3, 18, 20, 2, 15]
k = 15
m = 3
resultado=[]
for i in lista:
    if not(i < k and i % m == 0 ):
        resultado.append(i)
print(resultado)