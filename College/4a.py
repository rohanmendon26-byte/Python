import matplotlib.pyplot as plt
categories=["0-10","10-20","20-30","30-40","40-50"]
values=[55,48,25,68,90]
plt.bar(categories,values,color="skyblue")
plt.xlabel("Overs")
plt.ylabel("Runs")
plt.title("Runs scored in odi match")
plt.show()