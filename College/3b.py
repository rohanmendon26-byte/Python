from difflib import SequenceMatcher

str1=input("Enter a string 1:")
str2=input("Enter a string 2:")

sim=SequenceMatcher(None,str1,str2).ratio()

print(f"Difference between {str1} and {str2} is {sim}")