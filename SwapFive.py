import math


def generate_current():
    x = 0
    while True:
        yield x
        x += 1


def move_last_to_first(x):
    last_digit = x % 10
    remaining = x // 10
    if remaining == 0:
        return last_digit
    count_digits = int(math.log10(remaining)) + 1
    new_x = last_digit * (10**count_digits) + remaining
    return new_x


def find_target_number(digit):
    for x in generate_current():
        if x > digit and x % 10 == digit:
            new_x = move_last_to_first(x)
            if x * digit == new_x:
                return x


k = int(input())
x = find_target_number(k)
print(move_last_to_first(x))


# To-Do: Решено на 70 процентов, вернусь когда-нибудь дорешать
