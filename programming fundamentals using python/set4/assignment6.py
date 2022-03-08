"""
Problem Statement
Write a python program that accepts a text and displays a string which contains the word with the largest frequency in the text and the frequency itself separated by a space.
Rules:The word should have the largest frequency.
In case multiple words have the same frequency, then choose the word that has the maximum length.
Assumptions:The text has no special characters other than space.
The text would begin with a word and there will be only a single space between the words.
Perform case insensitive string comparisons wherever necessary.

Sample Input                                                                                                                Expected Output

"Work like you do not need money love like you have never been hurt and dance like no one is watching"                          like 3

"Courage is not the absence of fear but rather the judgement that something else is more important than fear"                    fear 2
"""

#lex_auth_0127382283825971201450

def max_frequency_word_counter(data):
    word=""
    frequency=0 
    data=data.lower()
    s=data.split()
    for i in s:
    	c=s.count(i)
    	if(frequency<c):
    		frequency=c
    		word=i
    	elif(frequency==c):
    		frequency=c
    		if(len(word)<len(i)):
    			word=i
    		else:
    			word=word
    print(word,frequency)
    
''' OTHER SOLUTION
word=""
    frequency=0
    data=data.lower()
    data=data.split()
    for i in data:
        if frequency<data.count(i):
            frequency=data.count(i)
            word=i
        elif frequency==data.count(i):
            frequency=frequency
            if len(word)<len(i):
                word=i
    print(word,frequency)
    '''

    #start writing your code here
    #Populate the variables: word and frequency


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    #print(word,frequency)


#Provide different values for data and test your program.
data="Work like you do not need money, love like you have never been hurt, and dance like no one is watching"
max_frequency_word_counter(data)
