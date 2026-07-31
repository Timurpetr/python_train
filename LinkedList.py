class ListObject:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = ListObject(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def __str__(self):
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes) + " -> None"


lst_in = [
    "1. Первые шаги в ООП",
    "1.1 Как правильно проходить этот курс",
    "1.2 Концепция ООП простыми словами",
    "1.3 Классы и объекты. Атрибуты классов и объектов",
    "1.4 Методы классов. Параметр self",
    "1.5 Инициализатор init и финализатор del",
    "1.6 Магический метод new. Пример паттерна Singleton",
    "1.7 Методы класса (classmethod) и статические методы (staticmethod)",
]
obj = ListObject(lst_in)
print(obj.data)
