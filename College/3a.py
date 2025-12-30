import string

sentence = input("Enter a sentence: ")

# Count words
wordList = sentence.strip().split()
print(f"The sentence has {len(wordList)} words\n")

digit_count = uppercase_count = lowercase_count = 0

# Loop through each character
for character in sentence:
    if character in string.digits:
        digit_count += 1
    elif character in string.ascii_uppercase:
        uppercase_count += 1
    elif character in string.ascii_lowercase:
        lowercase_count += 1

# Display results
print(f"This sentence has {digit_count} digits")
print(f"{uppercase_count} upper case letters")
print(f"{lowercase_count} lower case letters")
