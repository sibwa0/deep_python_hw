def filter_file(file, targets: list):
    result = []

    with open(file, "r") as f:
        file_as_txt = [s for s in f.readlines()]

        for sentence in file_as_txt:
            for target in targets:
                if target in sentence.strip().lower().split():
                    result.append(sentence)
                    break

    return result


if __name__ == "__main__":
    targets = ["роз", "яяя"]

    print(filter_file("file_for_filter.txt", targets))
