import random
user_choice=int(input("What is your choice?\nEnter 0 for rock,1 for paper,2 for scissor:"))
if user_choice>=3 or user_choice<0:
    print("Invalid number")
else:
    if user_choice==0:
            print("You choose rock")
    elif user_choice==1:
            print("You choose paper")
    else:
            print("You choose scissor")
    computers_choice=random.randint(0,2)
    if computers_choice==0:
        print("Computer choose rock")
    elif computers_choice==1:
        print("Computer choose paper")
    else:
        print("Computer choose scissor")

    if user_choice==0 and computers_choice==2:
        print("You won")
    elif computers_choice>user_choice:
        print("You lose")
    elif computers_choice==0 and user_choice==2:
        print("You lose")
    elif user_choice>computers_choice:
        print("You win")
    else:
        print("Draw")
