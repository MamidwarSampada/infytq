"""
Problem Statement
Use Luhn algorithm to validate a credit card number.
A credit card number has 16 digits, the last digit being the check digit. A credit card number can be validated using Luhn algorithm as follows:
Step 1a: From the second last digit (inclusive), double the value of every second digit.
Suppose the credit card number is 1456734512345698.
Take the double of 9,5,3,1,4,7,5 and 1
i.e., 18, 10, 6, 2, 8, 14, 10 and 2
Note: If any number is greater than 9, then sum the digits of that number.
i.e., 9, 1, 6, 2, 8, 5 ,1 and 2
Step 1b: Sum the numbers obtained in Step 1a.
i.e., 34
Step 2: Sum the remaining digits in the credit card and add it with the sum from Step 1b.
i.e., 34 + (8+6+4+2+5+3+6+4) = 72
Step 3: If the total is divisible by 10 then the number is valid else it is not valid.
Write a function, validate_credit_card_number(), which accepts a 16 digit credit card number and returns true if it is valid as per Luhn’s algorithm or false, if it is invalid. 
"""
#lex_auth_01269445968039936095

def validate_credit_card_number(card_number): 
    p=0
    k=0
    card_number=str(card_number)
    s=card_number[-2:-len(card_number)-1:-2]
   
    for i in s:
    	l=2*int(i)
    	if(l>9):
    		h=0
    		l=str(l)
    		for j in l:
    			h+=int(j)
    		p+=h
    	else:
    		p+=l
   
    g=card_number[-1:-len(card_number):-2]
    
    for i in g:
    	k+=int(i)
    
    t=p+k
    if(t%10==0):
    	return True
    else:
    	return False


#start writing your code here

card_number= 1456734512345698 #4539869650133101  #1456734512345698 # #5239512608615007
result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")
    
    
    
''' OTHER SOLUTION 
#lex_auth_01269445968039936095

def validate_credit_card_number(card_number):
    e=0
    o=0
    l=[]
    d=[]
    card_number=str(card_number)
    for i in range(len(card_number)):
        if i%2==0:
            l.append(int(card_number[i]))
        else:
            o+=int(card_number[i])
            
    for i in l:
        d.append(i*2)
    for i in d:
        if i>9:
            i=str(i)
            for j in i:
                e+=int(j)
        else:
            e+=i
        
            
    if (e+o)%10==0:
        return True
    return False
        
            
    #start writing your code here

card_number= 1456734512345698 #4539869650133101  #1456734512345698 # #5239512608615007
result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")
    
    '''
