"""
Problem Statement
Given an integer n, write a python function to return true, if it is possible to represent it as a sum of the squares of two different integers, else return false.
"""
#lex_auth_0127136357122129921205
import math
def check_squares(number):
    a=round(math.sqrt(number))
    for i in range(1,a):
        for j in range(i,a):
            if (i*i)+(j*j)==number:
                return True
    return False
    #start writing your code here


number=25
print(check_squares(number))
