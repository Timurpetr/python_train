from string import ascii_lowercase, digits


class CardCheck:
    @classmethod
    def check_card_number(self, number):
        number_count = number.split("-")

        if (
            len(number_count) == 4
            and len(number_count[0]) == 4
            and len(number_count[1]) == 4
            and len(number_count[2]) == 4
            and len(number_count[3]) == 4
        ):
            clean_number = number.replace("-", "")

            if all(char in digits for char in clean_number):
                return True
            else:
                return False
        else:
            return False

    @classmethod
    def check_name(self, name):
        ascii_uppercase = ascii_lowercase.upper()

        if name.isupper():
            words = name.split()

            if (
                len(words) == 2
                and all(char in ascii_uppercase for char in words[0])
                and all(char in ascii_uppercase for char in words[1])
            ):
                return True
            else:
                return False
        else:
            return False


is_number = CardCheck.check_card_number("1233-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI ASDDS")


# print(CardCheck.check_name(is_name))
print(is_number)
print(is_name)
