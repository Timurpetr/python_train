def strip_comments(strng, markers):
    words = strng.split()
    for index, x in enumerate(words):
        if x in markers:
            words = words[:index]
            break

    clean_strng = " ".join(words)
    return clean_strng

result = strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!'])
expected = 'apples, pears\ngrapes\nbananas'

print("Результат:")
print(repr(result))
print("Ожидалось:")
print(repr(expected))