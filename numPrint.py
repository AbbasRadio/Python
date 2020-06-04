#enter the element in a list and print only numeric value
list1 = ["Abbas","Hello",56,687,"Dishant",56.54,8793.6354,'Hi']
#print(list1)
for data in list1:
    if str(data).isnumeric():
        print(data)
    if isinstance(data,float):
        print(data)