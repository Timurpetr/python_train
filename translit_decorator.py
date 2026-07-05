t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


s = input().lower()

def dash(chars):
    def translator(func):
        def wrapper(*args,**kwargs):
            sep = func(*args,**kwargs)
            replaced = ["-" if x in chars else x for x in sep]
            text_str = "".join(replaced)
            while "--" in text_str:
                text_str = text_str.replace("--", "-")
            return list(text_str)

        return wrapper
    return translator

@dash(chars="?!:;,. ")
def translate(text):
    return [t.get(x, x) for x in text.lower()]



print("".join(translate(s)))