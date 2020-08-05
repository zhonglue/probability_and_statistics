##############################################
#  Date: 07/24/2020
#  Author: ZL Hu
#   Compute the correlation matrix from the iqsize.txt
#   iqsize.txt downloaded from PSU website: https://online.stat.psu.edu/onlinecourses/sites/stat501/files/data/iqsize.txt
##############################################

from matplotlib import pyplot as plt 
import numpy as np 
import pandas as pd 
import seaborn as sns 


data = pd.read_csv('iqsize.txt', sep = '\t')
print(data)

corr_mat = data.corr()
print(corr_mat)
# plt.matshow(corr_mat)
# plt.style.use('seaborn')
# plt.show()

# use seaborn to draw more appealing images

# I don't even need to specifically give the chars/anotations for x ticks
sns.heatmap(corr_mat, square = True, linewidths = .5, annot = True, cmap = 'GnBu')
plt.show()

# plot IQ vs Weight

height = data[['Height']]
weight = data[['Weight']]

plt.scatter(height, weight)
plt.style.use('seaborn')

plt.xlabel('IQ')
plt.ylabel('Weight')
plt.show()