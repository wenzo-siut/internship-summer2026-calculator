from add import add

def multiply_by_add(a, b):
    result = 0

    for _ in range(abs(b)):
        result = add(result, a)

    if b < 0:
        result = -result

    return result