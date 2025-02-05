import random
from art import logo, vs
from game_data import data

# todo - randomize game_data
# todo - print game_data w/o followers #'s
# todo - compare data "A" to data "B"
# todo - correct answer becomes data A
# todo - keep score

 
#  returns information w/o followers numbers
def format_data(celebrity):
    celebrity_name = celebrity['name']
    celebrity_descr = celebrity['description']
    celebrity_country = celebrity['country']
    return f"{celebrity_name}, a {celebrity_descr}, from {celebrity_country}" 

# compare users input to actual follower information
def compare_answer(user_guess, follower_a, follower_b):
    if follower_a > follower_b:
        return user_guess == 'a'
    else:
        return user_guess == 'b'
 
 
print(logo)    
score = 0

     # returns a random data from game_data
celebrityB = random.choice(data)  

# so game continues
continue_game = True
 
# make game continue
while continue_game:
    
    # correct answer now becomes celebrityA and new celebrity B
    celebrityA = celebrityB
    celebrityB = random.choice(data)    
    
    if celebrityA == celebrityB:
        celebrityB = random.choice(data)

    print(f"Compare A: {format_data(celebrityA)}.")
    print(vs)
    print(f"Compare B: {format_data(celebrityB)}.")
    
    # Ask user to guess
    guess = input("Who has more followers? Type 'A' or 'B': ").casefold()

     # clear the screen for new game
    print("\n" * 20)
    print(logo)


    # follower count of celebrityA vs celebrityB
    followerA_count = celebrityA["follower_count"]
    followerB_count = celebrityB['follower_count']

    # check if user is correct
    is_correct = compare_answer(guess, followerA_count, followerB_count)

    if is_correct:
        score +=1
        print(f"You're correct! Current Score {score}")
    else:
        print(f"Sorry you're wrong! Score is {score}")
        continue_game = False
      
