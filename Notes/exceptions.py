# exceptions are bad. These are errors that can happen

# print("hello, world)
# SyntaxError: unterminated string literal
# unterminated - started something not ended it
# string - type
# literal - you literally typed

# Runtime errors
x = int(input("What's x? "))
print(f"x is {x}")
# corner case - trying all possibilities for x
#   - try x = 0, 1, -1, cat
# when x = cat; error = invalid literal

# value error; *try* *except*
try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")

# better way of writing this limit the lines of code in try
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")


# main():

# *pass*
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass # repeats the question "What is x"


# main():