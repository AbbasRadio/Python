# -*- coding: utf-8 -*-
"""
Created on Tue May 12 18:10:49 2020

@author: Dell
"""
def sort_name(demo):
    for i in range(n):
        for j in range(i+1,n):
            if demo[i][0]>demo[j][0]:
                demo[i],demo[j]=demo[j],demo[i]
    return demo

    
demo=[] 
n= int(input("Enter Number of Students : "))
for i in range(n):
    demo.append(input("Enter Student Name : "))
print(sort_name(demo))