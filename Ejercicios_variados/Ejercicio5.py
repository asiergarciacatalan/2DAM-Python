Lista_original = [1, 2, 3, 4, 5,65,98,45,75,23,12,45,78,90,34,56,78,90]
imput = int(input("Introduce un número: "))
imput2 = int(input("Introduce la posición del número: "))
Lista_original.insert(imput2,imput)
Lista_original.pop()
print(Lista_original)
