from subtract import subtract


def divide_by_subtract(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    quotient = 0
    remainder = abs(a)
    divisor = abs(b)

    while remainder >= divisor:
        remainder = subtract(remainder, divisor)
        quotient += 1

    if (a < 0) != (b < 0):
        quotient = -quotient

    return quotient