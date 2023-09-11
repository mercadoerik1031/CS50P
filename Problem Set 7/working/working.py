import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)"

    match = re.search(pattern, s)

    if match:
        hour1, minute1, period1, hour2, minute2, period2 = match.groups()

        if minute1 is None:
            minute1 = "00"
        if minute2 is None:
            minute2 = "00"

        hour1, minute1, hour2, minute2 = (
            int(hour1),
            int(minute1),
            int(hour2),
            int(minute2),
        )

        if (
            (period1 == "AM" or period1 == "PM")
            and (period2 == "AM" or period2 == "PM")
            and (0 <= hour1 <= 12)
            and (0 <= hour2 <= 12)
            and (0 <= minute1 <= 59)
            and (0 <= minute2 <= 59)
        ):

            if hour1 == 12 and period1 == "AM":
                hour1 = 0
            if hour2 == 12 and period2 == "AM":
                hour2 = 0

            if period1 == "PM" and hour1 != 12:
                hour1 += 12
            if period2 == "PM" and hour2 != 12:
                hour2 += 12

            result = f"{hour1:02}:{minute1:02} to {hour2:02}:{minute2:02}"

            return result

        else:
            raise ValueError("Invalid time format or range")
    else:
        raise ValueError("Invalid input format")

if __name__ == "__main__":
    main()
