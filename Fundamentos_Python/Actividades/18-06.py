contador = 1
def filtrar(letra):


archivo_logico = open("agenda.txt")
while(True):
    linea = archivo_logico.readline()
# print(linea)
    for linea in archivo_logico:
        linea.rstrip
        print(linea.find(letra))
    if not linea:
        break
archivo_logico.close()
# si sale -1 es que no esta en esa linea. si lo encuentra arroa el numero
print("Listado de beneficiarios: ")


while (True):
    print("Menu principal")
    print("1. Ver listado")
    print("2. Ver listado filtrado")
    print("3. Agregar beneficiario")
    print("4. Buscar beneficiario")
    print("5. Borrar beneficiario")
    opcion = int(input("6. Salir "))

if (opcion == 3):
beneficiario = input("Digite la información del beneficiario a agregar: ")
cedula = input()
telefono = input()
archivo_logico_sa = open("agenda.txt", 'a')
linea = beneficiario + '\n' + cedula + '\n' + telefono + '\n'
archivo_logico_sa.write(linea)
archivo_logico_sa.close()
print("El beneficiario ha sido agregado")

if (opcion == 1):
print("Listado de beneficiarios")
archivo_logico = open("agenda.txt", 'r')
for linea in archivo_logico:
linea.rstrip
print(linea)
# FILTRAR LETRA
if (opcion == 2):
letra = input("Digite la letra por la que empiezan los beneficiarios: ")
archivo_logico = open("agenda.txt", 'r+')
print("Listado filtrado de beneficiarios: ")
for linea in archivo_logico:
linea = linea.rstrip()
if linea.find(str(letra)) != -1:
print(linea)
data = archivo_logico.readlines()[contador-1]
print(data)
contador = contador+1


# FILTRAR

if (opcion == 4):
nombre = str(input("Digite el nombre y apellido del beneficiario a buscar"))
# buscar(nombre)
archivo_logico = open("agenda.txt", 'r+')
for linea in archivo_logico:
linea = linea.rstrip()
if (linea == nombre):
print(linea)
data = archivo_logico.readlines()[contador-1]
print(data)
contador = contador+1
archivo_logico.close

if (opcion == 5):
cedula = print(input("Digite la cedula del beneficiario a borrar"))
# borrar(cedula)
archivo_logico = open("agenda.txt", "a")
# for linea in archivo_logico:
# linea= linea.rstrip()
# if (linea == cedula):
# linea= ' '+ '\n'
# print("El usuario ha sido eliminado del listado")
# contador=contador+1
# archivo_logico.close
##
directory = archivo_logico.readlines()
archivo_logico.close()
directory = dict([tuple(line.split(',')) for line in directory])
if linea in directory:
del directory[linea]
archivo_logico = open(archivo_logico, 'w')
for name, telf in directory.items():
archivo_logico.write(name + ',' + telf)
archivo_logico.close()
print('¡El cliente se ha borrado!\n')


if (opcion == 6):
print("Hasta pronto")
break
