s = input()

def scan(tag):
    def insert(func):
        def wrapper(*args):
            res = func(*args)
            return  f"<{tag}>{res}</{tag}>"
        return wrapper
    return insert



@scan(tag="div")
def low_case(text):
    return text.lower()

print(low_case(s))