# hangman
milestone 1 and 2 explanations were uploaded directly onto Github as I was still getting used to using the systems and commiting changes etc. 
Milestone 1 was fairly straightforward in the sense that all a list was created of the possible words in the game. Print statements were used.
import random


word_list = ['apple','mango','peach','blueberry','banana']
word = random.choice(word_list)
print(word) 
guess = input("Guess the letter")
if len(guess) == 1 and guess.isalpha:
    print("Good Guess!")
else:
    print("Oops!,that is not valid input")


Milestone 2 is where functions came into actions with the use of the 'def' method where user input was integrated along with the guesses being checked too. 
def check_guess(guess):
    guess = guess.lower 
    if guess in word:
        print (f"Good guess!'{guess} is in word")
    else:
        print(f"Sorry, {guess} is not in the word. Try again")


milestone 3 explanation
The hangman class was set up along with the methods allowing for the parameters to be intitialised. All the attributes were set up using the 'self' instance. The check_guess method was edited to peform actions for if the guess is part of the word. Characters were removed from num_letters. The ask_for_input was also checked for if the input is already in the list of guesses. 
class Hangman:
    def __init__(self,word_list,num_lives = 5):
        self.word = random.choice(word_list).lower()
        self.word_guessed = len(self.word)*['']
        self.num_letters = len(set(self.word)) - set(self.word_guessed)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
