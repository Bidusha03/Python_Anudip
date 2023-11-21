'''How to find the mean of every NumPy array in the given list?
Input:
list = [
np.array([3, 2, 8, 9]),
np.array([4, 12, 34, 25, 78]),
np.array([23, 12, 67])
]'''

import numpy as np      #Import the NumPy library use alias np
list=[np.array([3,2,8,9]),np.array([4,12,34,25,78]),np.array([23,12,67])]  #Create a list of NumPy arrays

mean_list=[]    #assign a blank list
# Use a for loop to iterate through each array in the list 
for i in list:
    mean=np.mean(i)     #calculate mean
    mean_list.append(mean)    #append the mean value

print("Mean value of 3 given array in a list : ",mean_list)  #print the result

''' Output :
Mean value of 3 given array in a list :  [5.5, 30.6, 34.0]
'''
