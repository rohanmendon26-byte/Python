num=input("Enter a value")
if(num==num[::-1]):
    print("pallindrome")
else:
    print("not pallindrome")

for i in range(10):
    if(num.count(str(i))>0):
        print(f'{str(i)} appears {num.count(str(i))} timesṇ')