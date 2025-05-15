'''
Problem-13: Compare the two dictionaries and find the common items based on KEYs of the dictionaries
	dict1 = {'age': 13, 'id': 12, 'address': 'Banani', 'course': 'Python'}

	dict2 = {'address': 'Rupnagar', 'id': 25, 'course': 'MERN'}
'''

dict1 = {'age': 13, 'id': 12, 'address': 'Banani', 'course': 'Python'}
dict2 = {'address': 'Rupnagar', 'id': 25, 'course': 'MERN'}

def common_by_keys(dict1: dict, dict2: dict) -> dict:
    common_keys: str = dict1.keys() & dict2.keys()
    common_items: dict = {}
    
    for key in common_keys:
        common_items[key] = list(set([dict1[key], dict2[key]]))
    
    return common_items

print(common_by_keys(dict1, dict2))