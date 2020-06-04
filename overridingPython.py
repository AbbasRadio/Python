# class parent1():
#     classVar = "Class Variable 1"
#     def show(self):
#         self.classVar = "Instance of Class Variable 1"
#         print("Show of Parent 1")
#
# class parent2(parent1):
#     classVar = "Class Variable 2"
#     def show(self):
#         self.classVar = "Instance of Class Variable 2"
#         print("Show of Parent 2")
# p1=parent2()
# print(p1.classVar)

class A():
    classVar = "I'm in Class A Variable"
    def __init__(self):
        self.var1 = "I'm in Class A"
        self.classVar = "I'm inside Class A Scope"
        self.special = "Special"
class B(A):
    def __init__(self):
        self.var1 = "I'm in Class A"
        self.classVar = "I'm inside Class A Scope"
        super(B, self).__init__() # super() is used to jump to parent class constructor 
        # print(super(B, self).classVar)
a=A()
b=B()

print(b.special ,":" , b.var1 ,":" , b.classVar)