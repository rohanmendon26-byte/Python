import matplotlib.pyplot as plt
age_men=[25,11,68,18,27,28,15,43,58,63,43,65,51,36,33,35,49,58]
age_women=[48,57,59,25,19,37,18,56,22,25,56,25,14,49,53,45,46,19,28,70,31]
plt.figure(figsize=(6,6))
bins=[10,20,30,40,50,60,70]
plt.hist([age_men,age_women],bins=bins,color=['blue','orange'],rwidth=0.5,label=['men','women'])
plt.xlabel('Age of people',fontsize=20)
plt.ylabel('Number of people',fontsize=20)
plt.title('Age v/s Number of people',fontsize=20)
plt.show()