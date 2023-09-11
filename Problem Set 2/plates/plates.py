def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if check_start(s) and check_length(s) and check_punctuation(s) and check_number(s) and check_middle(s):
        return True
    return False


def check_start(plate):
    return plate[0:2].isalpha()


def check_length(plate):
    return 2 <= len(plate) <= 6


def check_punctuation(plate):
    return plate.isalnum()


def check_number(plate):
    if plate.isalpha():
        return True
    elif plate[-1].isalpha():
        return False

    index = []

    for char in plate:
        if char.isnumeric():
            index.append(plate.find(char))
        else:
            continue

    if plate[int(index[0])] == "0":
        return False
    return True


def check_middle(plate):
    i = 1
    for i in range(1, len(plate) - 1):
        if plate[i].isnumeric() and plate[i + 1].isalpha():
            return False
    return True


main()