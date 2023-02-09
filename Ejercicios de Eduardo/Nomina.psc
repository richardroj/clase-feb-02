Algoritmo Nomina
	s = 30000
	Para n<-1 Hasta 3 Con Paso 1 Hacer
		Segun n Hacer
			1:
				Escribir "Ingrese el nombre del primer trabajador "
				leer a
			2:
				Escribir "Ingrese el nombre del segundo trabajador "
				leer a
			3:
				Escribir "Ingrese el nombre del tercero trabajador "
				leer a
			De Otro Modo:
				Escribir "No hay datos disponibles"
		Fin Segun
		p = s*h
		Escribir "Cuantas horas a trabajado " a " esta semana"
		leer h
		p = s*h
		Escribir "El salario de esta semana de " a " seria de " p "Bs"
	Fin Para
FinAlgoritmo
