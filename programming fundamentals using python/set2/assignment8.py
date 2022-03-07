"""
Problem Statement
Write a python program which finds the maximum number from num1 to num2 (num2 inclusive) based on the following rules.
 1. Always num1 should be less than num2
 2. Consider each number from num1 to num2 (num2 inclusive). Populate the number into a list, if the below conditions are satisfied
      a. Sum of the digits of the number is a multiple of 3

      b. Number has only two digits

      c. Number is a multiple of 5

3. Display the maximum element from the list
In case of any invalid data or if the list is empty, display -1.
"""
#lex_auth_012693813706604544157

def find_max(num1, num2):
    max_num=-1
    l=[]
    # Write your logic here
    if(num1<num2):
        for i in range(num1,num2+1):
            if(i>0 and i<100 and i%5==0 and i%3==0):
                l.append(i)
        if(len(l)>0):
            max_num=max(l)
    return max_num

#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,15)
print(max_num)
