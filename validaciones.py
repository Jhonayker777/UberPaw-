def validarMenu(mensaje, valorminimo, valormaximo):
    try:
        dato = int(input(mensaje))
        if dato < valorminimo or dato > valormaximo:
            return None
        else:
            return dato
    except Exception:
        return None