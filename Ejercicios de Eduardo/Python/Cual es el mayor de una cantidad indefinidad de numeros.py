
print("### Algoritmo para ver el mayor y el menor de ### \n  ### una cantida indefinidad de enteros ###")
print("Para dejar de ingresar numeros precione ¨t¨\n")
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
menor = lista[0]
menor = int(menor)
for num in lista:
    num = int(num)
    if num > mayor:
        mayor = num
for nam in lista:
    nam = int(nam)
    if nam < menor:
        menor = nam

print(f"El menor es : {menor}")        
print(f"El mayor es : {mayor}")  
print(lista)
exit = input("precione enter para terminar el algoritmo : ")
        
