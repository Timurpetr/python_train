from string import ascii_lowercase, digits


class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        self.check_name(name)
        self.name = name
        self.size = size

    def get_html(self):
        return f"<p class='login'> {self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):

        if not all(char in TextInput.CHARS_CORRECT for char in name):
            raise ValueError("некорректное поле name")
        else:
            if 3 <= len(name) <= 50:
                return True
            else:
                raise ValueError("некорректное поле name")


class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        self.check_name(name)
        self.name = name
        self.size = size

    def get_html(self):
        return (
            f"<p class='password'> {self.name}: <input type='text' size={self.size} />"
        )

    @classmethod
    def check_name(cls, name):

        if not all(char in TextInput.CHARS_CORRECT for char in name):
            raise ValueError("некорректное поле name")
        else:
            if 3 <= len(name) <= 50:
                return True
            else:
                raise ValueError("некорректное поле name")


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(
            [
                '<form action="#">',
                self.login.get_html(),
                self.password.get_html(),
                "</form>",
            ]
        )


login = FormLogin(TextInput("Логин", 10), PasswordInput("Пароль", 20))
html = login.render_template()
print(html)
