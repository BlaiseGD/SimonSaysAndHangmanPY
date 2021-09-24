import string
import random
import os
clear = lambda: os.system('clear')
################
#Makes simonSays
def simonSays():
  playerInput = ''
  simonsays = ''
  simonsaysALL = ''
  score = -1
  print('Instructions: type in the specified letter and as it goes on type the current letter and the letters prior')
  while simonsaysALL == playerInput:
    clear()
    simonsays = random.choice(string.ascii_letters)
    simonsaysALL += simonsays;
    print('simon says type in ' + simonsays)
    playerInput = input()
    score+=1
  print('\nYou lose! Your score was ' + str(score))
##############
#Makes Hangman
def Hangman():
  guesscount = 0
  correctcount = 0
  count = 0
  print('This game is designed with the intention of two people playing together\n\nWhat word do you want the player to guess?')
  print("You can guess wrong 11 times because some random website said that's the case")
  word = list(input()) #Takes word as list so I can iterate and check for player input to match
  while guesscount != 11:
    print('Type in a number:')
    playerguess=input()
    for i in word:
      if i == playerguess:
        print('correct')
        word[count] = None;
        correctcount += 1;
      count+=1 #This variable is to iterate so I can change the word list
    if correctcount == len(word):
      clear()
      print('You win!')
      exit(0)
    count = 0
    guesscount+=1
  clear()
  print('You lose!')
########
######## From here down is essentially a main function
print('Do you want to play Simon Says or Hangman? To play simon says type 1\n')
choice = input()
if choice == '1':
  simonSays()
else:
  Hangman()

