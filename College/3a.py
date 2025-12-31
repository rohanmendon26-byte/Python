import string
sentence=input("Enter a sentece:")
wordlist=sentence.strip().split()

digit_count=lowercase_count=uppercase_count=0

for character in sentence:
    if character in string.digits:
        digit_count+=1
    elif character in string.ascii_uppercase:
        uppercase_count+=1
    elif character in string.ascii_lowercase:
        lowercase_count+=1

print(f"The sentence has {digit_count} digits")
print(f"{lowercase_count} lower case letters")
print(f"{uppercase_count} upper case letters")