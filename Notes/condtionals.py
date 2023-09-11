> # greater than
>= # greater than or =
< # less than
<= # less than or =
== # equality / comparing
!= # not equal to
if # ask questions
or # ask multiple questions
and # a conjunction of questions
+ # addition
- # subtraction
* # multiplication
/ # division
% # modulus
match # like switch


x = int(input("What's x? "))
y = int(input("What's y? "))


# ask question
# this asks 3 different questions
if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")


# ask fewer questions
# elif - if there hasn't been a true value ask the next question
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")


# ask multiple equations with 'or'
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# if all we care if x != y
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")


####################################################################
# grade.py

score = int(input("Score: "))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else"
    print("Grade: F")


# cleaner code
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


##########################################################################
# parity.py

x = int(input("Whats x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")


def main():
    x = int(input("Whats x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
# n % 2 == 0 is a bool either true or false
    return n % 2 == 0


main()


#####################################################
# house.py

name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
    print("Who?")