import math

data = []
with open("three_data.txt") as file:
    for f in file:
        data.append(f.strip())

step_r = [1, 3, 5, 7, 1]
step_d = [1, 1, 1, 1, 2]
len_line = len(data[0])
tree_in_slopes = []

for r, d in zip(step_r, step_d):
    trees = 0
    point_now = 0
    for i in range(d, len(data), d):
        point_now += r
        if data[i][point_now % len_line] == "#":
            trees += 1
    tree_in_slopes.append(trees)

print(tree_in_slopes)
print(math.prod(tree_in_slopes))
