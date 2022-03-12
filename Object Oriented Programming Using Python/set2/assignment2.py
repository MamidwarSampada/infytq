"""
Problem Statement
Royal Orchid is a florist. They want to be alerted when stock of a flower goes below a particular level. 
The flowers are identified using name, price per kg and stock available (in kgs).
Write a Python program to implement the above requirement.
Details of Flower class are given below:

Class name: Flower

Attributes
(private)      flower_name,price_per_kg,stock_available

 Methods
(public)             __init__()                        Create and initialize all instance variables to None

                   validate_flower()                   Return true, if flower name is valid. Else, return false
                                                        (Refer table for valid flower names)

               validate_stock(required_quantity)       Accept the quantity required. Return true, if stock is available.
                                                        Else return false.

              sell_flower(required_quantity)           Accept the quantity required.
                                                       Validate flower name and stock.
                                                     If both are valid, update stock available based on the quantity required

                   check_level()                      Check if available stock is below the order level
                                                      If so, return true. Else, return false
                                                      (Refer table for order level of each flower)

                  setter methods                      Include setter methods for all instance variables to set its values

                  getter methods                      Include getter methods for all instance variables to get its values

 
Flower Name          Level(in Kgs)

Orchid                  15
Rose                    25
Jasmine                 40
Note: Perform case insensitive string comparison
Represent few flowers, initialize instance variables using setter methods, invoke appropriate methods and test your program.
"""
#lex_auth_012727119215337472135
#Start writing your code her
class Flower:
    def __init__(self):
        self.__flower_name=None
        self.__price_per_kg=None
        self.__stock_available=None
    def validate_flower(self):
        l=["orchid","rose","jasmine"]
        if self.__flower_name.lower() in l:
            return True
        else:
            return False
    
    def check_level(self):
        d=[15,25,40]
        l=["orchid","rose","jasmine"]
        if(self.__flower_name.lower() in l):
        	
        	if (d[l.index(self.__flower_name.lower())]>self.__stock_available):
        		return True
        	else:
        		return False
        else:
            return False
            
    def validate_stock(self,required_quantity):
        if required_quantity<=self.__stock_available:
            return True
        else:
            return False
            
    def sell_flower(self,required_quantity):
        if self.validate_flower() and self.validate_stock(required_quantity) and required_quantity<=self.__stock_available:
            self.__stock_available-=required_quantity
            return True
        else:
            return False
  
    
    def set_flower_name(self,flower_name):
        self.__flower_name=flower_name
    def get_flower_name(self):
        return self.__flower_name
        
    def set_price_per_kg(self,price_per_kg):
        self.__price_per_kg=price_per_kg
    def get_price_per_kg(self):
        return self.__price_per_kg
        
    def set_stock_available(self,stock_available):
        self.__stock_available=stock_available
    def get_stock_available(self):
        return self.__stock_available

 
