# task 1: MetaClass
class CustomMeta(type):
    def __new__(cls, name, bases, classdict: dict):
        new_classdict = {}
        for key, value in classdict.items():
            if key[0:2] != "__" and key[-1:-3] != "__":
                key = f"custom_{key}"
            new_classdict[key] = value

        new_classdict["__setattr__"] = cls.__setattr__
        return super().__new__(cls, name, bases, new_classdict)

    def __setattr__(cls, name: str, value):
        cls.__dict__[f"custom_{name}"] = value


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, _val=99):
        self.val = _val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"


# if __name__ == "__main__":
#     inst = CustomClass()
#     print("\n", inst.__dict__)
    # print(f"\n{CustomClass.__dict__ = }")
    # inst.custom_x == 50
    # inst.custom_val == 99
    # inst.custom_line() == 100
    # CustomClass.custom_x == 50
    # str(inst) == "Custom_by_metaclass"

    # print(CustomClass.__dict__)

    # inst.dynamic = "added later"
    # inst.custom_dynamic == "added later"
    # inst.dynamic  # ошибка

    # inst.x  # ошибка
    # inst.val  # ошибка
    # inst.line() # ошибка
    # inst.yyy  # ошибка
    # CustomClass.x  # ошибка
