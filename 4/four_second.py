from os import error
import re

from four import load_data, passports_separation
from four import FIELDS, FILE_DIR


def strict_passports_correction(passports):
    count = 0
    for passport in passports:
        finded = set(re.findall(r"([a-z]{3}:)", passport))
        if FIELDS.issubset(finded):
            # byr
            finded_strict = re.search(r"byr:(\d{4})", passport)
            bound = int(finded_strict.group(1))
            if bound < 1920 or bound > 2002:
                continue
            # iyr
            finded_strict = re.search(r"iyr:(\d{4})", passport)
            bound = int(finded_strict.group(1))
            if bound < 2010 or bound > 2020:
                continue
            # eyr
            finded_strict = re.search(r"eyr:(\d{4})", passport)
            bound = int(finded_strict.group(1))
            if bound < 2020 or bound > 2030:
                continue
            # hgt
            finded_strict = re.search(r"hgt:(\d{3}cm|\d{2}in)", passport)
            if finded_strict is None:
                continue
            bound_str = finded_strict.group(1)
            bound = int(bound_str[:-2])
            if bound_str[-2:] == "cm":
                if bound < 150 or bound > 193:
                    continue
            if bound_str[-2:] == "in":
                if bound < 59 or bound > 76:
                    continue
            # hcl
            finded_strict = re.search(r"hcl:(#([a-f0-9]*))", passport)
            if finded_strict is None or len(finded_strict.group(1)) != 7:
                continue
            # ecl
            finded_strict = re.search(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)", passport)
            if finded_strict is None:
                continue
            # pid
            finded_strict = re.search(r"pid:([0-9]*)", passport)
            if len(finded_strict.group(1)) != 9:
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
