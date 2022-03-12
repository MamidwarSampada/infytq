"""
Problem Statement
Spice Hut is a tiffin service provider which home delivers dinner to their customers – Occasional customers and Regular customers. 
Write a Python program to implement class diagram given below.
Class Description:

OccasionalCustomer class:
Initialize static variable counter to 1000
Inside the constructor, auto-generate bill_id starting from 1001 prefixed by "O"
validate_distance_in_kms(): Validate distance in kms
Delivery distance in kms should be between 1 and 5 (both inclusive)
If so, return true. Else, return false

Distance in kms                                Delivery charge in Rs.

Between 1 and 2(both inclusive)                  Rs. 5 per km

Between 2 and 5(excluding 2,including 5)         Rs. 7.5 per km

4. calculate_bill_amount(): Calculate total bill amount
Validate distance in kms
If valid, compute bill amount based on details mentioned below
Occasional customers can order only one tiffin per person
Cost/tiffin is Rs. 50
Delivery charges based on distance is as mentioned in the table
Bill amount includes tiffin cost and delivery charge
Set attribute, bill_amount with the computed bill amount value and return it
If invalid, set attribute, bill_amount as -1 and return it

RegularCustomer class:
Initialize static variable counter to 100
Inside the constructor, auto-generate bill_id starting from 101 prefixed by "R"
validate_no_of_tiffin(): Validate number of tiffins
Regular customer can order a min of 1 and a max of 7 tiffins
If value of no_of_tiffins is valid, return true. Else, return false
calculate_bill_amount(): Calculate weekly bill amount
Validate number of tiffins
If valid, compute bill amount based on details mentioned below
Cost/tiffin is Rs. 50
The order is applicable for all the 7 days of a week
Compute the bill amount based on cost/tiffin, number of tiffins and number of days
Set attribute, bill_amount with the computed bill amount value and return it
If invalid, set attribute, bill_amount as -1 and return it
Note: Perform case sensitive string comparison 

For testing:
Create objects of OccasionalCustomer and RegularCustomer classes
Invoke calculate_bill_amount() on OccasionalCustomer and RegularCustomer objects
Display the details of the customer
"""
#lex_auth_012737214447140864834
#Start writing your code here
from abc import abstractmethod,ABCMeta
class Customer(metaclass=ABCMeta):
    def __init__(self,customer_name):
        self.__customer_name=customer_name
        self.bill_amount=0
        self.bill_id=None
    @abstractmethod
    def calculate_bill_amount(self):
        pass
    def get_customer_name(self):
        return self.__customer_name

class OccasionalCustomer(Customer):
    __counter=1000
    def __init__(self,customer_name,distance_in_kms):
        super().__init__(customer_name)
        self.__distance_in_kms=distance_in_kms
        OccasionalCustomer.__counter+=1
        self.bill_id="O"+str(OccasionalCustomer.__counter)
    def get_distance_in_kms(self):
        return self.__distance_in_kms
    def validate_distance_in_kms(self):
        if 1<=self.__distance_in_kms<=5:
            return True
        else:
            return False
    
    def calculate_bill_amount(self):
        if self.validate_distance_in_kms():
            if 1<=self.__distance_in_kms<=2: 
                delivery_charges=self.__distance_in_kms*5
            elif 3<=self.__distance_in_kms<=5: 
                delivery_charges=self.__distance_in_kms*7.5
            self.bill_amount=50+delivery_charges
            return self.bill_amount
        else:
            self.bill_amount=-1
            return self.bill_amount
    
class RegularCustomer(Customer):
    __counter=100
    def __init__(self,customer_name,no_of_tiffin):
        super().__init__(customer_name)
        self.__no_of_tiffin=no_of_tiffin
        RegularCustomer.__counter+=1
        self.bill_id="R"+str(RegularCustomer.__counter)
    
    def get_no_of_tiffin(self):
        return self.__no_of_tiffin
    
    def validate_no_of_tiffin(self):
        if 1<=self.__no_of_tiffin<=7:
            return True
        else:
            return False
    
    def calculate_bill_amount(self):
        if self.validate_no_of_tiffin():
            self.bill_amount=50*self.__no_of_tiffin*7
            return self.bill_amount
        else:
            self.bill_amount=-1
            return self.bill_amount
 
