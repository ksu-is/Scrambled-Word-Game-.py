import random

# This is the welcome screen code
def welcome():
    print("Welcome to the Word Scrambled Game!")
    print("There are three levels, to move through each level you will have to unscramble each word correctly.")
    print("Enjoy unscrambling!")
  input("Press Enter to Start!")
print()

# This is the word bank 
words = ['fun', 'alert', 'computer']


for word in range(len(words)):
  scrambled =  "".join(random.sample(words[word] , len(words[word])))
  print (f"Unscramble this word! {scrambled} ")
 guess = input("Write here: ")
if guess == words[word]:
  print("Correct! Move on to the next level!")
else:
  print("Incorrect, Please try again!")
 

