# Author: Mike Sisson
# Creation Date: Aug 9, 2021
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('You are in a land full of dragons. In front of you,\nyou see two caves. In one cave, the dragon is friendly\nand will share his treasure with you. The other dragon\nis greedy and hungry, and will eat you on sight.')

def chooseCave():
  cave = ''
  while cave != '1' and cave != '2':
    print('Which cave will you go into? (1 or 2)')
    cave = input()
  return cave

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(2)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		print 'Gobbles you down in one bite!'

playAgain = 'yes'
while playAgain = 'yes' or playAgain = 'y':
	displayIntro()
	caveNumber = choosecave()
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
		print("Thanks for planing")

