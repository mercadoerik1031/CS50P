import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # 25[0-5]: This matches numbers from 250 to 255, ensuring that the first digit is 2, and the second digit can be any digit from 0 to 5.

    # 2[0-4][0-9]: This matches numbers from 200 to 249. It ensures that the first digit is 2 and the second digit can be any digit from 0 to 4,
    # and the third digit can be any digit from 0 to 9.

    # [0-1]?[0-9][0-9]?: This matches numbers from 0 to 199. It allows for optional leading zeros and matches one or two digits.
    # [0-1]? allows for an optional leading digit 0 or 1. [0-9] matches any single digit, and [0-9]? allows for an optional second digit.
    if re.match(
        r"^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$",
        ip,
    ):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
