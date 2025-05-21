### Problem-2: Group Anagrams Together

def grouped_list(words: list[str]) -> list[list[str]]:
	mapped_words: dict[str, list[str]] = {}

	for word in words:
		sorted_word = "".join(sorted(word))
		if sorted_word not in mapped_words:
			mapped_words[sorted_word] = []

		mapped_words[sorted_word].append(word)

	return list(mapped_words.values())

tags = ["bat", "tab", "cat", "act"]

print(f"Grouped values are: {grouped_list(tags)}") 