#Q1
import numpy as np
arr = np.array([1, 2, 3, 6, 4, 5])
rev=arr[::-1]
print('reverse array:',rev)


#Q2
import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[1, 2], [3, 4]])
if np.array_equal(arr1, arr2):
	print("Equal")
else:
	print("Not Equal")

#Q3
#from statistics import mode
#arr=[1,2,3,4,5,1,2,1,1,1]
#res=mode(arr)
#print('Mode:',res)

import numpy as np 
# create array 
x = np.array([1,2,3,4,5,1,2,1,1,1]) 
print("Original array:") 
print(x) 
print("Most frequent value in the above array:") 
print(np.bincount(x).argmax())


#from statistics import mode
#arr2=[1, 1, 1, 2, 3, 4, 2, 4, 3, 3]
#re=mode(arr2)
#print('Mode is :',re)
import numpy as np 
# create array 
x = np.array([1,2,3,4,5,1,2,1,1,1]) 
print("Original array:") 
print(x) 
print("Most frequent value in the above array:") 
print(np.bincount(x).argmax())


#Q4
import numpy as np


gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]')

sum1 = np.sum(gfg)
print('sum of all element:',sum1)
row_sum = np.sum(gfg, axis=1)
print('sum of row:',row_sum)

col = np.sum(gfg, axis=0)
print("sum of column:",col)


