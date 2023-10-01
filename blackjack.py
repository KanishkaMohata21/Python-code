import random
import os
def continue_playing():
    user_card=[]
    computer_card=[]
    is_game_over=False

    def returing_card():
        cards=[11,2,3,4,5,6,7,8,9,10,10,10,10,10]
        card=random.choice(cards)
        return card 

    for i in range(2):
        user_card.append(returing_card())
        computer_card.append(returing_card())

    def calculate_card(card):
        return sum(card)

    def calculate_score(card):
        if sum(card)==21 and len(card)==2:
            return 0
        if 11 in card and sum(card)>21:
            card.remove(11)
            card.append(1)
        return sum(card)

    def compare(user_score,computer_score):
        if user_score == computer_score:
            return "Draw 🙃"
        elif computer_score == 0:
            return "Lose, opponent has Blackjack 😱"
        elif user_score == 0:
            return "Win with a Blackjack 😎"
        elif user_score > 21:
            return "You went over. You lose 😭"
        elif computer_score > 21:
            return "Opponent went over. You win 😁"
        elif user_score > computer_score:
            return "You win 😃"
        else:
            return "You lose 😤"

    while is_game_over!=True:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"Your cards: {user_card}, current score: {user_score}")
        print(f"Computer's first card: {computer_card[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_card.append(returing_card())
            else:
                is_game_over = True

    while computer_score!=0 and computer_score<17:
        computer_card.append(returing_card())
        computer_score=calculate_score(computer_card)

    print(compare(user_score,computer_score))
    print(f"Your final hand: {user_card}, final score: {user_score}")
    print(f"Computer's final hand: {computer_card}, final score: {computer_score}")

while input("Do you want to play a game of Blackjack? Type 'y' or 'n':")=="y":
    os.system("cls")
    continue_playing()