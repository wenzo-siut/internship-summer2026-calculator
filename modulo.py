def modulo(a, b):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be numeric")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be numeric")

    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    return a % b