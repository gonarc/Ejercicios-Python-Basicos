"""
Mostrar todas las tablas de multiplicar del 1 al 10 con sus respectivos titulos

"""
"""
numeroTitulo = 0
numeroTabla = 0

for numeroTitulo in range(1, 11):
    print("##################")  # Salto del linea
    print("")  # Salto del linea
    print(f"TABLA DEL {numeroTitulo}: ")
    print("")  # Salto del linea
    for numeroTabla in range(1, 11):
     resultado = numeroTabla * numeroTitulo
     print(f"{numeroTitulo} x {numeroTabla} = {resultado}")

"""
print("")  # Salto de linea

resultado = 0
numero = int(
    input("Ingrese el número de la tabla de multiplicación que desea ver: "))
contador = 0
print("")  # Salto del linea

print(f"--- TABLA DEL {numero} ---")

print("")  # Salto del linea

for contador in range(1, 11):
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")

print("")  # Salto del linea

   
