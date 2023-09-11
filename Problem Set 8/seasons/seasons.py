import re
import inflect
import sys

from datetime import date


def main():
    user_input = input("Date of Birth: ")

    if not is_valid_format(user_input):
        sys.exit("Invalid date")

    bday = is_valid_format(user_input)
    days = convert_to_days(bday)
    minutes = convert_to_minutes(days)

    print(minutes_to_str(minutes))


def is_valid_format(bday):
    pattern = r"^([0-9]{4})-([0-9]{2})-([0-9]{2})?"

    if matches := re.search(pattern, bday):
        year = int(matches.group(1))
        month = int(matches.group(2))
        day = int(matches.group(3))

        if 1 <= month <= 12 and 1 <= day <= 31:
            return date(year, month, day)

    return False


def convert_to_days(bday):
    today = date.today()
    days = today - bday
    days = str(days).split(" ")
    return int(days[0])


def convert_to_minutes(days):
    return round(days * 24 * 60)


def minutes_to_str(minutes):
    p = inflect.engine()
    return p.number_to_words(minutes, andword="").capitalize() + " minutes"


if __name__ == "__main__":
    main()
