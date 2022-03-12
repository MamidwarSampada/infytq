"""
Problem Statement
Given two positive integers. Write a python function to return the greatest common divisor of the given numbers.

Sample Input            Expected Output

14 and 35                    7

800 and 2800                400
"""
#lex_auth_0127136213490565121191
import math
def find_gcd(num1,num2):
    a=math.gcd(num1,num2)
    return a
    #start writing your code here
    

num1=45
num2=9
print(find_gcd(num1,num2))
