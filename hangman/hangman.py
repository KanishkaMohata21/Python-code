import random
import hangman2
choosen_word=random.choice(hangman2.list_of_words)
lives=10
display=[]
for letter in choosen_word:
    display+="_"
print(display)
while lives!=0:
    guess=input("Guess a letter:").lower()
    if guess in display:
        print(f"You have already guessed {guess}")
    for position in range(len(choosen_word)):
        letter=choosen_word[position]
        if letter==guess:
                display[position]=letter
    if guess not in choosen_word:
        lives-=1
        print(f"Choosen letter is not in the word ,{lives} lives left")     
    print(display)
    if lives==0:
        print("You lose")
    if "_" not in display:
        print("You win")