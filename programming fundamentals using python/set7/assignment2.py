"""
Problem Statement
Write a python function, remove_duplicates() which accepts a string and removes all duplicate characters from the given string and return it.

Sample Input                                  Expected Output

1122334455ababzzz@@@123#*#*                    12345abz@#*
"""
#lex_auth_01269446319507046499

def remove_duplicates(value):
    a=""
    for i in value:
    	if(i not in a):
    		a+=i
    return a
    #start writing your code here

print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))
