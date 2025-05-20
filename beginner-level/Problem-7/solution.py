'''
### Problem-7: Find Missing Number in a Sequence
You received log files indexed from 1 to n. One log is missing. Find it.
'''

def find_missing_number(numbers: list[int]) -> int:
	sum_val = sum(numbers)
	l = len(numbers) + 1

	missing = ((l * (l + 1)) // 2) - sum_val
	return missing

print(find_missing_number([1, 2, 4, 5]))
