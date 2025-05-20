### Problem-5: Flatten a Nested List

def flatten_array(arr):
	for elem in arr:
		if isinstance(elem, list):
			yield from flatten_array(elem)
		else:
			yield elem

nested_arr = [1, [2, 3], [4, [5]]]
flat_arr = list(flatten_array(nested_arr))

print(flat_arr)