from collections import Counter

from six import load_data


def count_yes(data):
    counter = 0
    answers = []
    for line in range(len(data)):
        # When is one line.
        if answers == [] and data[line + 1] == "":
            counter += len(data[line])
        # Two and more lines.
        for ch in data[line]:
            answers.append(ch)
        if data[line] == "" or data[line] == data[-1]:
            counter_k_v = Counter(answers)
            print(counter_k_v)
            counter += sum(1 for i in counter_k_v.values() if i > 1)
            answers = []
    print(counter)


def main():
    declarations = load_data()
    count_yes(declarations)


if __name__ == "__main__":
    main()
