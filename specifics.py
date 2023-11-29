word = "Holbertommn"
word_first_3=word[:3]
print(f"First 3 letters: {word_first_3}")

word_last_2=word[-2:]
print(f"Last 2 letters: {word_last_2}")

x=len(word)
k=int(x/2)
middle_word=str(word[k])
print(f"Middle word: {middle_word}")