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
