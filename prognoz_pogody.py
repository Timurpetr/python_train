def process(input_string: str) -> str:
    l = 0
    m = 0
    n = 0
    int_string = [int(x) for x in input_string.split()]
    for x in int_string:
        if x > 0:
            l += 1
        if x == 0:
            m += 1
        if x < 0:
            n += 1
    return f"выше нуля: {l}, ниже нуля: {n}, равна нулю:{m}"
input_string = input()
output_string = process(input_string)
print(output_string)