####################################################################
#  Date: 07/18/2020
#  Author: ZL Hu
#  Read 1000 digits of Pi, and calculate the distribution of each number (0-9)
#  The pi is in pi_1000_digits.txt
#  Higher accuracy value of pi can be found: https://pi.911cha.com/
####################################################################

import numpy as np 
from matplotlib import pyplot as plt 
import os

f = open('pi_1000_digits.txt','r')

result = str()

for line in f.readlines():
    # line = line.strip()
    result += line
    # print(line)
ans = np.zeros(10)
print(result)
for i in range(10):
    ans[i] = result.count(str(i))
print(ans)
x = np.arange(10)
print(x)
plt.bar(x, ans)
plt.style.use('ggplot')
# use tick
plt.xticks(ticks = x, labels = x)
plt.show()
f.close()