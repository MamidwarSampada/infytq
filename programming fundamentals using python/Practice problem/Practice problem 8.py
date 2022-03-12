"""
Problem Statement
Write a python function which accepts a list of strings containing details of deposits and withdrawals made in a bank account and returns the net amount in the account.
Suppose the following input is supplied to the function 
["D:300","D:300","W:200","D:100"] where D means deposit and W means withdrawal,
then the net amount in the account is 500.

Sample Input                                   Expected Output

["D:300","D:200","W:200","D:100"]                 400

["D:350","W:100","W:500","D:1000"]                750
"""
#lex_auth_0127135929511936001157

def calculate_net_amount(trans_list):
    d=0
    w=0
    for i in trans_list:
        if i.split(":")[0]=='D':
            d+=int(i.split(":")[1])
        elif i.split(":")[0]=='W':
            w+=int(i.split(":")[1])
    #start writing your code here
    net_amount=d-w
    return net_amount

trans_list=["D:300","D:200","W:200","D:100"]
print(calculate_net_amount(trans_list))
 
