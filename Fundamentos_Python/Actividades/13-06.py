'''
lista = [0]*4
print(lista)
matriz = [lista]*3
print(matriz)
-----------------
matriz = []
for i in range(3):
    matriz.append([0]*4)

matriz[0][0] = 1
matriz[0][1] = 2
matriz[1][0] = 8
print(matriz)
'''


def impri_matr(matr):
    for x in range(len(matr)):
        for y in range(len(matr[x])):
            print(matr[x][y], end=' ')
        print()


matriz = []
filas = int(input("cant filas\t"))
columnas = int(input("cant columnas\t"))

for i in range(filas):
    matriz.append([0]*columnas)

for f in range(filas):
    for c in range(columnas):
        matriz[f][c] = int(input("Elementos : %d %d\t" % (f, c)))
impri_matr(matriz)
