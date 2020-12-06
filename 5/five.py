NUM_OF_ROW = 128
NUM_OF_COL = 8
FILE_DIR = "five_data.txt"


def load_data():
    data = []
    with open(FILE_DIR) as file:
        for line in file:
            data.append(line.strip())
    return data


def what_row(seat):
    max_possible_row = NUM_OF_ROW
    min_possible_row = 0
    for char_row in seat[:-3]:
        change = (max_possible_row - min_possible_row) / 2
        if char_row == "B":
            min_possible_row += change
        else:
            max_possible_row -= change
    return min_possible_row


def what_column(seat):
    max_possible_col = NUM_OF_COL
    min_possible_col = 0
    for char_col in seat[-3:]:
        change = (max_possible_col - min_possible_col) / 2
        if char_col == "R":
            min_possible_col += change
        else:
            max_possible_col -= change
    return min_possible_col


def seat_id(row, col):
    return row * 8 + col


def main():
    data = load_data()
    list_of_ids = []
    for line in data:
        row = what_row(line)
        col = what_column(line)
        list_of_ids.append(seat_id(row, col))
    print(max(list_of_ids))


if __name__ == "__main__":
    main()
