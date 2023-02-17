print ("Algoritmo para ordenar dos numeros de menor a mayor")

num1 = input("Ingrese el primer numero :")
num2 = input("Ingrese el segundo numero :")

if num1 == num2:
    print("Los numros son iguales")
else:
    if num1 < num2:
        print("El orden seria el siquiente :" +str(num1)+" == "+str(num2))
    else:
        print("El orden seria el siquiente :" +str(num2)+" == "+str(num1))
