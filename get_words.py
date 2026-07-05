menu = input()

def show_menu(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        formatted_menu = "\n".join(f"{i + 1}. {v}" for i, v in enumerate(result))
        print(formatted_menu)
        return formatted_menu
    return wrapper

@show_menu
def get_menu(s):
    return list(s.split())

get_menu(menu)