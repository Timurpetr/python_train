# Напишите функцию, которая вычисляет среднее арифметическое чисел в заданном массиве.
#
# Примечание: пустые массивы должны возвращать 0.
def find_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


print(find_average([]))
