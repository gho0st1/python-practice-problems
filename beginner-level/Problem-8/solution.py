### Problem-8: Factorial Using Recursion

def calculate_factorial(n: int) -> int:
	if n <= 1:
		return 1
	
	return n * calculate_factorial(n - 1)

usr_in = 5
# usr_in = int(input("Enter a number: "))

print(f"Factorial of {usr_in} is {calculate_factorial(usr_in)}")
