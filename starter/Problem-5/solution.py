### Problem-5: Write a program to sort the numbers in Ascending order

from typing import List


def sortNumber(arr: List[int]) -> None:
	arr.sort()
	print(arr)

numbers=[3, 5, 1, 9, 7, 2, 8 ]
sortNumber(numbers)