"""
Problem Statement
The International Cricket Council (ICC) wanted to do some analysis of international cricket matches held in last 10 years.
Given a list containing match details as shown below:
[match_detail1,match_detail2……]
Format of each match_detail in the list is as shown below:
country_name : championship_name : total_number_of_matches_played : number_of_matches_won
Example: AUS:CHAM:5:2 means Australia has participated in Champions Trophy 5 times and have won 2 times.

Write a python program which performs the following:
find_matches (country_name): Accepts the country_name and returns the list of details of matches played by that country.
max_wins(): Returns a dictionary containing the championship name as the key and the list of country/countries which have won the maximum number of matches in that championship as the value.
find_winner(country1,country2): Accepts name of two countries and returns the country name which has won more number of matches in all championships. If both have won equal number of matches, return "Tie".

Perform case sensitive string comparison wherever necessary.
match_list – ['ENG:WOR:2:0', 'AUS:CHAM:5:2', 'PAK:T20:5:1', 'AUS:WOR:2:1', 'SA:T20:5:0', 'IND:T20:5:3', 'PAK:WOR:2:0', 'SA:WOR:2:0', 'SA:CHAM:5:1', 'IND:WOR:2:1']

 

Sample Input                                                      Expected Output

find_matches ("AUS")                                     ['AUS':CHAM:5:2','AUS:WOR:2:1']

max_wins()                                      {'WOR': ['AUS', 'IND'], 'CHAM': ['AUS'], 'T20': ['IND']}

find_winner("AUS","IND")                                              IND
"""
#lex_auth_0127667391112806403379

def find_matches(country_name):
    l=[]
    #Remove pass and write your logic here
    for i in match_list:
        s=i.split(":")
        if s[0]==country_name:
            l.append(i) 
    return l

def max_wins():
    #Remove pass and write your logic here
    w=[]
    c=[]
    t=[]
    d={}
    for i in match_list:
        s=i.split(":")
        if s[1]=="WOR":
            w.append(i)
        elif s[1]=="CHAM":
            c.append(i)
        elif s[1]=="T20":
            t.append(i) 
    wmax=0
    g=[]
    for i in w: 
        s=i.split(":")
        if int(s[-1])>wmax:
            wmax=int(s[-1])
    print(wmax)
    for i in w:
        s=i.split(":")
        if int(s[-1])==wmax:
            g.append(s[0])
    print(g)
    if len(g)>0:
        d["WOR"]=g
    print(d)
    cmax=0
    gc=[]
    for i in c: 
        s=i.split(":")
        if int(s[-1])>cmax:
            cmax=int(s[-1])
    for i in c:
        s=i.split(":")
        if int(s[-1])==cmax:
            gc.append(s[0])
    if len(gc)>0:
        d["CHAM"]=gc
    print(d)
    tmax=0
    gt=[]
    for i in t: 
        s=i.split(":")
        if int(s[-1])>tmax:
            tmax=int(s[-1])
    for i in t:
        s=i.split(":")
        if int(s[-1])==tmax:
            gt.append(s[0]) 
    if len(gt)>0:
        d["T20"]=gt
    return d
    
            
    
            
        
    
        

def find_winner(country1,country2):
    #Remove pass and write your logic here 
    c1=0
    c2=0
    for i in match_list:
        s=i.split(":")
        if s[0]==country1:
            c1=int(s[-1])
        elif s[0]==country2:
            c2=int(s[-1])
    if c1>c2:
        return country1
    elif c2>c1: 
        return country2
    elif c1==c2:
        return "Tie"

#Consider match_list to be a global variable
match_list=["AUS:CHAM:5:2","AUS:WOR:2:1","ENG:WOR:2:0","IND:T20:5:3","IND:WOR:2:1","PAK:WOR:2:0","PAK:T20:5:1","SA:WOR:2:0","SA:CHAM:5:1","SA:T20:5:0"]

#Pass different values to each function and test your program
print("The match status list details are:")
print(match_list)
print(max_wins())

''' OTHER SOLUTION
#lex_auth_0127667391112806403379
def find_matches(country_name):
    #Remove pass and write your logic here
    l=[]
    for i in match_list:
        s=i.split(":")
        if s[0]==country_name:
            l.append(i)
    return l

def max_wins():
    d={}
    for i in match_list:
        s=i.split(":")
        if int(s[3])>0:
            if s[1] not in d:
                d[s[1]]=[s[0]]
            else:
                d[s[1]].append(s[0])
    match_list.sort(key=lambda x:x.split(":")[3],reverse=True)
    for key in d:
        m=0
        for i in match_list:
            s=i.split(":")
            if s[1]==key:
                if m<int(s[3]):
                    m=int(s[3])
                elif m>int(s[3]):
                    if s[0] in d[key]:
                        d[key].remove(s[0])
            
    return d
                
    #Remove pass and write your logic here
    

def find_winner(country1,country2):
    #Remove pass and write your logic here
    c1=0
    c2=0
    for i in match_list:
        s=i.split(":")
        if s[0]==country1:
            c1+=int(s[3])
        elif s[0]==country2:
            c2+=int(s[3])
    if c1>c2:
        return country1
    elif c1<c2:
        return country2
    else:
        return "Tie"


#Consider match_list to be a global variable
match_list=["AUS:CHAM:5:2","AUS:WOR:2:1","ENG:WOR:2:0","IND:T20:5:3","IND:WOR:2:1","PAK:WOR:2:0","PAK:T20:5:1","SA:WOR:2:0","SA:CHAM:5:1","SA:T20:5:0"]

#Pass different values to each function and test your program
print("The match status list details are:")
print(match_list)
print()'''
 
