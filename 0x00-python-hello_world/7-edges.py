#!/usr/bin/python3
word = "Holberton"
word_last_2, word_first_3 = word[-2:], word[:3]
middle_word = word[1:len(word) - 1]

print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
