# class computer:
#     def display(self):
#         print("I'm A Web Developer")
#
# d1=computer()
# print(type(d1))
# d1.display();
# computer.display(d1)

# class demo:
#     # if we want to call a contructor in a class then wee need to use __init_(self) function
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#     def put(self):
#         print("name :",self.name)
#         print("age :",self.age)
#         print("salary :",self.salary)
# # when we need to set the value in constructor we use below line
# d1=demo("Abbas",20,1200000)
# demo.put(d1)

# ============================================================================================

# Class Method : -
class student:
    school = "MLSU"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return ((self.m1+self.m2+self.m3)//3)
    # to access a class variable then we need to specify the below line to mention that this is a class method
    @classmethod
    def info(cls): # using cls in parenthesis defines that the variable to be used is a class variable
        return(cls.school)
s1 = student(56,98,79)
print(s1.avg())
print(student.info())