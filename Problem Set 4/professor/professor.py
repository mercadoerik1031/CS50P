import random


def main():
    level = get_level()
    score = 0

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = int(input(f"{x} + {y} = "))

        for j in range(2):
            if answer == x + y:
                score += 1
                break
            else:
                print("EEE")
                answer = int(input(f"{x} + {y} = "))
                print(f"{x} + {y} =", x + y)

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            user_input = int(input("Level: "))

            if 0 < user_input < 4:
                break
        except ValueError:
            pass

    return user_input


def generate_integer(level):
    while True:
        try:
            if level in (1, 2, 3):
                break
        except ValueError:
            pass

    if level == 1:
        start = 0
        stop = 10
    else:
        start = 10 ** (level - 1)
        stop = (10**level) - 1

    return random.randint(start, stop)


if __name__ == "__main__":
    main()
