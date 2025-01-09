from art import logo
import random


def deal_card():

    # returns a random card from the deck
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    # Take a list of cards and return the score calculated from the cards
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, com_score):
    if u_score == com_score:
        return "Draw "
    elif com_score == 0:
        return "Lose, opponent has Blackjack "
    elif u_score == 0:
        return "Win with a Blackjack"
    elif u_score > 21:
        return "You went over. You lose "
    elif com_score > 21:
        return "Opponent went over. You win"
    elif u_score > com_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    print(logo)
    computers_cards = []
    your_cards = []
    is_game_over = False
    computer_score = -1
    user_score = -1

    for _ in range(2):

        your_cards.append(deal_card())
        computers_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(your_cards)
        computer_score = calculate_score(computers_cards)
        print(f"Your cards: {your_cards}, current score: {user_score}")
        print(f"Computer's first cards: {computers_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            another_card = input("Do you want another card? Type 'y' or 'no': ")
            if another_card == 'y':
                your_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computers_cards.append(deal_card())
        computer_score = calculate_score(computers_cards)

    print(f"Your final hand: {your_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computers_cards}, final score: {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    print("\n" * 20)
    play_game()
