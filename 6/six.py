FILE_DIR = "six_data.txt"


def load_data():
    data = []
    with open(FILE_DIR) as file:
        for f in file:
            data.append(f.strip())
    return data


def count_yes(data):
    counter = 0
    answers = []
    for line in data:
        for ch in line:
            answers.append(ch)
        if line == "" or line == data[-1]:
            counter += len(set(answers))
            answers = []
    print(counter)


def main():
    declarations = load_data()
    count_yes(declarations)


if __name__ == "__main__":
    main()
