############################################################################
# Author: ZL Hu
# Date: 08/05/2020
# Description: Three door problem / Monty Hall Problem
#   You are given an opportunity to select one closed door of three, behind one of which there is a car. 
#   The other two doors hide goats. Once you have made your selection, the host Monty Hall, 
#   who knows where the car is, will open one of the remaining doors, revealing a door that does not contain the car. 
#   He then asks you if you would like to switch your selection to the other unopened door, or stay with your original choice. 
# Strategy analysis: 
#  switch door: you will win a car if your initial guess is incorrect (P = 2/3)
#  not switch: you will win a car only if your initial guess is correct (P = 1/3)


from matplotlib import pyplot as plt 
import numpy as np
from random import randint

iterations=10000 # number of tests
x = np.arange(iterations)
y = np.zeros(iterations)
ans = 0
for i in range(iterations):
    result = randint(1,3) # the car is randomly distributed behind three doors
    guess = randint(1,3) # i randomly guess where the car is
    if result != guess: # if I guess wrong, and change doors
        ans+= 1
    y[i]=ans/(i+1)
plt.figure(1)
plt.title("Changing doors")
plt.xlabel("Number of times played")
plt.ylabel("Chances to win a car if changing doors")
plt.xlim(0,iterations)  # set x axis limits
plt.ylim(0,1)   # set y axis limits
plt.scatter(x,y, s=1, c='g',marker='o',alpha=0.5)
plt.show()
plt.figure(2)
plt.title("Changing doors")
plt.xlabel("Number of times played")
plt.ylabel("Chances to win a car is changing doors")
plt.xlim(iterations-100, iterations)
plt.ylim(0.64, 0.7)
plt.scatter(x,y, s=1, c='g', marker = 'o', alpha=0.5)
static_x = np.arange(iterations - 100, iterations)
static_y = np.ones(100)*2/3
plt.plot(static_x, static_y)
plt.show()
