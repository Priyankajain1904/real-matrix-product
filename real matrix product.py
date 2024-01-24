'''Problem Statement 1: Write a Python program to multiply a 𝑀 × 𝑁 matrix by 𝑁 × 𝐴 matrix and
create a real matrix product.
Example:
Input:
Enter value M: 5
Enter value N: 3
Enter value A: 2
'''

import numpy as np
a=np.random.random((5,3))
print ("First Array is: ",a)
b=np.random.random((3,2))
print("Second Array is: ",b)
c=np.dot(a,b)
print("Real Matrix Array is: ",c)
