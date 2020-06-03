
#faulty calculator 
import sys
from math import *
def add(a,b):
    c=a+b
    return c**3
def sub(a,b):
    c=a-b
    return c-500
def div(a,b):
    c=a//b
    return sqrt(c**7)
def mul(a,b):
    c=a*b
    return c*150
pass
while 1:
    print("\n\n1. Addition\n2. Subtraction\n3. Division\n4. Multiplication")
    print("5. Exit")
    print("Enter Your Choice :")
    check = int(input())
    if check==1:
        print("Enter 2 Values =>")
        a,b = int(input("Enter 1 Number :")),int(input("Enter 2 Number :"))
        print("Addition is : ",add(a,b))
    elif check==2:
        print("Enter 2 Values =>")
        a,b = int(input("Enter 1 Number :")),int(input("Enter 2 Number :"))
        print("Subtraction is : ",sub(a,b))
    elif check==3:
        print("Enter 2 Values =>")
        a,b = int(input("Enter 1 Number :")),int(input("Enter 2 Number :"))
        print("Division is : ",div(a,b))
    elif check==4:
        print("Enter 2 Values =>")
        a,b = int(input("Enter 1 Number :")),int(input("Enter 2 Number :"))
        print("Multiplication is : ",mul(a,b))
    else:
        sys.exit()