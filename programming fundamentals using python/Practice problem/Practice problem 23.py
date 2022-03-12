"""
Problem Statement
Write a python function to find out whether a number is divisible by the sum of its digits. If so return True,else return False.

Sample Input               Expected Output

42                            True

66                            False
"""
#lex_auth_0127136251125350401190

def divisible_by_sum(number):
    s=str(number)
    c=0
    for i in s:
        c+=int(i)
    if number%c==0:
        return True
    return False
        
    #start writing your code here

    
number=42
print(divisible_by_sum(number))
