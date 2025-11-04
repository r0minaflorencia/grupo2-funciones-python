# tests/test_dividir_castro.py
from funciones.dividir_castro import dividir_castro  

def test_dividir_castro(): 
    assert dividir_castro(10, 2) == 5
    assert dividir_castro(5, 0) is None