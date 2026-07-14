class SingletonFive:
    _count = 0
    _fifth = None

    def __new__(cls, *args, **kwargs):
        if cls._count < 5:
            instance = super().__new__(cls)
            cls._count += 1
            if cls._count == 5:
                cls._fifth = instance
            return instance
        else:
            return cls._fifth

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]
print([obj.name for obj in objs])
