list_of_months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def is_valid_date(month, day, year):
    try:
        month = int(month)
        day = int(day)
        year = int(year)
        if month < 1 or month > 12 or day < 1 or day > 31 or year < 1:
            return False
        return True
    except ValueError:
        return False


def convert_to_iso_date(date_parts):
    month = date_parts[0]
    day = date_parts[1].rstrip(',')
    year = date_parts[2]

    if month.isdigit():
        month_num = int(month)
        return f"{year:04}-{month_num:02}-{int(day):02}"
    else:
        month_num = list_of_months.index(month.capitalize()) + 1
        return f"{year:04}-{month_num:02}-{int(day):02}"


def main():
    while True:
        date = input("Date: ").strip()

        if '/' in date:
            date_parts = date.split('/')
        else:
            date_parts = date.split(' ')

        if len(date_parts) == 3 and is_valid_date(date_parts[0], date_parts[1], date_parts[2]):
            iso_date = convert_to_iso_date(date_parts)
            print(iso_date)
            break
        else:
            pass

main()