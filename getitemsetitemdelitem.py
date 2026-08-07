class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def type_errors_ect(self, index):
        if index > len(self.marks) or index < 0:
            raise IndexError("Пошел нафик, такой оценки нету")
        if not isinstance(index, int):
            raise IndexError("Нужно использовать целое число")

    def __getitem__(self, index):
        if index == len(self.marks):
            raise IndexError("Пошел нафик, такой оценки нету")

        self.type_errors_ect(index)
        return self.marks[index]

    def __setitem__(self, index, value):
        self.type_errors_ect(index)
        if index == len(self.marks):
            self.marks.append(value)
        else:
            self.marks[index] = value

    def __delitem__(self, index):
        self.type_errors_ect(index)

        del self.marks[index]


s1 = Student("Сергей", [5, 5, 3, 2, 5])
del s1[0]
print(s1.marks)
