"""
Sacar el porcentaje de un numero que ingrese el usuario.
*Pedir un número al usuario y sacarle el porcentaje que el usuario pida.
"""
print("")
numero1=int(input("Ingrese un número: "))
numero2=int(input("Ingrese el porcentaje que desea sacar del número: "))

resultado= numero1*numero2/100
print(f"{int(resultado)} es el {numero2}% de {numero1}.")  