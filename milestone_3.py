import random
class Hangman:
    def __init__(self,word_list,num_lives = 5):
        self.word = random.choice(word_list).lower()
        self.word_guessed = len(self.word)*['']
        self.num_letters = len(set(self.word)) - set(self.word_guessed)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

def check_guess(self,guess):
    guess = guess.lower 
    if guess in self.word:
        print (f"Good guess!'{guess} is in word")
        for a,letter in enumerate(self.word):
            if guess == letter:
                print("Well Done!")
                self.word_guessed[a] == guess
                print(self.num_letters)
            self.num_letters -= 1 

    else:
        self.num_lives -=1 
        print(f"Sorry, {guess} is not in the word. Try again")
        print(f"You have {self.num_lives} left")
    self.list_of_guesses.append(guess) 

def ask_for_input(self):
    while True:
         guess = input("Guess the letter!")
         if not len(guess) == 0 or not guess.isalpha():
             print('Invalid letter. Please, enter a single alphabetical character')
         elif guess in self.list_of_guesses:
            print("You already tried that letter!")
         else:
            self.check_guess(guess)
            break