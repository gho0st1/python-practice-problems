'''
Problem-11: Find the most frequent character in the paragraph
	rhyme = 'Twinkle, twinkle, little star. How I wonder what you are!
'''

import string


def most_freq_char(text: str) -> str:
	char_count: dict[str, int] = {}	

	for char in text:
		c = char.lower()
		if (c in string.ascii_lowercase):  
			char_count[c] = char_count.get(c, 0) + 1
	
	return max(char_count, key=char_count.get)


rhyme = 'Twinkle, twinkle, little star. How I wonder what you are!'

print(most_freq_char(rhyme))
	
