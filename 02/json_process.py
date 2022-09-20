from faker import Faker
import json
import random

fake = Faker()

# generate json_str 
n = 5

def input_random_names_number(n, func):
    res = func()
    for _ in range(random.randint(1, n)):
        res += " " + func()

    return res

my_dict = {
    'female': input_random_names_number(n, fake.last_name_female),
    'male': input_random_names_number(n, fake.last_name_male)
}


def word_process(key, dct):
    if key in dct:
        dct[key] += 1
    else:
        dct[key] = 0

def is_valid_income_data(json_str, required_fields, keywords):
    if json_str.loads == ValueError:
        print("...Not valid json document.")
        return False

    if type(required_fields) != list:
        print(f"...Not valid keys. {type(required_fields)=} (Type == list)")
        return False

    if type(keywords) != list:
        print(f"...Not valid values. {type(keywords)=} (Type == list)")
        return False

    return True


def parse_json(json_str, keyword_callback, required_fields=None, keywords=None):
    if not is_valid_income_data(json_str, required_fields, keywords):
        return False

    dct = json.loads(json_str)

    if len(dct) == 0:
        print("...Json is empty.")
        return None

    cnt_male_female = dict()
    for key in required_fields:
        if (key in dct):
            for value in keywords:
                if value in dct[key]:
                    keyword_callback(value, cnt_male_female)

    return cnt_male_female


js_str = json.dumps(my_dict)

print(parse_json(js_str, word_process, ['female', 'male'], ['Smith', 'hello', 'world']))
