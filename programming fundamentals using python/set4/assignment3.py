"""
Problem Statement
Write a python function, find_correct() which accepts a dictionary and returns a list as per the rules mentioned below.
The input dictionary will contain correct spelling of a word as key and the spelling provided by a contestant as the value.
The function should identify the degree of correctness as mentioned below:
CORRECT, if it is an exact match
ALMOST CORRECT, if no more than 2 letters are wrong
WRONG, if more than 2 letters are wrong or if length (correct spelling versus spelling given by contestant) mismatches.
and return a list containing the number of CORRECT answers, number of ALMOST CORRECT answers and number of WRONG answers. 
Assume that the words contain only uppercase letters and the maximum word length is 10.

Sample Input                                                                                                             Expected Output
{"THEIR": "THEIR", "BUSINESS": "BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}                            [2, 2, 1]

 """

#lex_auth_01269444890062848087

def find_correct(word_dict):
    c=0
    a=0
    w=0

    for i in word_dict:
        if(len(i)==len(word_dict[i])):
            if(i==word_dict[i]):
               c+=1
            else:
               k=0
               for n in range(len(i)):
                   
                   if i[n]!=word_dict[i][n]:
                       k+=1
                      
               if(k<=2):
                    a+=1
               else:
                   w+=1
        else:
            w+=1
    
    d=[c,a,w]
    return d
    
''' OTHER SOLUTION 
c=0
    a=0
    w=0
    for key,value in word_dict.items():
        count=0
        if key==value:
            c+=1
        elif len(key)!=len(value):
            w+=1
        else:
            for i in range(len(key)):
                if key[i]!=value[i]:
                    count+=1
            if count<=2:
                a+=1
            else:
                w+=1
    l=[c,a,w]
    return l
    '''
            
    #start writing your code here

word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))
