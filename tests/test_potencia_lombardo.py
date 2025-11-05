#tests/test_potencia.py

from funciones.potencia_lombardo import potencia
def test_potencia():
 assert potencia(2, 3) == 8
 assert potencia(5, 0)