# cat.py
# wrong way to do it
'''
print("meow")
print("meow")
print("meow")
print("meow")
print("meow")
'''
i = 0
while i < 0: # ask a question over and over
    print("meow")
    i += 1

# for loop & list
for i in [0, 1, 2]: # i iterates through the list
    print("meow")

# if you don't care about the variable use "_"
for _ in range(100000): # i = 0 and goes up to 99999
    print("meow")

# other ways to repeat
print("meow\n" * 3, end="") # end="" removes empty line at bottom

# ask user how many time to repeat
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")


# create a function to repeat
def main():
    meow(3)


def get_number():
    while True:
        n = int(input("What's n"))
        if n > 0:
            break
    return n


def meow(n):
    for _ in range(n):
        print("meow")

main()


# lists
students = ["Hermione", "Harry", "Ron"]
print(students[0]) # prints Hermione
print(students[1])
print(students[2])

# other way to do it
students = ["Hermione", "Harry", "Ron"]
for student in students:
    print(student)

# len()
students = ["Hermione", "Harry", "Ron"]
for i in range(len(students)):
    print(i + 1, students[i])

# dictionaries {"keys": "value"}
# example we what to keep track of who is in what house
students = {"Hermione": "Gryffindor",
            "Harry": "Gryffindor",
            "Ron": "Gryffindor",
            "Draco": "Slytherin",
            }

for student in students:
    print(student, students[student], sep=", ") # prints Name and House

# dictionaries with multiple values
# list of dictionaries
students = [{"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}]


for student in students:
    print(student["name"], student["house"], student["patronus"], sep="") # print name, house, patronus


# nest for loop
print("#")
print("#")
print("#")

for _ in range(3):
    print("#")

def main():
    print_column(3)


def print_column(height):
    print("#\n", end="")

def print_row(width):
    print("?" * width)

def print_square(size):
    # for each row in square
    for i in range(size):

        # for each brick in row
        for j in range(size):

            # print brick
            print("#", end="")

        # starts the new row
        print()

# other way to print a square
def print_square(size):
    for i in range(size):
        print("#" * size)