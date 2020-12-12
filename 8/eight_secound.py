FILE_DIR = "eight_data.txt"


def load_data():
    with open(FILE_DIR) as file:
        data = {}
        for key, line in enumerate(file):
            data[key] = line.strip()
    return data


def check_line_rename(data):
    history = []
    key = 0
    counter = 0
    while True:
        if key in history or key == max(data.keys()):
            break
        history.append(key)
        if data[key][:3] == "acc":
            counter += int(data[key][3:])
        elif data[key][:3] == "jmp":
            key += int(data[key][3:])
            continue
        key += 1
    return key, counter


def rename_lines(data):
    last_keys = []
    for key, line in data.items():
        temp_data = data.copy()
        if line[:3] == "jmp":
            temp_data[key] = "nop" + temp_data[key][3:]
        elif line[:3] == "nop":
            temp_data[key] = "jmp" + temp_data[key][3:]
        last_key, counter = check_line_rename(temp_data)
        if last_key == max(data.keys()):
            break
    return counter


def main():
    data = load_data()
    counter = rename_lines(data)
    print(counter)


if __name__ == "__main__":
    main()
