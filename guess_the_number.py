import random
print("Welcome to the GUESS THE NUMBER GAME")
print("I am thinking of a number between 1 to 100")
difficulty_level=(input("Choose the difficulty level.easy or hard:")).lower()
if difficulty_level=="easy":
    print("U have 10 attempts")
    attempts=10
elif difficulty_level=="hard":
    print("U have 5 attempts")
    attempts=5
else:
    print("INVALID INPUT")

num=random.randint(1,100)
while attempts!=0:
    user_input=int(input("Guess a number:"))
    if user_input==num:
        print("CONGRATULATIONS!You Won")
    elif user_input>num:
        print("Greater than the number")
        attempts-=1
        print(f"{attempts} attempts left")
    elif user_input<num:
        print("Lesser than the number")
        attempts-=1
        print(f"{attempts} attempts left")
    else:
        print("Invalid guess")

print("Ohh,U lost")


