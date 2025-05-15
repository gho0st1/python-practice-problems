'''
Problem-12: Find the common items between the lists and make SUM of the new list items which are common between the lists.
	list1 = [3, 5, 7, 4, 8, 8]

	list2 = [4, 9, 8, 7, 1, 1, 13, 8, 8]
'''


from collections import Counter

list1 = [3, 5, 7, 4, 8, 8]

list2 = [4, 9, 8, 7, 1, 1, 13, 8, 8]

c1 = Counter(list1)
c2 = Counter(list2)

intersected_list = list((c1 & c2).elements())
print(sum(intersected_list))  