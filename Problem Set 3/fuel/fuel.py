def main():
    fuel = get_fuel("Fraction: ")
    print(fuel)


def get_fuel(prompt):
    while True:
        user_input = input(prompt)

        if user_input.find("/") == -1:
            continue

        x, y = user_input.split("/")

        try:
            x_int = int(x)
            y_int = int(y)

            if x_int > y_int:
                continue

            result = x_int / y_int

        except (ValueError, ZeroDivisionError):
            pass

        else:
            fuel = round(result * 100)
            if fuel <= 1:
                return "E"
            elif fuel >= 99:
                return "F"
            else:
                return str(fuel) + "%"


main()