m1=int(input("Enter the marks 1:"))
m2=int(input("Enter the marks 2:"))
m3=int(input("Enter the marks 3:"))

best_of_two=sorted([m1,m2,m3],reverse=True)[:2]
average_best_of_two=sum(best_of_two)/2

print("the best of two out of three marks is:",average_best_of_two)