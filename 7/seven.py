import re

FILE_DIR = "seven_data.txt"


def load_data(file_name):
    data = []
    with open(file_name) as file:
        for line in file:
            data.append(line.strip())
    return data


def bags_counter(text):
    bags_name = ["shiny gold"]
    for i in range(4):
        for line in text:
            for name in bags_name:
                finded = re.search(rf"^((\w+ )+)bags contain .*{name}", line)
                if finded != None:
                    bags_name.append(finded.group(1))
        bags_name = list(set(bags_name))
    return len(set(bags_name))


def main():
    text = load_data(FILE_DIR)
    number = bags_counter(text)
    print(number)


if __name__ == "__main__":
    main()
