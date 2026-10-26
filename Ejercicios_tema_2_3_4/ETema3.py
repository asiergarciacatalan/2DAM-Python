#Ejercicio1
bycicles=["trek","cannondale","redline","specialized"]
print(bycicles[0])
print(bycicles[0].title())
print(bycicles[-1])
print(bycicles[1])
print(bycicles[3])



#Ejercicio2
guest_list=["Ada Lovelace","Grace Hopper","Alan Turing"]
print(f"Hola {guest_list[0]}! Te invito a cenar en mi casa.")
print(f"Hola {guest_list[1]}! Te invito a cenar en mi casa.")
print(f"Hola {guest_list[2]}! Te invito a cenar en mi casa.")

#Ejercicio3
favourite_transportation=["Coche","Moto","Bicicleta"]
frase=f"Mi medio de transporte favorito es {favourite_transportation[0].title()}."
print(frase)

frase2=f"Mi medio de transporte favorito es {favourite_transportation[-2].title()}."
print(frase2)

frase3=f"Mi medio de transporte favorito es {favourite_transportation[-1].title()}."
print(frase3)



#Ejercicio4

guest_list=["Ada Lovelace","Grace Hopper","Alan Turing"]
print(guest_list[0])
guest_list[0]="Guido van Rossum"
print(f"Hola {guest_list[0]}! Te invito a cenar en mi casa.")



#Ejercicio5
guest_list=["Ada Lovelace","Grace Hopper","Alan Turing"]
print(f"hola {guest_list}, tengo una mesa mas grande, asi que puedo invitar a mas personas.")
guest_list.insert(0,"Guido van Rossum")
guest_list.insert(1,"Linus Torvalds")
guest_list.append("Dennis Ritchie")
print(guest_list)


#Ejercicio6
guest_list=["Ada Lovelace","Grace Hopper","Alan Turing"]
print(len(guest_list))
guest_list.pop(2)
guest_list.pop(1)
print(len(guest_list))
print(f"Hola {guest_list}! Te invito a cenar en mi casa.")



#Ejercicio7
places=["Paris","New York","Tokyo","London","Barcelona"]
print(places.sort())
print(places.reverse())
print(places.sort(reverse=True))
print(len(places))




#Ejercicio8

lista=[1,2,4]
print(lista[-1])


#ejercicio9
productos=["Camiseta","Pantalon","Zapatos","Sombrero"]
productos.append("Gafas")
productos.insert(1,"Cinturon")
too_expensive=["drone"]
productos.extend(too_expensive)
productos.remove(too_expensive[0])
print(f"producto removido: {too_expensive[0]}")
del productos[0]
print(len(productos.sort()))


#ejercicio10
