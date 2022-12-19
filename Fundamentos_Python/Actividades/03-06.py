'''
def suma(num1, num2):
    return(num1 + num2)


def resta(num1, num2):
    return (num1 - num2)


def mult(num1, num2):
    return(num1 * num2)


def div(num1, num2):
    return(num1 / num2)


sigue = True
while (sigue):
    num1 = int(input("Ingresa un numero:\t"))
    num2 = int(input("Ingresa un numero:\t"))
    op = int(input("Ingrese que operación quieres hacer\n 1 = Suma \n 2 = Resta\n 3 = multiplicación \n 4 = Division\n 5 = Salir\n"))

    if op == 1:
        print("La suma es:\t", suma(num1, num2))
        sigue = True
    elif op == 2:
        print("La resta es:\t", suma(num1, num2))
        sigue = True
    elif op == 3:
        print("La multiplicación es:\t", suma(num1, num2))
        sigue = True
    elif op == 4:
        print("La división es:\t", suma(num1, num2))
        sigue = True
    elif op == 5:
        print("Hasta la próxima")
        sigue = False
    else:
        print("Numero No Valido, ingrese otro que esté en el menú")
        sigue = True
---------------------------------------------------------------------------
'''
def llenarLista(n):
    vecto = []
    for x in range(n):
        val=int(input("Num a guardar"))
        vecto.append(val)
    return vecto

def mayMen(lis):
    may=lis[0]
    men=lis[1]
    for i in range(1,len(lis)):
        if(lis[i]>may):
            may=lis[i]
        elif(lis[i]<men):
            men=lis[i]
    return [may,men]
    
    
n=int(input("Cuantos valores tendrá la lista?"))
vecto = llenarLista(n)

rta = mayMen(vecto)

print("El número mayor es: {}".format(str(rta[0])))
print("El número menor es: {}".format(str(rta[1])))