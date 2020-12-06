import statistics
from five import load_data, what_row, what_column, seat_id


def main():
    data = load_data()
    list_of_ids = []
    for line in data:
        row = what_row(line)
        col = what_column(line)
        list_of_ids.append(seat_id(row, col))

    sort_list_ids = sorted(map(int, list_of_ids))
    missing_ids = []
    for i in range(min(sort_list_ids), max(sort_list_ids)):
        if i not in sort_list_ids:
            missing_ids.append(i)
    print(int(statistics.median(missing_ids)))


if __name__ == "__main__":
    main()
