"""
Problem Statement
Write a Python program to generate the next 15 leap years starting from a given year. Populate the leap years into a list and display the list.
"""

#lex_auth_012693797166096384149

def find_leap_years(given_year):
    list_of_leap_years=[]
    while(len(list_of_leap_years)<15):
        if((given_year%4==0 and given_year%100!=0) or given_year%400==0):
    
            while(len(list_of_leap_years)<15):
                
                s=given_year
                if((s%4==0 and s%100!=0) or (s%100==0 and s%400==0)):
                   list_of_leap_years.append(s)
                given_year+=4
        else:
            given_year+=1
        
        
    # Write your logic here

    return list_of_leap_years
    
''' OTHER SOLUTION 
list_of_leap_years=[]
    def leap(given_year):
        while True:
            if given_year%400==0 or (given_year%4==0 and given_year%100!=0):
                given_year=given_year
                break
            else:
                given_year+=1
        return given_year
        
    while len(list_of_leap_years)<15:
        given_year=leap(given_year)
        list_of_leap_years.append(given_year)
        given_year+=4
        '''

list_of_leap_years=find_leap_years(2000)
print(list_of_leap_years)
