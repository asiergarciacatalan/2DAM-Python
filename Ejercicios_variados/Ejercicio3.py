matriz=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz2=[[9, 8, 7], [6, 5, 4], [3, 2, 1]]
matriz_final=[[], [], []]
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz_final[i].append(matriz[i][j] + matriz2[i][j])
print(matriz_final)