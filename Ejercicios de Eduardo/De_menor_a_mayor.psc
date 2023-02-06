Algoritmo De_menor_a_mayor
	Escribir "Algoritmo para ordenar dos numeros de menor a mayor"
	Escribir "Ingrese el primer numero : "  
	Leer a
	Escribir "Ingrese el segundo numero : "
	Leer b
	Si a = b Entonces
		Escribir "Los numeros son iguales : " a " == " b
	SiNo
		si a < b Entonces
			Escribir "El orden seria el siguiente : " a " == " b
		SiNo
			Escribir "El orden seria el siguiente : " b " == " a
		Fin Si
	Fin Si
	
FinAlgoritmo
