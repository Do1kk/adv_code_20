with open("eight_data.txt") as file:
    data = {}
    for key, line in enumerate(file):
        data[key] = line.strip()

history = []
key = 0
counter = 0
while True:
    history.append(key)
    if data[key][:3] == "acc":
        counter += int(data[key][3:])
    elif data[key][:3] == "jmp":
        key += int(data[key][3:])
        continue
    key += 1
    if key not in history:
        break

print(counter)
