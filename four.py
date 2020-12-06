import re


def load_data(file_name):  # "four_data.txt"
    data = []
    with open(file_name) as file:
        for f in file:
            data.append(f.strip())
    return data


def passports_separation(data):
    passports = []
    info_str = ""
    for line in data:
        info_str += line + " "
        if line == "" or line == data[-1]:
            passports.append(info_str[:-1])
            info_str = ""
    return passports


def correct_passports(passports):
    count = 0
    for passport in passports:
        finded = set(re.findall(r"([a-z]{3}:)", passport))
        if FIELDS.issubset(finded):
            count += 1
    return count


def main():
    data = load_data(file_dir)
    passports = passports_separation(data)
    valid_num = correct_passports(passports)
    print(valid_num)


FIELDS = set(["ecl:", "pid:", "eyr:", "hcl:", "byr:", "iyr:", "hgt:"])
file_dir = "four_data.txt"

if __name__ == "__main__":
    main()
