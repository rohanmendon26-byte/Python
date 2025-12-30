import matplotlib.pyplot as plt
exp_vals=[1400,600,300,410,250]
exp_labels=['Home rent','food','phone','car','other utilities']
# plt.pie(exp_vals,labels=exp_labels,shadow=True)
plt.pie(exp_vals,labels=exp_labels,shadow=True,autopct='%1.1f%%',radius=1)
# plt.pie(exp_vals,labels=exp_labels,shadow=True,autopct='%1.1f%%',radius=1,explode=[0,0,0,0.2,0.1])
# plt.pie(exp_vals,labels=exp_labels,shadow=True,autopct='%1.1f%%',radius=1,explode=[0,0,0,0.2,0.1],counterclock=False,startangle=30)
plt.show()