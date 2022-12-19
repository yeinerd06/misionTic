def entregar_medicina(sis, diast):
    cant = 0
    if(sis < 75 and diast < 55):
        cant = 7
    elif(sis > 124 and sis < 136 and diast > 79 and diast < 86):
        cant = 1
    elif(sis > 134 and sis < 156 and diast > 84 and diast < 96):
        cant = 7
    elif(sis > 154 and sis < 176 and diast > 94 and diast < 106):
        cant = 15
    elif(sis >= 175 and diast >= 105):
        cant = 30
    elif(sis >= 135 and diast <= 85):
        cant = 15
    return int(cant)


def encontrar_Menor_Mayor(vecto, listExis):
    may = 0
    men = 0
    for i in range(1, len(vecto)):
        if(vecto[i] < vecto[men]):
            men = i
        if(vecto[i] > vecto[may]):
            may = i
    if(vecto[0] == men):
        men = 0
    if(vecto[0] == may):
        may = 0
    return [may, men]


def sapararCadena(cad):
    h = cad.split()
    return [h[0], h[1], h[2]]


n = 0  # cantidad de sucursales
k = 0  # numero de diferentes tipos de medicamento
m = 0  # total de pacientes a atender
while(n < 1 or k < 1):
    l = str(input())
    n = int(l[0])
    k = int(l[2])
    m = int(l[4])

medExist = []
medRestantes = []
cant_tiposdeMed = []  # guarda la cantidad disponibles de cada tipo de medicamento
# en la pocision 0 guarda la cantidad disponible del medicamento 1

for x in range(1, n):
    valor = int(input())
    while(valor < 1):
        valor = int(input())
    medRestantes.append(valor)
    medExist.append(valor)

for k in range(0, m):
    cad = str(input())
    h = sapararCadena(cad)
    sucursal = int(h[0])
    sistolica = int(h[1])
    diastolica = int(h[2])
    medRestantes[sucursal-1] -= entregar_medicina(sistolica, diastolica)

may_men = encontrar_Menor_Mayor(medRestantes, medExist)
men = may_men[1]
may = may_men[0]

print(men+1, " ", medRestantes[men])
print(may+1, " ", medRestantes[may])

for x in range(n):
    qpw = medRestantes[x]*100
    qpw = qpw/medExist[x]
    qpw = 100-qpw
    pri = qpw, ""

    if(qpw == 0):
        pri = '0.00%'
    else:
        modulo = qpw % 1
        modulo = (modulo*10) % 1
        modulo = round(modulo, 1)

        if(modulo == 0):
            pri = ('{}0%'.format(round(qpw, 2)))
        else:
            pri = ('{}%'.format(str(round(qpw, 2))))

    print(x+1, pri)
