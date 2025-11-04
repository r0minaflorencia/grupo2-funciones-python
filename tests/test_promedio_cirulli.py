# tests/test_promedio_cirulli.py

from funciones.promedio_cirulli import promedio_cirulli

def test_promedio_normal():
    assert promedio_cirulli([2, 4, 6]) == 4

def test_promedio_vacio():
    assert promedio_cirulli([]) is None

def test_promedio_un_elemento():
    assert promedio_cirulli([5]) == 5

def test_promedio_flotantes():
    assert promedio_cirulli([1.5, 2.5]) == 2.0
