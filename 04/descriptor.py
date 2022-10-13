# task 2: Descriptor
class Integer:
    def __set_name__(self, owner, name):
        # self.name = name
        self._val = f"_{name}"

    def __get__(self, obj, objtype):
        print(f"get {obj} cls={objtype}")

        return getattr(obj, self._val)

    def __set__(self, obj, val):
        print(f"set {val} for {obj}")
        if not isinstance(val, int):
            return setattr(obj, self._val, None)

        return setattr(obj, self._val, val)

    def __delete__(self, obj):
        print(f"delete from {obj}")

        return delattr(obj, self._val)


class String:
    def __set_name__(self, owner, name):
        # self.name = name
        self._val = f"_{name}"

    def __get__(self, obj, objtype):
        print(f"get {obj} cls={objtype}")

        return getattr(obj, self._val)

    def __set__(self, obj, val):
        print(f"set {val} for {obj}")
        if not isinstance(val, str):
            return setattr(obj, self._val, None)

        return setattr(obj, self._val, val)

    def __delete__(self, obj):
        print(f"delete from {obj}")

        return delattr(obj, self._val)


class PositiveInteger:
    def __set_name__(self, owner, name):
        # self.name = name
        self._val = f"_{name}"

    def __get__(self, obj, objtype):
        print(f"get {obj} cls={objtype}")

        return getattr(obj, self._val)

    def __set__(self, obj, val):
        print(f"set {val} for {obj}")
        if not isinstance(val, (int, float)) or val < 0:
            return setattr(obj, self._val, None)

        return setattr(obj, self._val, val)

    def __delete__(self, obj):
        print(f"delete from {obj}")

        return delattr(obj, self._val)


class Data:
    num = Integer()
    name = String()
    price = PositiveInteger()

    def __init__(self, num=None, name=None, price=None):
        self.num = num
        self.name = name
        self.price = price
