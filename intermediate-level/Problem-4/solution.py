### Problem-4: Validate Email Format

import re


def is_valid_email(email: str) -> bool:
	pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
	return re.match(pattern, email)

user_email = "test@domain.com"
# user_email = input("Enter your email: ")

print(f"'{user_email}' is{"" if is_valid_email(user_email) else " not"} a valid email")
