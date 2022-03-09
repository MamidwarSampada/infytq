"""
Problem Statement
Write a python function which accepts three numbers and returns True if
a. one of the three numbers is "close" to any one of the other numbers (differing from a number by at most 1), and
b.Number that is left out is "far", differing from both other values by 2 or more.
Return false if the above mentioned conditions are not satisfied.

Sample Input             Expected Output

4,1,3                      True

5,6,7                      False
"""
#lex_auth_0127136008767324161169
import math
def close_number(num1,num2,num3):
    if num1+1==num2 and num2+1==num3:
        return False
    elif math.fabs(num1-num2)>1 and math.fabs(num1-num3)>1 and math.fabs(num2-num3)>1:
        return False
    elif num1==num3:
        return False
    return True
    #start writing your code here
    
print(close_number(5,4,2))
