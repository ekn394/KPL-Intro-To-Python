# Number Stumper - Python Edition
# Evan Nordquist May 20, 2020
# Knock off of the board game "Mastermind" which was itself a rip off of something else. 

#Import Modules
import random


#Setup Global Variables and Constants
comp_guess = []
human_guess = []
number_right = []
number_in_wrong_place = []
NUM_DIGITS = 3
MAX_GUESS = 10


# Helper Functions
def getDifficulty():
	global NUM_DIGITS
	diffResponce = None
	while diffResponce not in "1 2 3".split():
		print("Select a difficulty level (1 - Easy, 2 - Medium, 3 - Hard)")
		diffResponce = input()
	if diffResponce == "1":
		NUM_DIGITS = 2
		print("Difficulty Level 1:")
	elif diffResponce == "2":
		NUM_DIGITS = 3
		print("Difficulty Level 2:")
	elif diffResponce == "3":
		NUM_DIGITS = 4
		print("Difficulty Level 3:")
	else:
		print("Something has gone wrong with setting the difficulty")


def intro():
	print("I am thinking of a %s-digit number (without duplicates). Try to guess what it is." % (NUM_DIGITS)) 
	print("I have thought up a number.  You have %s guesses to get it." % (MAX_GUESS))


def resetAllVariables():
	global comp_guess
	comp_guess = []
	resetTurnVariables()


def resetTurnVariables():
	global number_right, number_in_wrong_place, human_guess
	number_right = []
	number_in_wrong_place = []
	human_guess = []


def compGetNumber():
	while len(comp_guess) <NUM_DIGITS:
		nextOne = random.randint(0,9)
		if nextOne not in comp_guess:
			comp_guess.append(nextOne)


def testHumanGuess():
	answer = ''
	while len(answer) != NUM_DIGITS:
		print("Take a %s-digit guess" % (NUM_DIGITS))
		answer = input()
	
	for character in answer:
		human_guess.append(int(character))


def getClues(guess, secretNum):
	alreadyChecked = []
	if guess == secretNum: # toggle for house rules about duplicate guesses
		return "You got my number" 
	for i in range(len(guess)):
		if guess[i] in alreadyChecked:  # toggle for house rules about duplicate guesses
			continue # toggle for house rules about duplicate guesses
		alreadyChecked.append(guess[i]) # toggle for house rules about duplicate guesses
		if guess[i] == secretNum[i]:
			number_right.append(guess[i])
		elif guess[i] in secretNum:
			number_in_wrong_place.append(guess[i])
	print("""Number Right: %s \nNumber in Wrong Place: %s """ %(len(number_right), len(number_in_wrong_place)))
	print("")


# Main Game Loop
while True:
	getDifficulty()
	intro()
	resetAllVariables()
	compGetNumber()
	#print(comp_guess) # Toggle this for cheat mode
	guesses_taken = 0
	while guesses_taken <= MAX_GUESS:
		resetTurnVariables()
		testHumanGuess()
		guesses_taken += 1
		getClues(human_guess, comp_guess)
		if human_guess == comp_guess:
			print("You got my number!")
			break
		if guesses_taken == MAX_GUESS:
			print("Sorry you are out of guesses")
			print("The correct number was %s" %(comp_guess))
			break
		print("You have %s guesses left" %(MAX_GUESS - guesses_taken))
	print("Do you want to play again? (yes or no)")
	if not input().lower().startswith('y'):
		break
