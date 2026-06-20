import random
import keyboard
import sys

RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
CYAN = "\033[36m"

GALLOWS = [
    ["  ____", " |    |", " |", " |", " |", " |", " __|__"], # 0 ошибок
    ["  ____", " |    |", " |    O", " |", " |", " |", " __|__"], # 1 ошибка
    ["  ____", " |    |", " |    O", " |    |", " |", " |", " __|__"], # 2 ошибки
    ["  ____", " |    |", " |    O", " |   /|", " |", " |", " __|__"], # 3 ошибки
    ["  ____", " |    |", " |    O", " |   /|\\", " |", " |", " __|__"], # 4 ошибки
    ["  ____", " |    |", " |    O", " |   /|\\", " |   /", " |", " __|__"], # 5 ошибок
    ["  ____", " |    |", " |    O", " |   /|\\", " |   / \\", " |", " __|__"]  # 6 ошибок
]


words = [
    "яблоко", "компьютер", "программа", "виселица", "солнце", "звезда",
    "облако", "тетрадь", "карандаш", "линейка", "учитель", "ученик",
    "дружба", "сестра", "собака", "дерево", "цветок", "дорога", "страна"
]


def print_rules():
    print(f"{BOLD}{GREEN}Добро пожаловать в игру 'Виселица'!{RESET}")
    print("Правила игры:")
    print("- Компьютер загадывает слово.")
    print("- Вы должны угадать это слово по буквам.")
    print(f"- Каждая ошибка приближает вас к виселице.{RESET}")
    print(f"- Всего допускается {BOLD}{RED}6 ошибок{RESET}.")
    print(f"- Чтобы начать новую игру, введите {CYAN}'n или т'{RESET}.")
    print(f"- Чтобы выйти из игры, введите {CYAN}'q илм й'{RESET}.")

def print_gallows(errors):
    for line in GALLOWS[errors]:
        print(line)


def get_display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_game(word):
    guessed_letters = []
    errors = 0
    max_errors = 6

    for letter in word:
        if letter not in guessed_letters:
            guessed_letters.append(letter)
        if letter not in word:
            errors += 1
            print_gallows(errors)
        if errors >= max_errors:
            print_gallows(errors)
        if letter in word:




def main():
    print_rules()

    while True:
        if keyboard.is_pressed('q'):
            print(f"{RED}Выход из программы...{RESET}")
            sys.exit()

        if keyboard.is_pressed('n'):
            word = random.choice(words)
            print(f"\n{GREEN}Игра началась!{RESET}")
            print(f"Загадано слово из {len(word)} букв.")
            print(f"{BOLD}Подсказка (для теста): {word}{RESET}")



            print(f"\nИгра окончена. Нажми {CYAN}'n'{RESET} снова или {CYAN}'q'{RESET} для выхода.")

            while keyboard.is_pressed('n'):
                pass


if __name__ == "__main__":
    main()