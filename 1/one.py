data = []
result = -1
with open("one_data.txt") as file:
    for f in file:
        data.append(int(f.strip()))

for i in range(len(data)):
    for j in range(i, len(data)):
        if data[i] + data[j] == 2020:
            result = data[i] * data[j]


print(result)
