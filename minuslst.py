class NewList:
    def __init__(self, initial_list=None):
        if initial_list is None:
            self._list = []
        else:
            self._list = list(initial_list)

    def get_list(self):
        return self._list

    def __repr__(self):
        return str(self._list)

    @staticmethod
    def _subtract_lists(list1, list2):
        result = list1[:]
        for item in list2:
            for i, val in enumerate(result):
                if val == item and type(val) is type(item):
                    del result[i]
                    break
        return result

    def __sub__(self, other):
        if isinstance(other, NewList):
            other_list = other.get_list()
        elif isinstance(other, (list, tuple)):
            other_list = other
        else:
            return NotImplemented

        result = self._subtract_lists(self._list, other_list)
        return NewList(result)

    def __rsub__(self, other):
        if isinstance(other, (list, tuple)):
            result = self._subtract_lists(other, self._list)
            return NewList(result)
        return NotImplemented
