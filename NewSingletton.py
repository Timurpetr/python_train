# class SingletonFive:
#     _instance = None
#     _count = 0
#
#     def __new__(cls, *args, **kwargs):
#         if cls._count < 5:
#             new_obj = super().__new__(cls)
#             cls._count += 1
#             if cls._count == 5:
#                 cls._instance = new_obj
#             return new_obj
#         else:
#             return cls._instance
#
#     def __init__(self, n):
#         self.n = n
#
#
# objs = [SingletonFive(str(n)) for n in range(10)]
# print([obj.n for obj in objs])


TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


# здесь объявляйте класс Dialog
class Dialog:
    def __new__(cls, *args, **kwargs):
        if TYPE_OS == 1:
            target_class = super().__new__(DialogWindows)
        elif TYPE_OS == 2:
            target_class = super().__new__(DialogLinux)
        else:
            raise None
        target_class.name = args[0]
        return target_class


dlg = Dialog("asdadsasd")
print(dlg)
