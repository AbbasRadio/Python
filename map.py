# Map (works on each element of collection)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

newList = list(map((lambda a: a ** 2), numbers))

print(newList)