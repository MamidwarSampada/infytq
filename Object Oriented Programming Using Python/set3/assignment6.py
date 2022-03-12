"""
Problem Statement
Write a Python program to generate tickets for online bus booking, based on the class diagram given below.
Method description:
Initialize static variable counter to 0
validate_source_destination(): Validate source and destination. source must always be Delhi and destination can be either Mumbai, Chennai, Pune or Kolkata. If both are valid, return true. Else return false
generate_ticket():
Validate source and destination
If valid, generate ticket id and assign it to attribute, ticket_id. Ticket id should be generated with the first letter of source followed by first letter of destination and an auto-generated value starting from 01 (Ex: DM01, DP02,.. ,DK10,DC11)
Else, set ticket_id as None
Note: Perform case insensitive string comparison

For testing:
Create objects of Ticket class
Invoke generate_ticket() method on Ticket object
Display ticket id, passenger name, source, destination
In case of error/invalid data, display appropriate error message
"""
#lex_auth_012751870201536512237
#Start writing your code her
class Ticket:
    counter=0
    def __init__(self,source,destination,passenger_name):
        self.__source=source
        self.__destination=destination
        self.__passenger_name=passenger_name
        self.__ticket_id=None
    def validate_source_destination(self):
        l=["Mumbai","Chennai","Pune","Kolkata"]
        if(self.__source.title()=="Delhi"):
            if(self.__destination.title() in l):
                return True
            else:
                return False
        else:
            return False
    def generate_ticket(self):
        if(self.validate_source_destination()):
            if(Ticket.counter<9):
                self.__ticket_id=self.__source[0]+self.__destination[0]+"0"+str(Ticket.counter+1)
            else:
                self.__ticket_id=self.__source[0]+self.__destination[0]+str(Ticket.counter+1)
                
                
    def get_source(self):
        return self.__source
    def get_destination(self):
        return self.__destination
    def get_ticket_id(self):
        return self.__ticket_id
    def get_passenger_name(self):
        return self.__passenger_name
    
