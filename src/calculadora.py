def sumar(a: float, b: float) -> float:
    """Suma dos números."""
    return a + b


def restar(a: float, b: float) -> float:
    """Resta b de a."""
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Multiplica dos números."""
    return a * b


def dividir(a: float, b: float) -> float:
    """
    Divide a entre b.
    Lanza ZeroDivisionError si b es cero.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return round(a / b, 4)


def porcentaje(valor: float, total: float) -> float:
    """
    Calcula qué porcentaje representa valor del total.
    Lanza ZeroDivisionError si total es cero.
    Lanza ValueError si algún argumento es negativo.
    """
    if valor < 0 or total < 0:
        raise ValueError("Los valores no pueden ser negativos")
    if total == 0:
        raise ZeroDivisionError("El total no puede ser cero")
    return round((valor / total) * 100, 2)


def factorial(n: int) -> int:
    """
    Calcula el factorial de n.
    Lanza ValueError si n es negativo.
    """
    if n < 0:
        raise ValueError("El factorial no está definido para negativos")
    if n == 0:
        return 1
    return n * factorial(n - 1)
