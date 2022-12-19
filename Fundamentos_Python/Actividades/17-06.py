def dividir(num,div):
    return num/div

numero1= int(input("Digite el primer numero: "))
numero2= int(input("Digite el segundo numero: "))
try:
    res= dividir(numero1,numero2)
    print(res)
except ZeroDivisionError:
    print("Usted intenta dividir por cero")