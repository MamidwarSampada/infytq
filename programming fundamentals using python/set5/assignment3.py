"""
Problem Statement
Write a python function, check_double(number) which accepts a whole number and returns True if it satisfies the given conditions.
The number and its double should have exactly the same number of digits.
Both the numbers should have the same digits ,but in different order.
Otherwise it should return False.
Example: If the number is 125874 and its double, 251748, contain exactly the same digits, but in a different order.
"""
#lex_auth_01269441810970214471

def check_double(number):
    d=number*2
    number=str(number)
    d=str(d)
    
    if(len(number)==len(d)):
        c=0
        for i in d:
            if(i in number):
                c+=1
        if(c==len(number)):
            return True
        else:
            return False
    else:
        return False
        
        
'''OTHER SOLUTION
d=number*2
    number=str(number)
    d=str(d)
    if len(number)==len(d):
        for i in number:
            if i not in d:
                return False
        return True
    return False
    '''
    #Remove pass and write your logic here

#Provide different values for number and test your program
print(check_double(125874))
