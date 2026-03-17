from validaciones import validarNombre, validarDecimal, validarEntero
from gestionjson import generar_id, cargar, guardar

ArchivoUsuarios = "usuarios.json"

def Datos(): 
	usuarios=cargar(ArchivoUsuarios)

	nombreUsuario=validarNombre("Ingrese su nombre, por favor: ")
	Email = validarEntero("Ingrese su email, por favor: ")
	contraseña=validarNombre("Ingrese contraseña, por favor: ")

	nuevo_usuario={
		"id": generar_id(usuarios),
		"nombre": nombreUsuario,
		"Email": Email,
		"contraseña": contraseña,
	}
	usuarios.append(nuevo_usuario)
	guardar(ArchivoUsuarios,usuarios)
	print("MASCOTA GUARDADA")