'''
Problem-10: The list below is the collection of the ages of people from a village. Clean up the data and store only numbers in another list.
	data_list = [13, 24, 'Karim', {'name': 'guru'}, 45, 17]
'''

data_list = [13, 24, 'Karim', {'name': 'guru'}, 45, 17]
int_list: list[int] = [x for x in data_list if isinstance(x, int)]

print(int_list)