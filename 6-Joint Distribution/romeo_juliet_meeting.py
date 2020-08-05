#########################################################################
# Authour: ZL Hu
# Date: 08/05/2020
# Description: Romeo and Juliet meeting problem
#  Romeo and Juliet decide to arrive and meet sometime betwen 7 and 8 am. 
#  Whoever arrives first will wait for 20 minutes for the other person.
#  If the other person doesn't turn up inside 20 minutes then the person waiting will leave
#  What is the probability that Romeo and Juliet can meet?
#  Assuming their arrival time is uniformly distributed.
#########################################################################


from matplotlib import pyplot as plt 
import numpy as np 
import random

iterations = 10000

x = np.arange(iterations) # x=[1,2,3,...10000]
y = np.zeros(iterations) # y=[0,0,...0] 10000 zeros
chance = 0
for i in range(iterations): # conduct experiment 10000 times
    x_arrival = random.uniform(0,60)
    y_arrival = random.uniform(0, 60)
    if abs(x_arrival-y_arrival) <= 20: # their arrival time is less than 10 minutes apart
        chance += 1 # the successful chance increases by 1
    y[i]=chance/(i+1)
print(sum(y[-100:])/100)
plt.xlabel('Times of experiments')
plt.ylabel('Chances of successful meeting')
plt.scatter(x,y,s=1, color='g',marker='o', alpha=0.5)
plt.xlim(0,iterations)
plt.ylim(0,1)
plt.title("Chances of meeting in 20 minutes")
plt.show()
