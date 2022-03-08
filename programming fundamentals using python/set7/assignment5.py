"""
Problem Statement
Write a python function, nearest_palindrome() which accepts a number and returns the nearest palindrome greater than the given number. 

Sample Input           Expected Output

12300                     12321

12331                     12421
"""
#lex_auth_01269443664174284882
def nearest_palindrome(number): 
    number+=1

    number=str(number)
    p=number[::-1]
    

    while(int(p)!=int(number)): 
        number=int(number)+1 
        number=str(number) 
        p=number[::-1] 
    return int(number)
  
   #start writitng your code here

number=12300
print(nearest_palindrome(number))

'''OTHER SOLUTION
def nearest_palindrome(number):
    number+=1
    while True:
        s=str(number)[::-1]
        if number==int(s):
            return number
        else:
            number+=1
        
    #start writitng your code here

number=12300
print(nearest_palindrome(number))
'''
