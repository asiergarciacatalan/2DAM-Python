matriz=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz_transpuesta=[[], [], []]
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz_transpuesta[j].append(matriz[i][j])
print(matriz_transpuesta)