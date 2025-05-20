### Problem-2: Count Vowels in a Sentence

def count_vowels(string: str) -> int:
	vowels: list[str] = ["a", "e", "i", "o", "u"]
	cnt: int = 0

	for ch in string:
		if ch.lower() in vowels:
			cnt = cnt + 1
	
	return cnt

print(count_vowels("Data Science is awesome"))

user_str = input("Enter a string to count vowels from: ")
print (count_vowels(user_str))