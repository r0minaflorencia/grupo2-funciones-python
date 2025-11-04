# tests/test_restar_diaz.py

from funciones.restar_diaz import restar

def test_restar_positivo():
    assert restar(10, 4) == 6

def test_restar_negativo():
    assert restar(5, 10) == -5

def test_restar_cero():
    assert restar(0, 0) == 0