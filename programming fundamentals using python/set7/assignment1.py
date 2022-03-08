"""
Problem Statement
Write a python function, check_anagram() which accepts two strings and returns True, if one string is a special anagram of another string. Otherwise returns False.
The two strings are considered to be a special anagram if they contain repeating characters but none of the characters repeat at the same position. The length of the strings should be the same.
Note: Perform case insensitive comparison wherever applicable.

Sample Input                                                          Expected Output

eat, tea                                                                    True

backward,drawback                                                           False (Reason: character 'a' repeats at position 6, not an anagram)

Reductions,discounter                                                       True

About, table                                                                False
"""
#lex_auth_0127382206342184961397

def check_anagram(data1,data2):
    data1=data1.lower()
    data2=data2.lower()
    t=0
    if(len(data1)==len(data2)):
        for i in data1:
        	if(i in data2): 
        	    if(data1.count(i)==data2.count(i)): 
        	        if(data1.index(i)!=data2.index(i)): 
        	            t+=1
        	        else: 
        	            return False 
        	    else: 
        	        return False
        	else:
        		return False
    else:
       return False
    if(t==len(data1)):
       return True
    else:
        return False
        		#start writing your code here

print(check_anagram("eat","tea"))


'''OTHER SOLUTION 
def check_anagram(data1,data2):
    data1=data1.lower()
    data2=data2.lower()
    if len(data1)==len(data2):
        if all(i in data1 for i in data2) and all(i in data2 for i in data1):
            for i in range(len(data2)):
                if data1[i]==data2[i]:
                    return False
            return True
        return False
    
    else:
        return False
    #start writing your code here

print(check_anagram("eat","tea"))
'''
