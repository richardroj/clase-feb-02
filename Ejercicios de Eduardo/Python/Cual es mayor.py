print ("Algoritmo que determina el mayor y el menor de 3 numeros")
num1 = int(input("Ingrese el primer numero :"))
num2 = int(input("Ingrese el primer segundo :"))
num3 = int(input("Ingrese el primer tercero :"))

if num1 != num2 and num1 != num3 and num2 != num3:
    if num1 > num2 and num1 and num3:
        print ("El mayor es : "+str(num1))
    elif num2 > num1 and num2 > num3:
            print ("El mayor es : "+str(num2))
    elif num3 > num1 and num3 > num2:
                print ("El mayor es : "+str(num3))                
else:
      print("Los numeros no pueden ser iguales")
if num1 != num2 and num1 != num3 and num2 != num3:
    if num1 < num2 and num1 and num3:
     print ("El menor es : "+str(num1))
    elif num2 < num1 and num2 < num3:
            print ("El menor es : "+str(num2))
    elif num3 < num1 and num3 < num2:
                print ("El menor es : "+str(num3))       
    else:
      print("Los numeros no pueden ser iguales")





