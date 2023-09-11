import sys


def main():
    check_argv()
    print(count_lines(sys.argv[-1]))


def check_argv():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if not sys.argv[-1].endswith(".py"):
            sys.exit("Not a Python file")

        try:
            open(sys.argv[-1])
        except FileNotFoundError:
            sys.exit("File does not exist")


def count_lines(f):
    count = 0

    with open(f, "r") as file:
        for line in file:
            if line.lstrip().startswith("#") or line.strip() == "":
                continue
            else:
                count += 1
        return count


if __name__ == "__main__":
    main()
