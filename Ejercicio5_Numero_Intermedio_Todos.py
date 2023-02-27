"""
Mostrar en pantalla los numeros intermedios entre dos numeros dichos por el usuario

"""

numero1=int(input("ingrese el primer numero: "))
numero2=int(input("ingrese el segundo numero: "))
numeroParaMostrar= numero1
numero2ParaMostrar= numero2
print(f"Todos los numeros intermedios entre {numeroParaMostrar} y {numero2ParaMostrar} son: ")


while numero1 <= numero2: #While
    intermedio = numero1
    print(intermedio)
    numero1+=1  
    
"""
contador=0 #FOR
for contador in range(numero1,numero2+1):
    print(contador)
"""
