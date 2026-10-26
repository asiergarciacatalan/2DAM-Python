#Ejercicio1
pizzas=["Margarita","Cuatro Quesos","Carbonara"]
for pizza in pizzas:
    print(f"Me gusta la pizza {pizza}.")

#Ejercicio2
animales=["tigre","leon","puma"]
for animal in animales:
    print(f"el {animal} es un buen cazador")


print("todos los animales son felinos")



#Ejercicio3
#Indentation error
#Syntaxerror
#ninguno
#indentationerror







#Ejercicio4

numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for numero in range(numbers(1,5)):
    print(numero)


for numeroimpar in range(1,21,2):
    print(numeroimpar)



multiplos=list(range((3,31,3)))
for i in multiplos:
    print(i)


#Ejercicio5

lista=[]
for i in range(1,11):
    lista.append(i**3)

print(lista)

cubos2 = [n ** 3 for n in range(1, 11)]
print(cubos2)


print(lista==cubos2)




#Ejercicio6
numeros=list(range(1,1_000_000))
print(min(numeros))
print(max(numeros))
print(sum(numeros))


cuadrados=[n**2 for n in range(1,11)]
print(cuadrados)
print(min(cuadrados))
print(max(cuadrados))
print(sum(cuadrados))


#Ejercicio7
players=["asier","pirry","machaco","oke","adam"]
print(players[0:2])
print(players[1:3])
print(players[2:4])


#Ejercicio8
players=["asier","pirry","machaco","oke","adam"]
for player in players:
    print(player.title())


scores=[6343,3552,7392,2759,3536,6743] 
for score in scores:
    print(score.sort(scores[0:3]))   




#Ejercicio9
pizzas=["Margarita","Cuatro Quesos","Carbonara"]
pizza_friend=pizzas[:]
pizza_friend.append("Hawaiana")
pizza.append("Barbacoa")


for pizza in pizzas:
    print(pizza)

for pizza in pizza_friend:
    print( pizza)




#Ejercicio10
tupla=("azul","rojo","verde","amarillo")
for color in tupla:
    print(color)



    