import matplotlib.pyplot as plt
import numpy as np

# You may wish to add some code here.

def geometric() : 
  # Add code to generate a geometric random variable with 
  # p=0.5 here.
  
n, ssum = 0, 0 
indices, average = np.zeros(200), np.zeros(200)
for i in range(200) : 
  ssum = ssum + 2**geometric()
  n = n + 1
  # Add code to calculate average from n random variables here and to thus 
  # set the elements of the list called average.  Also write code to set the elements 
  # of the list called indices. 
  
# This will plot the graph for the data
plt.plot( indices, average, '.' )
plt.xlabel("Number of random variables")
plt.ylabel("Sample mean")
plt.savefig("average_variable.png")
