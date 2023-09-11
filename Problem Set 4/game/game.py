import random

while True:
    try:
        user_input = int(input("Level: "))
        if user_input > 0:
            break

    except ValueError:
        pass

answer = random.randint(1, user_input)

guess = 0

while guess != answer:
    try:
        guess = int(input("Guess: "))
        if guess < 0:
            continue
        elif guess > answer:
            print("Too large!")
        elif guess < answer:
            print("Too small!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass