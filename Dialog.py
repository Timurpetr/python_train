TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    def __new__(cls, *args, **kwargs):
        target_class = None
        if TYPE_OS == 1:
            target_class = super.__new__(DialogWindows)
        else:
            target_class = super.__new__(DialogLinux)
        target_class.name_class = args[0]
        return target_class


dlg = Dialog(123)
print(dlg)
