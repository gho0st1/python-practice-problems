### Problem-1: Longest Word in a Sentence

def longest_word(sentence: str) -> str:
	words = sentence.split()
	max_word = max(words, key=len)
	return max_word

sentence = "Machine learning is fascinating"
# sentence = input("Please enter a sentence: ")

print(f"Longest word in sentence: {longest_word(sentence)}")