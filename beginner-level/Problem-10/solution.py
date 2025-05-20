### Problem-10: Check if a Number is Prime

import math


def is_prime(n: int) -> bool:
	if (n < 3):
		return False
	
	sqr_root = int(math.sqrt(n))
	for i in range (3, sqr_root + 1, 2):
		if not (n % i):
			return False
		
	return True

number = 29
number = int(input("Enter a number: "))
print(f"""{number} is{" not" if not is_prime(number) else ""} a Prime Number""")