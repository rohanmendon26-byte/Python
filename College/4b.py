import matplotlib.pyplot as plt
day=[1,2,3,4,5,6]
num=[48,12,28,38,20,36]
plt.xlabel("Days",fontsize=15)
plt.ylabel("Number of cases",fontsize=15)
plt.title("Number of cases reported",fontsize=15)
plt.scatter(day,num,s=250,color=['g','b','r','m','b','g'])
plt.show()