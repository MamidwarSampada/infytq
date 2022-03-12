"""
Problem Statement
Write a python function which accepts a given number, n and returns the count of all possible distinct binary strings which are of length n, such that there are no consecutive 1’s in the binary string.

Sample Input      Expected Output
n=2                    3
n=5                    5
Note: The possible binary strings when n= 2 are 00, 01 and 10 and the possible strings when n=3 are 000,001,010,100,101.
"""
#lex_auth_0127667363944120323415

def count_strings(number):
    #Remove pass and write your logic here
    a=[0 for i in range(number)]

    b=[0 for i in range(number)]

    a[0] = b[0] = 1

    for i in range(1,number):

        a[i] = a[i-1] + b[i-1]

        b[i] = a[i-1]

     

    return a[number-1] + b[number-1]

#Pass different values to the function and test your program
number=3
print("The number of strings that can be made are:",count_strings(number))
