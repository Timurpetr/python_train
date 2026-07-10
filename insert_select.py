import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for line in data:
            idx, name, old, salary = line.split()
            self.lst_data.append({
                'id': idx,
                'name': name,
                'old': old,
                'salary': salary
            })

    def select(self, a, b):
        return self.lst_data[a : b + 1]
db = DataBase()
db.insert(lst_in)