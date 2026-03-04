from python_app.palindromo import es_palindromo
from python_app.utils import suma

def test_palindromo_basico():
    assert es_palindromo("radar") is True


def test_palindromo_mayusculas():
    assert es_palindromo("Radar") is True


def test_palindromo_con_espacios():
    assert es_palindromo("anita lava la tina") is True


def test_no_palindromo():
    assert es_palindromo("python") is False


def test_cadena_vacia():
    assert es_palindromo("") is True


# =========================
# Tests para suma
# =========================

def test_suma_positivos():
    assert suma(2, 3) == 5


def test_suma_con_cero():
    assert suma(0, 5) == 5


def test_suma_negativo():
    assert suma(-2, 3) == 1