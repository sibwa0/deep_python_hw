# task 2: Descriptor
class Integer:
    def __init__(self):
        self._val = 0

    def __set_name__(self, owner, name):
        self._val = f"_{name}"

    def __get__(self, obj, objtype):
        return getattr(obj, self._val)

    def __set__(self, obj, val):
        if not isinstance(val, int):
            raise ValueError("Not Int")

        return setattr(obj, self._val, val)

    def __delete__(self, obj):
        return delattr(obj, self._val)


class String:
    def __init__(self):
        self._val = ""

    def __set_name__(self, owner, name):
        self._val = f"_{name}"

    def __get__(self, obj, objtype):
        return getattr(obj, self._val)

    def __set__(self, obj, val):
        if not isinstance(val, str):
            raise ValueError("Not Str")

        return setattr(obj, self._val, val)

    def __delete__(self, obj):
        return delattr(obj, self._val)


class PositiveInteger:
    def __init__(self):
        self._val = 0

    def __set_name__(self, owner, name):
        self._val = f"_{name}"

    def __get__(self, obj, objtype):
        return getattr(obj, self._val)

    def __set__(self, obj, val):
        if not isinstance(val, (int, float)) or val < 0:
            raise ValueError("Not PositiveInt")

        return setattr(obj, self._val, val)

    def __delete__(self, obj):
        return delattr(obj, self._val)


class Data:
    num = Integer()
    name = String()
    price = PositiveInteger()

    def __init__(self, num=0, name="", price=0):
        self.num = num
        self.name = name
        self.price = price
