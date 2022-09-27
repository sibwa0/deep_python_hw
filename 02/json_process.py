import json


def word_process(key, dct):
    if key in dct:
        dct[key] += 1
    else:
        dct[key] = 1


def is_valid_income_data(json_str, required_fields, keywords):
    if json.loads(json_str) == ValueError:
        print("...Not valid json document.")
        return False

    tmp_dct = json.loads(json_str)
    for _, value in tmp_dct.items():
        if not isinstance(value, str):
            print(
                f"...Not valid values.\n{type(value)=}\n{tmp_dct=}\n \
                Should be: (Value type == str)"
            )
            return False

    if not isinstance(required_fields, list) or \
            not all(isinstance(x, str) for x in required_fields):
        print(
            f"...Not valid keys.\n{type(required_fields)=}\n \
            {required_fields=}\n \
            Should be: (Type == list) (Elements == str)"
        )
        return False

    if not isinstance(keywords, list) or \
            not all(isinstance(x, str) for x in keywords):
        print(
            f"...Not valid values.\n{type(keywords)=}\n{keywords=}\n \
            Should be: (Type == list) (Elements == str)"
        )
        return False

    return True


def parse_json(json_str, callback, required_fields=None, keywords=None):
    if not is_valid_income_data(json_str, required_fields, keywords):
        return False

    dct = json.loads(json_str)

    if len(dct) == 0:
        print("...Json is empty.")
        return None

    cnt_male_female = {}
    for key in required_fields:
        # if (key in dct):
        for value in keywords:
            if value in dct[key]:
                callback(value, cnt_male_female)

    return cnt_male_female


# generate fake data
def input_random_names_number(amount, func):
    res = func()
    for _ in range(amount):
        res += " " + func()

    return res
