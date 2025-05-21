### Problem-9: Password Validator (Security Utility)

import re

def validate_password(password: str) -> bool:
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

password = "Secure123!"
# password = input("Enter your password: ")

print(f"The password is{"" if validate_password(password) else " not"} valid.")
