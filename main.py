import os
import random
from hangman_art import logo,stages
from hangman_words import word_list

print(logo)
chosen_word= random.choice(word_list)
display = []
lives = 6
found = False

for _ in chosen_word:
    display.append("-")

print(display)


while "".join(display) != chosen_word and lives >= 0:
    guess= input("Guess a letter: ").lower()
    _ = os.system('clear')
    for i in range(len(chosen_word)):    
        if guess == chosen_word[i]: 
            display[i] = chosen_word[i]
            found = True
    if found:
        found = False
        print(display)
        print(f"\n{guess} is the right letter.\n") 
    else:
        print(stages[lives])
        print(f"{guess} is not the right letter. You lose a life.\n")
        lives -= 1        
    
if lives >= 0:
    print("\nYou won")
else:
    print(f"\nYou lose. The right word was {chosen_word}")
