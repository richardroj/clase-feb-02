
print("### Algoritmo para ver el mayor de una cantida indefinidad de enteros ###")
print("Para dejar de ingresar numeros precione ¨t¨")
mayor = 0
mayor = int(mayor)

lista = []
a = True
while a == True:
    numero = input("Ingrese los numeros : ")
    lista.append(numero)
    if numero == "t":
        a = False
lista.pop()
for num in lista:
    num = int(num)
    if num > mayor:
        mayor = num
print(f"El mayor es : {mayor}")  
print(lista)
exit = input("precione enter para terminar el algoritmo")
        
