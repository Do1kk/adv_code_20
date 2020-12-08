import re

from four import load_data, passports_separation
from four import FIELDS, FILE_DIR


def strict_passports_correction(passports):
    count = 0
    for passport in passports:
        finded = set(re.findall(r"([a-z]{3}:)", passport))
        if FIELDS.issubset(finded):
            # byr
            find_strict = re.search(r"byr:(\d{4})", passport)
            bound = int(find_strict.group(1))
            if bound < 1920 or bound > 2002:
                continue
            # iyr
            find_strict = re.search(r"iyr:(\d{4})", passport)
            bound = int(find_strict.group(1))
            if bound < 2010 or bound > 2020:
                continue
            # eyr
            find_strict = re.search(r"eyr:(\d{4})", passport)
            bound = int(find_strict.group(1))
            if bound < 2020 or bound > 2030:
                continue
            # hgt
            find_strict = re.search(r"hgt:(\d{3}cm|\d{2}in)", passport)
            if find_strict is None:
                continue
            bound_str = find_strict.group(1)
            bound = int(bound_str[:-2])
            if bound_str[-2:] == "cm":
                if bound < 150 or bound > 193:
                    continue
            if bound_str[-2:] == "in":
                if bound < 59 or bound > 76:
                    continue
            # hcl
            find_strict = re.search(r"hcl:(#([a-f0-9]*))", passport)
            if find_strict is None or len(find_strict.group(1)) != 7:
                continue
            # ecl
            find_strict = re.search(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)", passport)
            if find_strict is None:
                continue
            # pid
            find_strict = re.search(r"pid:([0-9]*)", passport)
            if len(find_strict.group(1)) != 9:
                continue

            count += 1
    return count


def main():
    data = load_data(FILE_DIR)
    passports = passports_separation(data)
    valid_num = strict_passports_correction(passports)
    print(valid_num)


if __name__ == "__main__":
    main()
