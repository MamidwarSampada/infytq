"""
Problem Statement
Mary is a kindergarten teacher. She has given a task to the children after teaching them a list of words. The task is to find the unknown words (other than the words they already know) from the given text. Write a python function which accepts the text and the known list of words and returns the set of unknown words found.
Return -1 if there are no unknown words.

Sample Input                                       Expected Output

Text: "the sun rises in the east"
                                                   {'rises', 'the'}
Vocabulary: ["sun","in","east","doctor","day"]    
"""
#lex_auth_0127667326864670723497

def find_unknown_words(text,vocabulary):
    #Remove pass and write your logic her
    l=[]
    t=text.split()
    for i in t:
        if i not in vocabulary:
            l.append(i) 
    if len(l)>0:
        s=set(l)
        return s
    return -1

text="The sun rises in the east and sets in the west."
vocabulary = ["sun","in","rises","the","east"]
unknown_words=find_unknown_words(text,vocabulary)
print("The unknown words in the file are:",unknown_words)
    
'''OTHER SOLUTION '''
'''def find_unknown_words(text,vocabulary):
    s=set()
    #Remove pass and write your logic here
    for word in text.split(" "):
        if word not in vocabulary:
            s.add(word)
    if len(s)>0:
        return s
    return -1
            '''
        

