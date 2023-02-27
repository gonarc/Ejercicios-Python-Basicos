"""
Pedir dos numeros al usuario y hacer todas las operaciones basicas de una calculadora y motrar en pantalla.

"""
numeroUsuario=int(input("Ingrese un número: "))
operacion=(input("Ingrese la operación a realizar: "))
numero2Usuario=int(input("ingrese otro número: "))

if operacion == "+":
    print(numeroUsuario + numero2Usuario)
if operacion == "-":
    print(numeroUsuario - numero2Usuario)
if operacion == "*":
    print(numeroUsuario * numero2Usuario)
if operacion == "/":
    print(numeroUsuario / numero2Usuario)

