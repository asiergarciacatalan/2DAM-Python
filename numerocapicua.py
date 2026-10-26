lista=[1,2,4,3,2,1]
for i in range(len(lista)):
    if lista[i]==lista[len(lista)-1-i]:
        continue
    else:
        print("No es capicua")
        break
else:
    print("Es capicua")
i=0
j=len(lista)-1
espalitrono=True
while(i<j and !espalitrono){
    if(lista[i]!=lista[j])
        espalitrono=False

    i+=1
    j-=1
}
print(espalitrono)