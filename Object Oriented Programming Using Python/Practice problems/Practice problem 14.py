"""
Problem Statement
Fortune hotel wants to automate their daily activities such as check in and check out. There are two types of rooms- Standard and Luxury. Free wifi is available in Luxury room and comfortable desk is available in standard room.
Write a python program to implement the class diagram given below.

Class description

Customer class: 
Initialize static variable counter to 1000

Hotel class:
room_list: List of objects of rooms in the hotel
check_in(customer, room_type): Check-in the given customer based on details mentioned below.
Customer can check in, only if the type of room desired by the customer is available.
If the room is available,
Auto-generate room.customer.customer_id starting from 1001
Assign the customer to the available room
Return true
Else, return false
check_out(customer): Check-out the given customer based on details mentioned below.
Find out the room allocated to the given customer. If found,
Identify the room rent based on type and number of days stayed by the customer
Release the room, i.e., the room should be available for check in by other customers.
Return total room rent
Else, return false

Room class:
Initialize static variable counter to 100
Auto-generate room_id in the child class constructors starting from 101 and prefixed by "L" for luxury room and "S" for Standard room. Examples – S101, L102, S103, L104, L105 etc.

LuxuryRoom class:
calculate_room_rent(no_of_days): Calculate room rent
Calculate room rent based on room price and number of days
For stay of more than 5 days, provide 5% discount on total room rent
Return the final room rent

StandardRoom class:
calculate_room_rent(no_of_days): Calculate room rent
Calculate room rent based on room price and number of days
Return the calculated room rent
Perform case sensitive comparison.
Create objects of Hotel class, invoke appropriate methods and test your program.
"""
#lex_auth_012741101715464192518
#Start writing you code here  
from abc import ABCMeta,abstractmethod
class Customer: 
    counter=1000
    def __init__(self,customer_name,address,no_of_days): 
        self.__customer_id=None 
        self.__customer_name=customer_name 
        self.__address=address 
        self.__no_of_days=no_of_days 
    
    def set_customer_name(self,customer_name):
        self.__customer_name=customer_name 
    
    def set_customer_id(self,customer_id): 
        self.__customer_id=customer_id 
    
    def set_address(self,address):
        self.__address=address 
    
    def set_no_of_days(self,no_of_days): 
        self.__no_of_days=no_of_days 
    
    def get_customer_name(self): 
        return self.__customer_name 
    
    def get_customer_id(self): 
        return self.__customer_id 
        
    def get_address(self): 
        return self.__address 
        
    def get_no_of_days(self):
        return self.__no_of_days
    
    
class Room(metaclass=ABCMeta):
    counter=100 
    
    def __init__(self,price):
        self.__room_id=None
        self.__price =price
        self.__customer=None  
    
    def get_customer(self): 
        return self.__customer 
        
    def get_price(self): 
        return self.__price 
        
    def get_room_id(self): 
        return self.__room_id
        
        
        
    def set_customer(self,customer):
        self.__customer=customer 
        
    def set_price(self,price): 
        self.__price=price 
        
    def set_room_id(self,room_id): 
        self.__room_id=room_id 
    
    
    @abstractmethod    
    def calculate_room_rent(self,no_of_days):
        pass  
        

class LuxuryRoom(Room):
    def __init__(self,price): 
        super().__init__(price)
        self.__free_wifi=True
        LuxuryRoom.counter+=1
        self.__room_id="L"+str(LuxuryRoom.counter) 
        self.set_room_id(self.__room_id)
    
    def get_free_wifi(self):
        return self.__free_wifi 
        
    def set_free_wifi(self,free_wifi): 
        self.__free_wifi=free_wifi 
        
    def calculate_room_rent(self,no_of_days): 
        room_rent=self.get_price()*no_of_days 
        if no_of_days>5:
            room_rent-=room_rent*0.05 
        return room_rent
    
class StandardRoom(Room): 
    def __init__(self,price):
        super().__init__(price)
        self.__comfortable_desk=True
        StandardRoom.counter+=1 
        self.__room_id="S"+str(StandardRoom.counter) 
        self.set_room_id(self.__room_id)
    def get_comfortable_desk(self): 
        return self.__comfortable_desk 
        
    def set_comfortable_desk(self,comfortable_desk):
        self.__comfortable_desk=comfortable_desk 
        
    def calculate_room_rent(self,no_of_days):
        room_rent=no_of_days*self.get_price() 
        return room_rent
        
        
class Hotel:
    def __init__(self,room_list,location): 
        self.__room_list=room_list
        self.__location=location 
    
    def get_room_list(self):
        return self.__room_list 
    
    def set_room_list(self,room_list): 
        self.__room_list=room_list 
        
    def get_location(self): 
        return self.__location 
        
    def set_location(self,location): 
        self.__location=location 
        
    def check_in(self,customer,room_type):
        
        for i in self.__room_list:
            if i.get_room_id()[0]==room_type[0] and i.get_customer()==None:
                i.set_customer(customer)
                Customer.counter+=1 
                i.get_customer().set_customer_id(Customer.counter) 
            
                return True
            
        return False
    
    def check_out(self,customer): 
        for i in self.__room_list: 
            if i.get_customer()!=None :  
                if i.get_customer().get_customer_id()==customer.get_customer_id(): 
                    r=i.calculate_room_rent(customer.get_no_of_days())
                    i.set_customer(None) 
                    return r 
        return False
       
 
