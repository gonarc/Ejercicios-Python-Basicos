"""
Escribir un programa que muestre los cuadrados(numeros multiplicados por si mismos) de los primeros 60 numeros naturales.
Resolerlo con ciclo for y while por separado.
"""
contador = 0
for contador in range(0,61):
    numeroElevado = contador**2
    print(f"El cuadrado de {contador} es {numeroElevado}")
