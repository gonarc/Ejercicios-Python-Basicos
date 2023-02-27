"""escribir un script que muestre por pantalla todos los numeros pares del 1 al 120 """
contador=0
for contador in range(1,121):
#Bucle para correr numeros del 0 al 120 como pide el ejercicio.
   if contador%2 == 0:
#Verificacion de que el resto del numero sea igual a 0 para identificar el numero par. 
    print(contador)
   """else:
       print(f"El numero {contador} es impar") 
   contador+=1
   """  
   