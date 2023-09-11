import inflect

p = inflect.engine()

names = []


def main():
    while True:
        try:
            user_input = input("Name: ")
            user_input.isalpha()
        except EOFError:
            break

        else:
            names.append(user_input.capitalize())

    name_list = p.join(names)
    print("\nAdieu, adieu, to " + name_list)


if __name__ == "__main__":
    main()