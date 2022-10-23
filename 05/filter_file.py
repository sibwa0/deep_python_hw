def filter_file(file, targets: list):
    sentence = file.readline()

    while sentence != "":
        for target in targets:
            if target in sentence.strip().lower().split():
                yield sentence
                break
        sentence = file.readline()
