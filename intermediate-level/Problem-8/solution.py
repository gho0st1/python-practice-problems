### Problem-8: Command-line Calculator

def calculate(expression: str) -> int:
	parsed_list = expression.split()
	command = parsed_list[0].lower()
	numbers = list(map(int, parsed_list[1:]))

	if command == 'add':
		return sum(numbers)
	elif command == 'subtract':
		return numbers[0] - numbers[1]
	elif command == 'multiply':
		return numbers[0] * numbers[1]
	else:
		return numbers[0] / numbers[1]
	
expression = 'add 5 7'
expression = input("Enter an expression: ")

print(f"The result is: {calculate(expression)}")