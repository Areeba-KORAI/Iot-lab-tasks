sentence = input("Enter a sentence: ")

num_chars = len(sentence)
num_words = len(sentence.split())
num_spaces = sentence.count(' ')

vowels = "aeiouAEIOU"
num_vowels = sum(1 for char in sentence if char in vowels)

num_digits = sum(1 for char in sentence if char.isdigit())

print("\n--- Sentence Analysis ---")
print(f"Number of characters: {num_chars}")
print(f"Number of words: {num_words}")
print(f"Number of vowels: {num_vowels}")
print(f"Number of spaces: {num_spaces}")
print(f"Number of digits: {num_digits}")