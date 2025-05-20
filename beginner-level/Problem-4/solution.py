### Problem-4: Check if a Word is a Palindrome

def is_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print("The string is " + ("not " if not is_palindrome("Madam") else "") + "a Palindrom")

# user_str = input("Enter a string to check for palindrom: ")
# print("The string is " + ("not " if not is_palindrome(user_str) else "") + "a Palindrom")