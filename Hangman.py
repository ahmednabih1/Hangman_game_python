
"""
Word guessing game (hangman)
○ A list of words will be hardcoded in your program, out of
  which the interpreter will
○ choose 1 random word.
○ The user first must input their names
○ Ask the user to guess any alphabet. If the random word
  contains that alphabet, it
○ will be shown as the output(with correct placement)
○ Else the program will ask you to guess another alphabet.
○ Give 7 turns maximum to guess the complete word.
"""
import random
#following line was just to test
#arr2=["goat"]

arr2=["ahmed","nabih","persona","rain","goat",]

word=random.choice(arr2)
username=input("enter your name: ")
word_length=len(word)
guess="_" * word_length
"""print(word)"""

for i in range(0,7):
    letter = input("guess a letter: ")
    print('you still have ', (6-i),'tries')
    if i==7:
        print("failed")

    for i in range(0,word_length):
        if word[i]==letter:
            guess=guess[0:i] + letter + guess[i+1:word_length]


    if guess==word:
        print("well done")
        break

    print(guess)



