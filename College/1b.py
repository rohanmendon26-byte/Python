num=input("Enter a number")

if num==num[::-1]:
    print("pallindrome")
else:
    print("Not pallindrome")

for i in range(10):
    if num.count(str(i)):
        print(f"{str(i)} appears {num.count(str(i))} times")