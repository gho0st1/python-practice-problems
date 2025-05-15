### Problem-1: Write a program to find the length of the variable name
# Variable, name="Hello there"

def printLenOfStaticVariable(str):
	print(len(str))

def printLenOfInputVariable():
	str = input()
	print(len(str))

printLenOfInputVariable()
printLenOfStaticVariable("Hello Sakib!")