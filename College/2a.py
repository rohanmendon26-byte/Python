def fn(n):
    if n<=2:
        return n-1
    else:
        return fn(n-1)+fn(n-2)
    
try:
 num=int(input("enter a  value:"))
 
 if num>0:
    print(f'fn({num})={fn(num)}')
 else:
    print("Enter number greater than zero")

except ValueError:
   print("Try withh numeric value")

