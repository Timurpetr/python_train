# Цель этого упражнения — преобразовать строку в новую строку,
# в которой каждый символ заменяется на «(», если он встречается в исходной строке только один раз, или на «)»,
# если он встречается более одного раза. При определении того,
# является ли символ повторяющимся, регистр не учитывается.
def duplicate_encode(word):
    letter_counts = {}
    word = word.lower()
    for char in word:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1

    res = []

    for letter in word:
        if letter_counts[letter] > 1:
            res.append(")")
        else:
            res.append("(")

    return "".join(res)


print(duplicate_encode("Success"))
