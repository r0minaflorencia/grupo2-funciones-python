# tests/test_sumar.py
from funciones.sumar_avalos import sumar_avalos

def test_sumar():
    assert sumar_avalos(3, 5) == 8
    assert sumar_avalos(-2, 2) == 0
