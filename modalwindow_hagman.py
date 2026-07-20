import customtkinter as ctk
import random

WORDS = [
    "python",
    "java",
    "kotlin",
    "javascript",
    "ruby",
    "golang",
    "swift",
    "visualbasic",
    "perl",
    "php",
    "html",
    "css",
    "csharp",
    "cplusplus",
    "typescript",
    "scala",
    "rust",
    "dart",
    "elixir",
    "erlang",
]


class HangmanApp:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.title("Hangman Game")
        self.app.geometry("400x600")
        self.game = HangmanGame(random.choice(WORDS))
        self.create_widgets()
        self.update_ui()

    def create_widgets(self):
        self.main_frame = ctk.CTkFrame(self.app)
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)
        self.title_label = ctk.CTkLabel(
            self.main_frame, text="Виселица", font=("Arial", 28, "bold")
        )
        self.title_label.pack(pady=10)
        self.word_label = ctk.CTkLabel(
            self.main_frame, text="", font=("Arial", 34, "bold")
        )
        self.word_label.pack(pady=20)
        self.attempts_label = ctk.CTkLabel(self.main_frame, text="", font=("Arial", 16))
        self.attempts_label.pack(pady=10)
        self.result_label = ctk.CTkLabel(
            self.main_frame, text="", font=("Arial", 18, "bold")
        )
        self.result_label.pack(pady=10)

        import string

        self.letter_buttons = {}
        letters_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        letters_frame.pack(pady=10)
        for i, letter in enumerate(string.ascii_uppercase):
            btn = ctk.CTkButton(
                letters_frame,
                text=letter,
                width=40,
                height=40,
                command=lambda l=letter: self.on_letter_click(l),
            )
            row, col = divmod(i, 7)
            btn.grid(row=row, column=col, padx=2, pady=2)
            self.letter_buttons[letter] = btn

        self.reset_button = ctk.CTkButton(
            self.main_frame, text="Новая игра", command=self.reset_game
        )
        self.reset_button.pack(pady=20)

    def on_letter_click(self, letter):
        if not self.game.is_active():
            return
        if self.game.guess_letter(letter):
            self.letter_buttons[letter].configure(state="disabled")
            self.update_ui()

    def update_ui(self):
        self.word_label.configure(text=self.game.get_display_word())
        self.attempts_label.configure(
            text=f"Осталось попыток: {self.game.attempts_left}"
        )
        if self.game.is_won():
            self.result_label.configure(text="Вы выиграли!", text_color="green")
            self.disable_all_buttons()
        elif self.game.is_lost():
            self.result_label.configure(
                text=f"Вы проиграли. Слово: {self.game.word}", text_color="red"
            )
            self.disable_all_buttons()
        else:
            self.result_label.configure(text="")

    def disable_all_buttons(self):
        for btn in self.letter_buttons.values():
            btn.configure(state="disabled")

    def enable_all_buttons(self):
        for btn in self.letter_buttons.values():
            btn.configure(state="normal")

    def reset_game(self):
        self.game = HangmanGame(random.choice(WORDS))
        self.enable_all_buttons()
        self.result_label.configure(text="")
        self.update_ui()

    def run(self):
        self.app.mainloop()


class HangmanGame:
    def __init__(self, word, max_attempts=6):
        self.word = word.upper()
        self.max_attempts = self.attempts_left = max_attempts
        self.guessed_letters = set()

    def guess_letter(self, letter):
        letter = letter.upper()
        if letter in self.guessed_letters:
            return False
        self.guessed_letters.add(letter)
        if letter not in self.word:
            self.attempts_left -= 1
        return True

    def get_display_word(self):
        return " ".join(
            char if char in self.guessed_letters else "_" for char in self.word
        )

    def is_won(self):
        return all(char in self.guessed_letters for char in self.word)

    def is_lost(self):
        return self.attempts_left <= 0

    def is_active(self):
        return not self.is_won() and not self.is_lost()

    def on_letter_click(self, letter):
        if not self.game.is_active():
            return
        if self.game.guess_letter(letter):
            self.letter_buttons[letter].configure(state="disabled")
            self.update_ui()

    def update_ui(self):
        self.word_label.configure(text=self.game.get_display_word())
        self.attempts_label.configure(
            text=f"Осталось попыток: {self.game.attempts_left}"
        )
        if self.game.is_won():
            self.result_label.configure(text="🎉 Вы выиграли!", text_color="green")
            self.disable_all_buttons()
        elif self.game.is_lost():
            self.result_label.configure(
                text=f"😢 Вы проиграли. Слово: {self.game.word}", text_color="red"
            )
            self.disable_all_buttons()
        else:
            self.result_label.configure(text="")

    def disable_all_buttons(self):
        for btn in self.letter_buttons.values():
            btn.configure(state="disabled")

    def enable_all_buttons(self):
        for btn in self.letter_buttons.values():
            btn.configure(state="normal")

    def reset_game(self):
        self.game = HangmanGame(random.choice(WORDS))
        self.enable_all_buttons()
        self.result_label.configure(text="")
        self.update_ui()

    def run(self):
        self.app.mainloop()


if __name__ == "__main__":
    app = HangmanApp()
    app.run()
