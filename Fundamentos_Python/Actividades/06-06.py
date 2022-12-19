'''
list = ["Azul", "Rojo", "Cafe", "Verde"]
print("Crear Lista \n", list, "\n")

list[1] = "Blanco"
print(list[1])

print("Funcion Index  ", list.index("Cafe"))
print("Funcion Len -- Tamaño de lista  ", len(list), "\n")

list.pop(2)
print("Funcion Pop \n", list, "\n")

if("Rojo" in list):
    list.remove("Rojo")
    print("Funcion Remove \n", list, "\n")

list.clear()
print("Funcion clear \n", list, "\n")

# ---> si el indice está fuera de rango, inserta al final
list.insert(2, "Violeta")
print("Funcion Insert in position \n", list, "\n")

list.append("Amarillo")
print("Funcion Append \n", list, "\n")
'''

def llenar_lista():
    lista1 = []
    tamaño = int(input("Cuantos elementos quiere cargar\t"))
    for x in range(tamaño):
        valor = input(str("Ingrese un animal terrestre\t"))
        lista1.append(valor)
    return lista1


animalesTerrestres = llenar_lista()
print(animalesTerrestres)
ciclemos = True
while(ciclemos):
    print("1. Agregar elemento")
    print("2. Eliminar elemento")
    print("3. Ingresar elemento")
    print("4. Vaciar lista")
    print("5. Salir")
    opcion = int(input("Ingrese opcion deseada:\t"))
    if(opcion == 1):
        animal = input(str("Ingrese un animal terreste\t"))
        animalesTerrestres.append(animal)
        print(animalesTerrestres)
    elif(opcion == 2):
        animal = input(str("Que animal quiere eliminar?\t"))
        animalesTerrestres.remove(animal)
        print(animalesTerrestres)
    elif(opcion == 3):
        animal = input(str("Que animal quiere insertar\t"))
        n = int(input("En que posición quiere ingresarlo \t"))
        animalesTerrestres.insert(n, animal)
        print(animalesTerrestres)
    elif(opcion == 4):
        animalesTerrestres.clear()
        print(animalesTerrestres)
    elif(opcion == 5):
        ciclemos = False
    else:
        print("Error número no existe en el menú, ingrese otro")
