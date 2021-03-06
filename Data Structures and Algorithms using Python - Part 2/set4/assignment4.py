"""
Problem Statement
Given a list of numbers sorted in ascending order. Write a python function which searches for a given number in the list. 
The given number may occur more than once in the list. The function should return the index position at which the last occurrence of the given element is found.
If the number is not found, return -1.
"""
#lex_auth_0127667364335943683412

def last_instance( num_list,  start,  end,  key):
    #Remove pass and write your logic here
    ind=-1
    for i in range(len(num_list)):
        if num_list[i]==key:
            ind=i
    return ind

num_list=[1,1,2,2,3,4,5,5,5,5]
start=0
end=len(num_list)-1
key=5 #Number to be searched
#Pass different values for num_list, start,end and key and test your program
result=last_instance(num_list, start,end,key)

if(result!=-1):
    print("The index position of the last occurrence of the number:",result)
else:
    print("Number not found")
