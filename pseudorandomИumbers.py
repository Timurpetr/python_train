# state, n, a и b
state, n, a, b = list(map(int, input().split(",")))


def xorshift32():
    global x
    # Операции сдвига и XOR
    x ^= (x << 13) & 0xFFFFFFFF  # 1. Сдвиг влево на 13, маска для 32 бит
    x ^= x >> 17  # 2. Сдвиг вправо на 17
    x ^= (x << 5) & 0xFFFFFFFF  # 3. Сдвиг влево на 5, маска для 32 бит
    return x
