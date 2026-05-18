"""Pruebas unitarias para el módulo calculadora."""
import pytest
from src.calculadora import sumar, dividir, porcentaje, factorial


class TestSumar:
    def test_suma_positivos(self):
        assert sumar(2, 3) == 5.0

    def test_suma_negativos(self):
        assert sumar(-2, -3) == -5.0

    def test_suma_con_cero(self):
        assert sumar(7, 0) == 7.0

    def test_suma_decimales(self):
        assert sumar(1.5, 2.5) == 4.0


class TestDividir:
    def test_division_entera(self):
        assert dividir(10, 2) == 5.0

    def test_division_decimal(self):
        assert dividir(1, 3) == 0.3333

    def test_division_por_cero(self):
        with pytest.raises(ZeroDivisionError):
            dividir(5, 0)


class TestPorcentaje:
    def test_porcentaje_normal(self):
        assert porcentaje(25, 100) == 25.0

    def test_porcentaje_total_cero(self):
        with pytest.raises(ZeroDivisionError):
            porcentaje(5, 0)

    def test_porcentaje_valor_negativo(self):
        with pytest.raises(ValueError):
            porcentaje(-5, 100)

class TestFactorial:
    def test_factorial_cinco(self):
        assert factorial(5) == 120

    def test_factorial_cero(self):
        assert factorial(0) == 1

    def test_factorial_negativo(self):
        with pytest.raises(ValueError):
            factorial(-1)