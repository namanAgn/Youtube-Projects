import random
import time
import string

alphabet = string.ascii_lowercase

letters = []
checkLetters = []

guessedLetters = ''

easy = ['trial', 'truck', 'tired']

print("Guess the word game!")
time.sleep(1)
print("A 5 letter word would be given to you for you to guess.")
time.sleep(1)

Word = random.choice(easy)

i = 0
easyGuesses = 6
letter = 0

for  i in Word:
  letters += i

for letter in alphabet:
  checkLetters += letters

while easyGuesses > 0:
  guess = input("Enter a random letter of your choice: ")
  if letters.__contains__(guess):
    print("You guessed the letter correctly!")
    guessedLetters += guess
    if guessedLetters == Word:
      print("You guessed the word!")
      break
    else: 
      continue
  else:
    print(f"{guess} is not in the word.")
    easyGuesses -= 1
  if easyGuesses == 0:
    print(f"You have ran out of guesses! The word was {Word}")