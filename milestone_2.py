from random import random


word_list = ['apple','mango','peach','blueberry','banana']
word = random.choice(word_list)


while True:
    guess = input("Guess the letter!")
    if not len(guess) == 0 or not guess.isalpha():
        print('Invalid letter. Please, enter a single alphabetical character')
    else:
        break

if guess is word:
    print (f"Good guess!'{guess} is in word")
else:
    print(f"Sorry, {guess} is not in the word. Try again")
    