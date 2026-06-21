def product_fib(_prod):
    fib_1, fib_2 = 0, 1
    if _prod == 0:
        return 0, 1, True
    while fib_1 * fib_2 != _prod:
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        if fib_1 * fib_2 == _prod:
            return fib_1, fib_2, True
        elif fib_1 * fib_2 > _prod:
            return fib_1, fib_2, False
print(product_fib(714))
print(product_fib(800))
print(product_fib(0))