'''
### Problem-6: Capitalize First Letter of Each Word
Build a custom title formatter that capitalizes the first letter of each word without using `.title()`
'''

def pascal_case_formatter(s: str) -> str:
	formatted_string = " ".join(word[0].upper() + word[1:] for word in s.split())
	return formatted_string

print(pascal_case_formatter("python for web developers"))

# user_str = input("Enter a string to be formatted: ")
# print(pascal_case_formatter(user_str))