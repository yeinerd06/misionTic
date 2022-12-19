cont = int(input())  # numero de zonas a analizar
suma = int(0.0)
cant_a = 0
cant_b = 0
cant_c = 0
cant_d = 0
cant_e = 0
while (cont > 0):
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
    if(cant < 1 or area < cant*36900):
        salida = 0
    else:
        salida = (area-(cant*36900))/tipo
        if salida % 1 > 0:
            salida = (salida//1) + 1
    if type == "a":
        cant_a += salida
    elif type == "b":
        cant_b += salida
    elif type == "c":
        cant_c += salida
    elif type == "d":
        cant_d += salida
    else:
        cant_e += salida
    suma += salida
    cont -= 1
# Salidas
print(int(suma))
if(cant_a == 0):
    print('a 0.00%')
else:
    prin = 100/(suma/cant_a)
    prin = round(prin, 2)
    if((prin % 1)/10!=0):
        print('a {}%'.format(str(round(prin, 2))))
    else:
        print("a {}0%".format(prin))
if(cant_b == 0):
    print('b 0.00%')
else:
    prin = 100/(suma/cant_b)
    prin = round(prin, 2)
    if((prin % 1)/10!=0):
        print('b {}%'.format(str(round(prin, 2))))
    else:
        print("b {}0%".format(prin))
if(cant_c == 0):
    print('c 0.00%')
else:
    prin = 100/(suma/cant_c)
    prin = round(prin, 2)
    if((prin % 1)/10!=0):
        print('c {}%'.format(str(round(prin, 2))))
    else:
        print("c {}0%".format(prin))
if(cant_d == 0):
    print('d 0.00%')
else:
    prin = 100/(suma/cant_d)
    prin = round(prin, 2)
    if((prin % 1)/10!=0):
        print('d {}%'.format(str(round(prin, 2))))
    else:
        print("d {}0%".format(prin))
if(cant_e == 0):
    print('e 0.00%')
else:
    prin = 100/(suma/cant_e)
    prin = round(prin, 2)
    if((prin % 1)/10!=0):
        print('e {}%'.format(str(round(prin, 2))))
    else:
        print("e {}0%".format(prin))
