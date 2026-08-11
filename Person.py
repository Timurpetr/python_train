class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job

    def _get_fields(self):
        return (self.fio, self.job, self.old, self.salary, self.year_job)

    def __iter__(self):
        return iter(self._get_fields())

    def __setitem__(self, index, value):
        attrs = ("fio", "job", "old", "salary", "year_job")
        attr_name = attrs[index]
        setattr(self, attr_name, value)

    def __getitem__(self, index):
        return self._get_fields()[index]


pers = Person("Гейтс Б.", "бизнесмен", 61, 1000000, 46)
pers[0] = "Балакирев С.М."

for v in pers:
    print(v)
