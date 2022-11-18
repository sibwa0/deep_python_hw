import json
from json import JSONDecodeError

def word_process(key, dct):
    if key in dct:
        dct[key] += 1
    else:
        dct[key] = 1


def is_valid_income_data(json_str, required_fields, keywords, callback):
    try:
        json.loads(json_str)
    except JSONDecodeError:
        print("...Not valid json document.")
        return False

    if callback is None:
        print("...Not Callback, None")
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


def parse_json(json_str, callback=None, required_fields=None, keywords=None):
    if not is_valid_income_data(json_str, required_fields, keywords, callback):
        return False

    dct = json.loads(json_str)

    if len(dct) == 0:
        print("...Json is empty.")
        return None

    cnt_male_female = {}
    for key in required_fields:
        for value in keywords:
            # to form dct[key] in list of words 
            for div_key in dct[key].split():
                if value == div_key:
                    callback(value, cnt_male_female)

    return cnt_male_female


# generate fake data
def input_random_names_number(amount, func):
    res = func()
    for _ in range(amount):
        res += " " + func()

    return res


if __name__ == "__main__":
    json_str = '{"key1": "Word1 word2", "key2" "word2 word3"}'
    required_fields = ["key1"]
    keywords = ["word2"]

    print(parse_json(json_str, word_process, required_fields, keywords))
