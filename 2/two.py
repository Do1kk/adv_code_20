import re

data = []
with open("two_data.txt") as file:
    for f in file:
        data.append(f.strip())

counter = 0
for line in data:
    regularexp = re.search("(\d+)-(\d+) ([a-z]): ([a-z]+)", line)
    occurrence = len(
        [i.start() for i in re.finditer(regularexp.group(3), regularexp.group(4))]
    )
    min_occ = int(regularexp.group(1))
    max_occ = int(regularexp.group(2))
    if occurrence <= max_occ and occurrence >= min_occ:
        counter += 1

print(counter)
