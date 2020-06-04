# Numpy 1D, 2D, 3D, 4D array
from numpy import *

#1D
# arr = array([1,2,3,4,5])
# print(type(arr))
# print(arr.dtype)
# print(arr)

#------------------------------------------------------------------------

#1 Array
#2 Linspace
#3 Logspace
#4 Arange
#5 zeros
#6 ones

#------------------------------------------------------------------------
#2 Linspace #divide default(50)

# arr = linspace(0,10,4) # 0 to 10 ,4 equal parts
# print(arr)

#------------------------------------------------------------------------
#3 Logspace

# arr = logspace(1,40,5) # 10^1 to 10^40 / 5
# print(arr)

#------------------------------------------------------------------------
#4 Arange

# arr = arange(1,15,2) #1 to 14 , 2 jumps
# print(arr)

#------------------------------------------------------------------------
#5 Zeros and ones

# arr = ones(5,int)
# print(arr)

#------------------------------------------------------------------------

# arr = array([1,2,3,4,5])
# arr2 = array([6,7,8,9,10])
# # arr3 = arr + arr2 #vetcorized operation(working on index without index)
# # print(arr3)
# print(concatenate([arr,arr2]))

#------------------------------------------------------------------------

# angle = array([0,30,45,60,90])
# angle = angle * 3.14/180
# print(sin(angle))
# print(cos(angle))
# print(tan(angle))

#------------------------------------------------------------------------

# arr = array([9,4,6,2,5,4,0,0,7,8])
# print(arr**2)
# print(sqrt(arr))
# print(sum(arr))
# print(min(arr))
# print(max(arr))
# print(len(arr))
# print(sort(arr))

#------------------------------------------------------------------------

# arr = array([1,2,3,4,5,65,67,54])
# arr1 = arr
# print(id(arr)) # base address
# print(id(arr1)) # base address
# arr1[3] = 100
# print(arr)
# print(arr1)

#------------------------------------------------------------------------

# arr1 = [1,2,3,4,5]
# arr2 = arr1.copy() # deep copy
# # arr2 = arr1 # shalow copy
# arr1[1] = 100
# print(arr1)
# print(arr2)
# print(id(arr1))
# print(id(arr2))

#types of copy

#1 Shallow copy (change in one list affects other list, same id of both list)

# arr2 = arr1
# #or
# arr2 = arr1.view()

#2 Deep copy (change in one does not reflect on other list, diff id)

# arr2 = arr1.copy()

#------------------------------------------------------------------------

# arr1 = array([[1,2,3],[4,5,6],[7,8,9]])
# # print(arr1)
# for i in range(3):
#     for j in range(3):
#         print(arr1[i][j],end=' ')
#     print()

#------------------------------------------------------------------------

# arr1 = array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# print(arr1.dtype) # Data type
# print(arr1.ndim) # Dimension
# print(arr1.shape) # 3X3
# print(arr1.size) #Size
# arr2  = arr1.flatten() #2D to 1D
# print(arr2)
# arr3 = arr2.reshape(3,4) # 3X4
# arr4 = arr2.reshape(6,2) # 6X2
# arr5 = array([[1,2,3],[4,5,6],[7,8,9]])
# m = matrix('1 2 3;4 5 6;7 8 9')
# m1 = matrix('1 2 3;4 5 6;7 8 9')
# print(m)
# print(diagonal(m))
# print(m.min())
# print(m.max())
# print(m.dot(2))

# m2 = m1 * m # Vectorized oprations
# print(m2)

#------------------------------------------------------------------------