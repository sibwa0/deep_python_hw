def filter_file(file, targets: list):
    result = []

    with open(file, "r", encoding='utf-8') as file_desc:
        file_as_txt = list(file_desc.readlines())

        for sentence in file_as_txt:
            for target in targets:
                if target in sentence.strip().lower().split():
                    result.append(sentence)
                    break

    return result

def filter_file_gen(file, targets: list):
    sentence = file.readline()
    
    while sentence != "":
        for target in targets:
            if target in sentence.strip().lower().split():
                yield sentence
                break
        sentence = file.readline()

    return None


if __name__ == "__main__":
    with open("file_for_filter.txt", "r", encoding='utf-8') as file_desc:
        targets = ["роза", "яяя"]
        result = []

        for sentence in filter_file_gen(file_desc, targets):
            result.append(sentence)