### Problem-9: Sum of Digits of an Integer

def sum_of_digits(n: int) -> int:
	sum = 0
	while (n):
		sum = sum + (n % 10)
		n = n // 10

	return sum

number = 9875
# number = int(input("Enter a number: "))
print(f"Sum of digits of {number} is {sum_of_digits(number)}")