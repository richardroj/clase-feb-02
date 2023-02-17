
print ("Algoritmo para determinar el salario de los trabajadores")

Bs = 30000
Bs = int(Bs)
for n in range(3):
    nombre = input("Ingrese el nombre del trabajador :")
    horas = input("Cuantas horas a trabajado "+nombre+" esta semana :")
    horas = int(horas)
    salario = horas*Bs
    print("EL salario de esta semana de "+nombre+" seria de "+str(salario)+".Bs")                        



