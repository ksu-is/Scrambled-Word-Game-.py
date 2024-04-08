import random

# This is the welcome screen code
def welcome():
    print("Welcome to the Word Scrambled Game!")
    print("There are three levels, to move through each level you will have to unscramble each word correctly.")
    print("Enjoy unscrambling!")
    input("Press Enter to Start!")
print()

# This is the word bank 
words_one = ['fun']
words_two = ['alert']
words_three = ['computer']


for word in range(len(words)):
  scrambled =  "".join(random.sample(words_one[word] , len(words_one[word])))
  print (f"Unscramble this word! {scrambled} ")
  guess = input("Write here:")
if guess == words_one[word]:
  print("Correct! Move on to the next level!")
else:
  print("Incorrect, Please try again!")

  for word in range(len(words_two)):
     scrambled = "".join(random.sample(words_two[word] , len(words_two[word])))
     print (f"Unscramble this word! {scrambled} ")
     guess == input("Write here:")
if guess == words_two[word]:
   print("Correct! Move on to the last level!")
else:
   print("Incorrect, Please try again!")

 

