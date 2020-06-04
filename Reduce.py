# Reduce (reduce list to one value)

from functools import reduce
numbers = (1,2,3,4,5)
# numbers = [1,2,3,4,5]
print(reduce((lambda a,b: a+b),numbers))