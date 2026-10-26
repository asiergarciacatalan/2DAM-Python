numeros=[5,2,7,2,8,5,2,6,7]
lista_sin_repetidos=[]
for i in range(len(numeros)):
    for j in range(len(numeros)-1):
        if numeros[i]<numeros[j]:
            temp=numeros[i]
            numeros[i]=numeros[j]
            numeros[j]=temp
            
            
print(numeros)
for i in range(len(numeros)):
    if numeros[i] not in lista_sin_repetidos:
        lista_sin_repetidos.append(numeros[i])        
print("Lista sin repetidos:", lista_sin_repetidos)