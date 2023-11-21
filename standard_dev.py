''' Compute the standard deviation of the NumPy array
Input: arr1 = [20, 2, 7, 1, 34]'''


import numpy as np      #Import the NumPy library use alias np
arr1=np.array([20,2,7,1,34])
Standard_dev=np.std(arr1)   #calculate standard deviation using std()
print("standard Deviation:",Standard_dev)   #print the output

'''Output :
standard Deviation: 12.576167937809991
'''
