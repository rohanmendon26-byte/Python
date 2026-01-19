def BintoDex(val):
    return int(val,2)
def OcttoHex(val):
    dval=int(val,8)
    return hex(dval)

try:
    val1=input("Enter a binary number")
    print(BintoDex(val1))
except ValueError:
    print("Invalid literal in input with base 2")

try:
    val2=input("Enter a octal number")
    print(OcttoHex(val2))
except ValueError:
    print("Illegal literal in input with base 8")