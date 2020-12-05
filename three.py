data = []
with open("three_data.txt") as file:
    for f in file:
        data.append(f.strip())

point_now = 0
step = 3
len_line = len(data[0])
trees = 0
data = data[1:]
for line in data:
    point_now += step
    if line[point_now % len_line] == "#":
        trees += 1

print(trees)
