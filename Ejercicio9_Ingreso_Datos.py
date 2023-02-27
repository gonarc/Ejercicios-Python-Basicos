"""
Pedir números al usuario indefinidamente hasta que ingrese 111

"""
print("") #Salto de linea
print("Ingrese los datos que quiera, si quieres parar ingese '111'")
print("") #Salto de linea
numero=int(input("Ingrese un número: "))
while not numero == 111:
    print("") #Salto de linea
    numero=int(input("Ingrese un número: "))
    
print("FINALIZADO")    