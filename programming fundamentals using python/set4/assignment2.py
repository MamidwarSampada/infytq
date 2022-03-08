"""
Problem Statement
Write a python function, encrypt_sentence() which accepts a message and encrypts it based on rules given below and returns the encrypted message.
Words at odd position -> Reverse It
Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change
Note: Assume that the sentence would begin with a word and there will be only a single space between the words.
Perform case sensitive string operations wherever necessary.

Sample Input                                            Expected Output

the sun rises in the east                          eht snu sesir ni eht stea
"""

#lex_auth_01269444195664691284


def encrypt_sentence(sentence):
    s=sentence.split()
    o=""
    for i in range(len(s)):
        g=""
        if(i%2==0):
            d=s[i][::-1]
            o+=d+""
        else:
            v=""
            c=""
            
            for j in s[i]:
                if(j=="a" or j=="e" or j=="i" or j=="o" or j=="u" or j=="A" or j=="E" or j=="I" or j=="O" or j=="U"):
                    v+=j+""
                else:
                    c+=j+""
            g=c+v+""
        o+=g+" "
    return o.strip()  
    
    
''' OTHER SOLUTION 
sen=""
    sen1=""
    sentence=sentence.split(" ")
    for i in range(len(sentence)):
        if i%2==0:
            sen1=sentence[i][::-1]
        else:
            v="aeiouAEIOU"
            vow=''
            c=''
            for j in sentence[i]:
                if j in v:
                    vow+=j
                else:
                    c+=j+''
            sen1=c+vow
        sen+=sen1+" "
    return sen.strip()
    '''
                
    #start writing your code here

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
