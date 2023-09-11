import sys


from tabulate import tabulate


def main():
    check_argv()
    file = sys.argv[-1]
    headers = get_table(file)[0]
    table = get_table(file)[1:]

    print(tabulate(table, headers, tablefmt="grid"))


def check_argv():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if not sys.argv[-1].endswith(".csv"):
            sys.exit("Not a CSV file")

        try:
            open(sys.argv[-1])
        except FileNotFoundError:
            sys.exit("File does not exist")


def get_table(f):
    table = []
    with open(f, "r") as file:
        for line in file:
            table.append(line.rstrip().split(","))
    return table


if __name__ == "__main__":
    main()
