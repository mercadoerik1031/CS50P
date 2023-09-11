def main():
    while True:
        user_input = input("Fraction: ")

        if "/" in user_input and (user_input[0].isdigit() and user_input[-1].isdigit()):
            break
        else:
            continue

    percent = convert(user_input)
    print(gauge(percent))


def convert(fraction):
    x, y = fraction.split("/")

    while True:
        try:
            x_int = int(x)
            y_int = int(y)
            x_int < y_int

            return round((x_int / y_int) * 100)

        except (ValueError, ZeroDivisionError):
            pass


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
