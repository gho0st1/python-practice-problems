### Problem-3: Find Duplicates in a List

from typing import Dict


def find_duplicates(arr: list) -> list:
	dups: list = []
	counter: Dict[any, int] = {}

	for elem in arr:
		counter[elem] = counter.get(elem, 0) + 1
		if (counter[elem] > 1):
			dups.append(elem)
	
	return dups

print(find_duplicates(["ai", "ml", "python", "ml", "dl", "ai"]))