'''
Problem-14: Sort the list in DESCENDING order and find the subtraction of maximum and minimum numbers.
	list_1 = [4, 9, 8, 7, 5, 2, 13]
'''

list_1 = [4, 9, 8, 7, 5, 2, 13]
list_1.sort(reverse=True)

print(list_1[0] - list_1[-1])