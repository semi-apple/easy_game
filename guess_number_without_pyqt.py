import random


def print_random_number():
    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 0 and 9.")

    for i in range(10):
        secret_number = random.randint(0, 9)
        print('i is ', i, '; secret number is ', secret_number)


print_random_number()
