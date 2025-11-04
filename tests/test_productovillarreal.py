from funciones.villarreal import producto

def test_producto():
    assert producto(3, 4) == 12
    assert producto(-2, 5) == -10