# task 1: MetaClass
class CustomMeta(type):
    def __new__(cls, name, bases, classdict: dict):
        new_classdict = {}
        for key, value in classdict.items():
            if key[0:2] != "__" and key[-1:-3] != "__":
                key = f"custom_{key}"
            new_classdict[key] = value

        return super().__new__(cls, name, bases, new_classdict)


class CustomClass(metaclass=CustomMeta):
    x = 50

    # def __getattribute__(self, name: str):
    #     if name[0:2] != "__" and name[-1:-3] != "__" and name[0:7] != "custom_":
    #         return super().__getattribute__(name)

    #     return super().__getattribute__(name)

    # def __getattr__(self, name: str):

    #     return super().__getattribute__(name)

    def __setattr__(self, name: str, value):
        if name[0:2] != "__" and name[-1:-3] != "__" and name[0:7] != "custom_":
            name = f"custom_{name}"

        return super().__setattr__(name, value)

    def __init__(self, _val=99):
        self.val = _val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"


if __name__ == "__main__":
    print("-----")
    inst = CustomClass(30)
    print(str(inst))

    # print("\n", inst.__dict__)
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
