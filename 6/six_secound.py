from collections import Counter

from six import load_data


def count_yes(data):
    counter = 0
    answers = []
    line_counter = 0
    # Last line. "strip()" in load_data erase last line.
    data.append("\n")
    for line in range(len(data[:])):
        line_counter += 1
        for ch in data[line]:
            answers.append(ch)
        if data[line] == "" or data[line] == data[-1]:
            counter_k_v = Counter(answers)
            counter += sum(1 for i in counter_k_v.values() if i == line_counter - 1)
            answers = []
            line_counter = 0
    print(counter)


def main():
    declarations = load_data()
    count_yes(declarations)


if __name__ == "__main__":
    main()
