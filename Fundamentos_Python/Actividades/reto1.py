'''
Vamos a recibir el area en m^2
la cantidad de antenas previamente instaladas, con un rango de 36900m^2
el tipo de antenas a instalar en la zona

las antenas tienen rangos especificos dependiendo del tipo de antena
a, b, c, d, e
44600, 51800, 9600, 15300 & 13900 


salida: cuantas antenas se deben instalar por zona?
'''

area = float(input())
cant = int(input())
type = str(input())
validType = type == "a" or type == "b" or type == "c" or type == "d" or type == "e"

if type == "a":
    tipo = 44600
elif type == "b":
    tipo = 51800
elif type == "c":
    tipo = 9600
elif type == "d":
    tipo = 15300
else:
    tipo = 13900

if cant < 0 or not validType:
    salida = "error en los datos"
elif area < cant*36900:
    salida = 0
else:
    salida = (area-(cant*36900))/tipo
    if salida % 1 > 0:
        salida = int((salida//1) + 1)

print(salida)
