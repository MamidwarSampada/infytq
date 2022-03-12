"""
Problem Statement
WeCare insurance company wants to calculate premium of vehicles.
Vehicles are of two types – "Two Wheeler" and "Four Wheeler". Each vehicle is identified by vehicle id, type, cost and premium amount.
Premium amount is 2% of the vehicle cost for two wheelers and 6% of the vehicle cost for four wheelers. Calculate the premium amount and display the vehicle details.
Identify the class name and attributes to represent vehicles. 
calculate_premium()
vehicle_cost
TwoWheeler
vehicle_type
vehicle_id
Vehicle
premium_amount
FourWheeler
premium_percentage
calculate_vehicle_cost()
__init__()
display_vehicle_details()
Write a Python program to implement the class chosen with its attributes and methods.
Note:
Consider all instance variables to be private and methods to be public
Include getter and setter methods for all instance variables
Display appropriate error message, if the vehicle type is invalid
Perform case sensitive string comparison
Represent few objects of the class, initialize instance variables using setter methods, invoke appropriate methods and test your program.
"""
#lex_auth_012736349701922816604
#Start writing your code here
class Vehicle:
    def __init__(self):
        self.__vehicle_id=None
        self.__vehicle_cost=None
        self.__vehicle_type=None
        self.__premium_amount=None
        
    def set_vehicle_id(self,vehicle_id):
        self.__vehicle_id=vehicle_id
    def get_vehicle_id(self):
        return self.__vehicle_id
    
    def set_vehicle_cost(self,vehicle_cost):
        self.__vehicle_cost=vehicle_cost
    def get_vehicle_cost(self):
        return self__.vehicle_cost
        
    def set_vehicle_type(self,vehicle_type):
        self.__vehicle_type=vehicle_type
    def get_vehicle_type(self):
        return self.__vehicle_type
        
    def set_premium_amount(self,premium_amount):
        self.__premium_amount=premium_amount
    def get_premium_amount(self):
        return self.__premium_amount
        
    def calculate_premium(self):
        if(self.__vehicle_type=="Two Wheeler"):
            self.__premium_amount= 0.02*self.__vehicle_cost
        elif(self.__vehicle_type=="Four Wheeler"):
            self.__premium_amount= 0.06*self.__vehicle_cost
        else:
            return 1
    def display_vehicle_details(self):
        if(self.calculate_premium()==1):
            print("invalid")
        else:
            print(self.__vehicle_cost,self.__vehicle_type,self.__vehicle_id,self.__premium_amount)
c=Vehicle()

        
