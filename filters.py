#Filter (filter some elements out of multiple elemnts, used on collections)

# Even
# numbers = [1,2,3,4,5,6,7,8,9,10]
#
# def even(n): # Automatically receive each item of (one by one) numbers
#     return not n & 1 # return n (only works with filter)
#     ## or
#     #return n%2 == 0
#     ## or
#     # if not n & 1:
#     #     return n
#
# filteredList = list(filter(even,numbers))
# print(filteredList)

#------------------------------------------------------------------------

#Even With lambda

numbers = [10,9,8,7,6,5,4,3,2,1]

filteredList = list(filter(lambda n: n%2 == 0,numbers))

print(filteredList)

#------------------------------------------------------------------------