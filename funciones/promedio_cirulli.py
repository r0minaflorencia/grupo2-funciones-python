# funciones/promedio_cirulli.py

def promedio_cirulli(numeros):
    """Devuelve el promedio de una lista de números.
    Si la lista está vacía, devuelve None.
    """
    if not numeros:
        return None
    return sum(numeros) / len(numeros)
