# tests/test_numeropar_martinez.py
from funciones.funcionesnumeropar_martinez import es_par

def test_es_par():
    assert es_par(4) is True
    assert es_par(7) is False
