### Problem-1: Reverse a String Without Slicing

def reverse_string(string: str) -> str:
	l = len(string)
	reversed_str = ""
	for i in range (l-1, -1, -1):
		reversed_str = reversed_str + string[i]

	return reversed_str

print(reverse_string("bongodev"))

# user_str = input("Enter a string to reverse: ")
# print (reverse_string(user_str))