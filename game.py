from __future__ import print_function
import random
import os
import boards
import time

#import wordlist

hangman = ['H', 'A', 'N', 'G', 'M', 'A', 'N']

def importwordlist(file):
	with open(file, 'r') as f:
		words = filter(None, f.read().split('\n'))
		return words

class gameboard(object):

	def __init__(self, difficulty, wordlist):
		self.difficulty = difficulty
		self.words = wordlist
		hangmanpics = ''

	def choosedifficulty(self, difficulty):	
		if self.difficulty == "easy":
			hangmanpics = boards.easy
			return hangmanpics

		elif self.difficulty == "hard":
			hangmanpics = boards.hard
			return hangmanpics
	
	def displaygameboard(self, hangmanpics, missedLetters, correctLetters, secretWord):
		print(hangmanpics[len(missedLetters)])
		print()
		
		print("Missed Letters: ", end=' ')
		for letter in missedLetters:
			print(letter, end = ' ')
		print()
		
		blanks = '_' * len(secretWord)
		
		for i in range(len(secretWord)):
			#changes the guessed blanks
			if secretWord[i] in correctLetters:
				blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
			
		for letter in blanks:
			print(letter, end=' ')
		
		print()

#    print hangmanpics
	
class GameEngine(object):
	#takes the user input and runs the functions
	def __init__(self, board):
		self.gameboard = board
		self.missedLetters = ''
		self.correctLetters = ''
		self.gameisdone = False
	
	def getRandomWord(self, wordList):
		wordindex = random.randint(0, len(wordList)-1)
		return wordList[wordindex]
	
	def getGuess(self, alreadyGuessed):
		while True:
			print('Guess a letter...')
			guess = raw_input('> ').lower()
			if len(guess) != 1:
				print("Please enter just a single letter")
			elif guess in alreadyGuessed:
				print("You have already guessed that letter, pick another")
			elif guess not in 'abcdefghijklmnopqrstuvwxyz':
				print("I said, LETTER!")
			else:
				return guess
	
	def playagain(self):
		print('Do you want to play again? (yes or no)')
		return raw_input('> ').lower().startswith('y')
	
	def oneguess(self, secretWord):
		
		time.sleep(0.5)
		self.hangmanpics = self.gameboard.choosedifficulty(self.gameboard.difficulty)
		self.gameboard.displaygameboard(self.hangmanpics, self.missedLetters, self.correctLetters, secretWord)
		guess = self.getGuess(self.missedLetters + self.correctLetters)
		if guess in secretWord:
			self.correctLetters = self.correctLetters + guess
			
			foundAllLetters = True
			for i in range(len(secretWord)):
				if secretWord[i] not in self.correctLetters:
					foundAllLetters = False
					break
			if foundAllLetters:
				print("Yes! The secret word is %s! You have won with only %d incorrect guesses" %(secretWord, len(self.missedLetters)))
				self.gameisdone = True
		else:
			self.missedLetters = self.missedLetters + guess
			if len(self.missedLetters) >= len(self.hangmanpics) - 1:
				self.gameboard.displaygameboard(self.hangmanpics, self.missedLetters, self.correctLetters, secretWord)
				print("Sorry, you have run out of guesses! You have lost after %d correct guesses, %d incorrect guesses. The word was %s" %(len(self.correctLetters), len(self.missedLetters), secretWord))
				self.gameisdone = True
		
		
				
class game(object):
	def __init__(self, game):
		self.game = game
	
	def play(self):
		secretWord = mygame.getRandomWord(words)
		while True:
			mygame.oneguess(secretWord)
			if mygame.gameisdone:
				if mygame.playagain():
					myboard = gameboard(raw_input('Select Diffculty > '), words)
					mygame = GameEngine(myboard)
					secretWord = mygame.getRandomWord(words)
					mygame.missedLetters = ''
					mygame.correctLetters = ''
					mygame.gameisdone = False
				else:
					quit()
	
				
if __name__ == '__main__':
	print('\n'*10)
	for letter in hangman:
		print(letter, end=' ')
		time.sleep(0.3)
	print()
	words = importwordlist('wordlist.txt')
	myboard = gameboard(raw_input('Select Diffculty, easy or hard > ').lower(), words)
	mygame = GameEngine(myboard)
	play = game(mygame)
	play.play()