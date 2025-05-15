### Problem-4: Write a program to find the index of 7

from typing import List


def findIndexOf(val: int, arr: List[int]) -> None:
	if val in arr:
		idx = arr.index(val)
		print(f"Index of {val} is {idx}")
	else:
		print(f"{val} not found in {arr}")

numbers=[3, 5, 1, 9, 7, 2, 8 ]
findIndexOf(7, numbers)