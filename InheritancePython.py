# class parent:
#     def first(self):
#         print("I'm a parent function")
#
# class child(parent):
#     def second(self):
#         print("I'm a child function")
#
# c1=child()
# c1.first()
# c1.second()
#==================================================================================================================
# class teacher1:
#     def show1(self):
#         self.teacher="Vijay Sir"
#         self.m1=70
#     def display1(self):
#         print(self.teacher)
#         print(self.m1)
#
# class teacher2:
#     def show2(self):
#         self.teacher="Ajay Sir"
#         self.mm1=50
#     def display2(self):
#         print(self.teacher)
#         print(self.m1)
#
# class student(teacher1,teacher2):
#     pass
# d1=student()
# d1.show1()
# print(d1.teacher,d1.m1)
#==================================================================================================================
# class first:
#     a=100
#     def show1(self):
#         print(self.a)
# class second(first):
#     b=200
#     def show2(self):
#         print(self.b)
# class third(second):
#     c=300
#     def show3(self):
#         print(self.c)
# d1=third()
# d1.show1()
# d1.show2()
# d1.show3()
#==================================================================================================================
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def putdata(self):
        print("M1 =",self.m1)
        print("M2 =",self.m2)
    def __add__(self, other):
        x1=self.m1+other.m1
        x2=self.m2+other.m2
        s3=student(x1,x2)
        return (s3)
    def __sub__(self, other):
        x1=self.m1-other.m1
        x2=self.m2-other.m2
        s3=student(x1,x2)
        return (s3)
    def __mul__(self, other):
        x1=self.m1*other.m1
        x2=self.m2*other.m2
        s3=student(x1,x2)
        return (s3)
    def __truediv__(self, other):
        x1=self.m1/other.m1
        x2=self.m2/other.m2
        s3=student(x1,x2)
        return (s3)
    def __str__(self):
        return("M1 ={}, M2 ={}".format(self.m1,self.m2))
s3=s1/s2
s1=student(10,20)
s2=student(30,40)
print(s3)
