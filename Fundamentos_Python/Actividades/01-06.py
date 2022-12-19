'''
n = int(input("Ingrese la cantidad de notas\t"))  
c=1
sum=0
for c in range(n):
    sum+=float(input("ingrese la nota #{} \t".format(str(c+1))))
prom=sum/n
print("El promedio obtenido es: ", prom)
--------------------------------------------------------------------------
n=20
j=100
k=2
for i in range (n,j,k):
    print(i)
print("FIN")
--------------------------------------------------------------------------
cadena = str(input())
cadena2=""
cont = len(cadena)
for i in range(cont-1,-1,-1):
    cadena2 += cadena[i]
cadena2[cont]='P'
print(cadena2)
---------------------------------------------------------------------------
for i in range (len("MUNDO")):
    print("JTJND"[i])
---------------------------------------------------------------------------
-----------
for i in range (2,51,2):
    print(i)
'''

cad = str(input())
h = cad.split()

for i in range(0, len(h)):
    a=int(h[i])
    print(a)
