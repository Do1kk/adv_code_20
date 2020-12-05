import re

data = []
with open("two_data.txt") as file:
    for f in file:
        data.append(f.strip())

counter = 0
for line in data:
    regularexp = re.search("(\d+)-(\d+) ([a-z]): ([a-z]+)", line)
    password = regularexp.group(4)
    charact = regularexp.group(3)

    f_occ = int(regularexp.group(1)) - 1
    s_occ = int(regularexp.group(2)) - 1
    if (
        password[f_occ] == charact
        and password[s_occ] != charact
        or password[f_occ] != charact
        and password[s_occ] == charact
    ):
        counter += 1

print(counter)
