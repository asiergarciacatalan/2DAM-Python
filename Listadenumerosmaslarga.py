lista=[4,2,7,0,4,3,2,1]
contador=1
longitud_final=0
for i in range(1,len(lista)):
    if lista[i]<lista[i-1]:
        contador+=1
    else:
        contador=1
    if contador>longitud_final:
        longitud_final=contador


     
        

    
       
print(longitud_final)