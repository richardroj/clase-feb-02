Algoritmo Numero_mayor_y_menor
	Escribir "Algoritmo que determina cual es el mayor y el menor de 3 numeros"
	Escribir "Por favor no ingrese numeros iguales"
	Escribir 'ingrese el primer numero :'
	Leer a
	Escribir 'ingrese el segundo numer :'
	Leer b
	Escribir 'ingrese el tercero numero :'
	Leer c
	Si a<>b Y a<>c Y c<>b Entonces
		Si a>b Entonces
			Si a>c Entonces
				Escribir 'EL numero mayor es : ',a
			SiNo
				Escribir 'El numero mayor es : ',c
			FinSi
		SiNo
			Si b>c Entonces
				Escribir 'El numero mayor es : ',b
			SiNo
				Escribir 'El numero mayor es : ',c
			FinSi
		FinSi
		Si a<b Entonces
			Si a<c Entonces
				Escribir 'EL numero menor es : ',a
			SiNo
				Escribir 'El numero menor es : ',c
			FinSi
		SiNo
			Si b<c Entonces
				Escribir 'El numero menor es : ',b
			SiNo
				Escribir 'El numero menor es : ',c
			FinSi
		FinSi
	SiNo
		Escribir 'Los numeros deven ser diferentes'
		
	FinSi
FinAlgoritmo
