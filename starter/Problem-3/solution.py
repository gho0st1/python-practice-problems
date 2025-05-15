### Problem-3: Write a function that takes 2 numbers as arguments (age of two brothers) and find who is elder

def printElderBrother(firstBro, secondBro):
	if (firstBro == secondBro):
		print("They are the same age")
	else:
		print(("First Bro" if firstBro > secondBro else "Second Bro") + " is the older brother")

printElderBrother(50, 100)

# x = int, input("Enter the age of First Bro: ")
# y = int, input("Enter the age of Sedond Bro: ")
# printElderBrother(x, y)