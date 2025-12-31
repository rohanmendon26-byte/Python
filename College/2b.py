def bin2dec(val):
    return int(val,2)

def oct2hex(val):
    dval=int(val,8)
    return hex(dval)

try:
    num1=input("Enter a binary number:")
    print(bin2dec(num1))

except ValueError:
    print("Invalid literal in input with base 2")

try:
    num2=input("Enter a octal number:")
    print(oct2hex(num2))

except ValueError:
    print("Invalid literal in input with base 2")

