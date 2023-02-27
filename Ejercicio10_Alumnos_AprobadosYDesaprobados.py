"""
ingreso de datos de 15 alumnos, y decir cuantos han aprobado cuantos han desaprobados.
"""
alumnos=int(input("Ingrese la cantidad de alumnos: "))
aprobados=0
desaprobados=0
contador=1
while contador <= alumnos:
    nota= int(input(f"Ingrese la nota del alumno {contador}: "))
    if nota > 6:
        aprobados+=1
    else:
        desaprobados+=1
    contador+=1
print(f"La cantidad de aprobados es de:{aprobados}")             
print(f"La cantidad de desaprobados es de:{desaprobados}")             