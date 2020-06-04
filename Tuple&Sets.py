#Tuple: unmutable, dissimilar elements, can contain tuple or list (nested)

# a = (1,2,3,'one','two')
# print(a)

#------------------------------------------------------------------------

#Sets: no-index, same values will apperar once, mutable,un-ordered dissimilar collection, no nested sets

# a = {1,1,22,23,3,3,3,3,3,6,5}
# # print(a)
#
# # cannot print with index
#
# for item in a:
#     print(item)

#------------------------------------------------------------------------

# s1 = {1,2,3,4,5}
#
# s2 = {5,6,7,8,1}

# print(s1.union(s2)) # UNION
# #or
# print(s1|s2)

# print(s1.intersection(s2)) # Intersection
# #or
# print(s1&s2)

# print(s1.difference(s2)) # Differnce
# #or
# print(s1-s2)

# print(s1-s2|s2-s1) #symmetric differnce
# #or
# print((s1|s2)-(s1&s2))

#------------------------------------------------------------------------