"""
Problem Statement
Tom is working in a shop where he labels items. Each item is labelled with a number between num1 and num2(both inclusive). Since Tom is also a natural mathematician, he likes to observe patterns in numbers. Tom could observe that some of these label numbers are divisible by other label numbers.
Write a Python function to find out those label numbers that are divisible by another label number and display how many such label numbers are there totally.
Note:- Consider only the distinct label numbers. The list of those label numbers should be considered as a set.
"""
#lex_auth_0127136209566679041189

def check_numbers(num1,num2):
    count=0
    l=[]
    for i in range(num1,num2+1):
        for j in range(num1,num2+1):
            if i!=j and i%j==0:
                l.append(i)
                count+=1
                break
    num_list=set(l)
        
    #start writing your code here
    
    return [num_list,count]

num1=2
num2=20
print(check_numbers(num1, num2))
