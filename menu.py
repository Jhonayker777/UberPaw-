#============================================================
#  🐾 UberPaws! - Menú Principal
#  Proyecto: Uber para mascotas
#  Metodología: Scrum
#  Developer: Sara Ramírez
# ============================================================

from validaciones import validarMenu
def menuPrincipal():
    while True:
        print("""
        *********************************************
                    BIENVENIDO A UBERPAWS! 🐾
            Tu servicio de transporte de mascotas
        *********************************************""")
        op = validarMenu("""    
                     INGRESA TU PERFIL:
                    1. Administrador
                    2. Usuario (Dueño de mascota)
                    3. Conductor
                            """, 1, 3)
        while op is None:
            op = validarMenu("Error, intente nuevamente: ", 1, 3)

        match op:
            case 1:
                menuAdministrador()
            case 2:
                menuUsuario()
            case 3:
                menuConductor()


#ADMINISTRADOR: ingresa con contraseña
def menuAdministrador():
    contraseña_admin = 2123
    try:
        contraseña = int(input("Ingresa la contraseña de administrador: "))
    except Exception:
        print("Contraseña invalida.")
        return

    if contraseña != contraseña_admin:
        print("Contrasena incorrecta, no puedes ingresar.")
        return

    print("*** Bienvenido, Administrador ***")

    while True:
        op = validarMenu("""
                ***********************
                ¿Que deseas gestionar?
                ***********************
                1. Gestionar Usuarios
                2. Gestionar Conductores
                3. Conductores pendientes de aprobacion
                4. Salir
                """, 1, 4)
        while op is None:
            op = validarMenu("Error, intente nuevamente: ", 1, 4)

        match op:
            case 1:
                menuAdministradorUsuarios()
            case 2:
                menuAdministradorConductores()
            case 3:
                print("(Proxima tarea: aprobar o rechazar conductores)")
            case 4:
                print("Saliendo...")
                break


def menuAdministradorUsuarios():
    while True:
        op = validarMenu("""
                        *************************
                        1. Registrar usuario
                        2. Actualizar usuario
                        3. Eliminar usuario
                        4. Listar usuarios
                        5. Buscar usuario
                        6. Salir
                        *************************
                        """, 1, 6)
        while op is None:
            op = validarMenu("Error, intente nuevamente: ", 1, 6)

        match op:
            case 1:
                print("(Proxima tarea: registrar usuario)")
            case 2:
                print("(Proxima tarea: actualizar usuario)")
            case 3:
                print("(Proxima tarea: eliminar usuario)")
            case 4:
                print("(Proxima tarea: listar usuarios)")
            case 5:
                print("(Proxima tarea: buscar usuario)")
            case 6:
                print("Saliendo...")

        if op == 6:
            break


def menuAdministradorConductores():
    while True:
        op = validarMenu("""
                        *************************
                        1. Listar conductores
                        2. Buscar conductor
                        3. Eliminar conductor
                        4. Salir
                        *************************
                        """, 1, 4)
        while op is None:
            op = validarMenu("Error, intente nuevamente: ", 1, 4)

        match op:
            case 1:
                print("(Proxima tarea: listar conductores)")
            case 2:
                print("(Proxima tarea: buscar conductor)")
            case 3:
                print("(Proxima tarea: eliminar conductor)")
            case 4:
                print("Saliendo...")

        if op == 4:
            break


#USUARIO: ingresa con correo y constraseña 
def menuUsuario():
    while True:
        op = validarMenu("""
                    **********************
                    ¿Que deseas hacer?
                    **********************
                    1. Registrarme (primera vez)
                    2. Ingresar 
                    3. Salir
                    """, 1, 3)
        while op is None:
            op = validarMenu("Error, intente nuevamente: ", 1, 3)

        match op:
            case 1:
                print("(Proxima tarea: registrar usuario)")
            case 2:
                correo = input("Ingresa tu correo electronico: ").strip()
                print(f"Bienvenido/a! (Proxima tarea: validar correo '{correo}' contra JSON)")
            case 3:
                print("Saliendo...")

        if op == 3:
            break


#CONDUCTOR: ingresa con contraseña
def menuConductor():
    while True:
        op = validarMenu("""
                    **********************
                    ¿Que deseas hacer?
                    **********************
                    1. Registrarme (primera vez)
                    2. Ingresar con mi contrasena
                    3. Salir
                    """, 1, 3)
        while op is None:
            op = validarMenu("Error, intente nuevamente: ", 1, 3)

        match op:
            case 1:
                print("(Proxima tarea: registrar conductor)")
            case 2:
                contrasena = input("Ingresa tu contrasena: ").strip()
                print(f"(Proxima tarea: validar contrasena contra JSON)")
            case 3:
                print("Saliendo...")

        if op == 3:
            break


menuPrincipal()
