from validaciones import validarNombre, validarDecimal, validarEntero
from gestionjson import generar_id, cargar, guardar
ArchivoMascotas = "mascotas.json"

def Datos(): 
	mascotas=cargar(ArchivoMascotas)

	nombreMascota=validarNombre("Por favor ingrese el nombre de la mascota")
	Edad = validarEntero("Ingrese la edad de su mascota")
	tamañoMascota=validarDecimal(input("Ingrese el tamaño de la mascota en cm"))
	Transporte=validarNombre("Se requiere jaula para trasportar la mascota?")
	Comportamiento= validarNombre("Describa a su mascota (Juguetón, Cariñoso, Protector, Independiente, Tímido): ")
	Raza = validarNombre("Por favor ingrese la raza de su mascota: ")
	Vacunas = validarNombre("Que vacunas tiene su mascota")

	
	

	nueva_mascota={
		"id": generar_id(mascotas),
		"nombre": nombreMascota,
		"Edad": Edad,
		"tamaño": tamañoMascota,
		"transporte": Transporte,
		"comportamiento": Comportamiento,
		"raza": Raza,
		"vacunas": Vacunas
	}
	mascotas.append(nueva_mascota)
	guardar(ArchivoMascotas,mascotas)
	print("MASCOTA GUARDADA")