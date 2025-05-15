'''
Problem-8: Guessing game

Write a function that takes a number 1 to 9 from the user input (use input function inside a function). 
Store a number in a variable (let’s assume 6). 
- If the input value is less than the variable, print (your guess is almost there), 
- if the input value is greater than the variable, print - your guess is higher, 
- if the input value and variable are equals, print - Your Guess Is Correct!
'''

import random

def guessingGame(target: int) -> None:
	guess = -1
	while (guess != target):
		guess = int(input("Enter your guess: "))

		if (guess < target):
			print("Your guess is almost there")
		elif (guess > target):
			print("Your guess is higher")
		else:
			print("Your guess is correct")

guessingGame(random.randint(1, 10))