from art import logo
import random
print(logo)

# todo choose a number between 1 and 100
# todo choose easy or hard
# todo guess the number
# todo check the number against chosen number
# todo reduce the attempts with every guess
easy_attempts = 10
hard_attempts = 5

def check_guess(user_guess, actual_answer,attempts):
    # Checks answer against guess, returns the number of attempts remaining
    if user_guess > actual_answer:
        print("Too high.")
        return attempts - 1
    elif user_guess < actual_answer:
        print("Too low!")
        return attempts - 1
    else:
        print(f"You got it! The answer was {actual_answer}")


# choose easy or hard
def is_easy_or_hard():
    user_choice = input("Do you choose 'Easy' or 'Hard'?: ").casefold()
    if user_choice == "easy":
        return easy_attempts
    else:
        return hard_attempts

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    num = random.randrange(1, 101)
    print(f"Psst, the correct number is {num}")

    attempts = is_easy_or_hard()


    # loop if the guess is wrong
    guess = 0
    while guess != num:
        print(f"You have {attempts} attempts remaining to guess the number.")

    # let the user guess a number
        guess = int(input("Make a guess: "))
        attempts = check_guess(guess, num, attempts)
        if attempts == 0:
            print("You've run out of attempts. GAME OVER!")
            return

play_game()