def validarMenu(mensaje, valorminimo, valormaximo):
    try:
        dato = int(input(mensaje))
        if dato < valorminimo or dato > valormaximo:
            return None
        else:
            return dato
    except Exception:
        return None
    
    
def validarEntero(mensaje):
   try:
       if isinstance(mensaje, str):
           texto = mensaje.strip()
           if texto == "":
               return None
           if texto.lstrip("-").isdigit():
               return int(texto)
           return int(input(mensaje))
       return int(mensaje)
   except Exception:
       return None
   

def validarNombre(nombre):
   if nombre.strip()== "":
       print("CAMPO VACIO")
       return False
   else:
       return True

