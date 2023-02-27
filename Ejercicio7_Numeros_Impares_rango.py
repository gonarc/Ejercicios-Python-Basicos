"""
Mostrar todos los numeros impares entre dos numeros que quiera el usuario

"""

numero1=int(input("Ingrese el primer número: "))
numero2=int(input("Ingrese el segundo número: "))
contador=0

for contador in range(numero1,numero2):
    if not contador%2 == 0:
        print(f"{contador} Numero impar")