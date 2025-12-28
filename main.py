import random
from art import logo

def guess_the_number():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    num = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if(difficulty == 'easy'):
        count = 10
    elif(difficulty == 'hard'):
        count = 5
    else:
        print("Choose easy or hard.")
        guess_the_number()

    while(count != 0):
        print(f"You have {count} attempts remaining to guess the number.")

        temp = int(input("Make a guess: "))
        if(temp == num):
            print(f"You guessed right, the number is {num}.")
            exit()
        else:
            count -= 1

        if(temp > num):
            print("Too high.")
        else:
            print("Too low.")

        print("Guess again.")

guess_the_number()