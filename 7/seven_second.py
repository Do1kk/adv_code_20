import re
from seven import load_data
from seven import FILE_DIR

FIRST_BAG_NAME = "shiny gold"


def bags_to_dict(data):
    bags = {}
    for line in data:
        first_bag = re.search(r"^((\w+ )+)bags contain \d", line)
        inner_bags = re.findall(r"(\d+) (\w+ \w+) bag", line)
        if first_bag != None:
            bags[first_bag.group(1)[:-1]] = inner_bags
    return bags


def count(bag_name, bags):
    return sum(
        [
            int(bag[0]) * int(count(bag[1], bags) + 1)
            if bag[1] in bags
            else int(bag[0])
            for bag in bags[bag_name]
        ]
    )


def main():
    data = load_data(FILE_DIR)
    bags_dict = bags_to_dict(data)
    value = count(FIRST_BAG_NAME, bags_dict)
    print(value)


if __name__ == "__main__":
    main()
