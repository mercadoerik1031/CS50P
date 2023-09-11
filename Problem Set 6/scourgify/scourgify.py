import sys
import csv


def main():
    is_valid_argv()
    students_dict = reader(sys.argv[1])
    writer(students_dict, sys.argv[-1])


def is_valid_argv():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if not sys.argv[-1].endswith(".csv"):
            sys.exit("Not a CSV file")

        try:
            open(sys.argv[1])
        except FileNotFoundError:
            sys.exit("File does not exist")


def reader(f):
    students = []

    with open(f, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            students.append({"name": row["name"], "house": row["house"]})

    return students


def writer(students, f):
    with open(f, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()

        for row in students:
            last_name, first_name = row["name"].split(",")
            house = row["house"]

            writer.writerow(
                {
                    "first": first_name.strip(),
                    "last": last_name.strip(),
                    "house": house.strip(),
                }
            )


if __name__ == "__main__":
    main()
