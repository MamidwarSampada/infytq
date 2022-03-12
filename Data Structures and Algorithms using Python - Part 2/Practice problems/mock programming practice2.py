"""
Problem Statement
AtoZ shopping has come up online to facilitate shopping of items by the customers. The process of calculation of bill amount has to be automated.
The class design for the same is given below. 
Class Diagram:
Note:
Do not include any extra instance/static variables and instance/static methods in the given classes
Case sensitive comparison is required to be done wherever applicable
Do not change any value or case of the given variables
Read notes and examples for better understanding of the logic
Implementation Details:
Class Name
Implementation Details
CustomerDetails
Partially implemented
Customer
Fully Implemented
RegisteredCustomer
Partially implemented
Bill
Partially implemented
CustomerDetails Class: 
customer_point _details: 
This is a static dictionary which contains the customer id (string) as key and points (integer) as value. The initial values of customer_point_details dictionary are:
customer_point_details
{'R1001':892, 'R1002':956, 'R1003':1352}
mem_card_types and card_type_points: 
mem_card_types is a static list that has all the membership card types. card_type_points is another static list that has the points of corresponding membership card type. 
The values are to be stored in each list is given below 

mem_card_types                          card_type_points 

['Silver', 'Gold', 'Platinum']              [2,4,5]
Note: Both the lists have one to one correspondence. I.e. for silver membership card there is 2 points.
get_card_points(card_type):
This is a static method which accepts card_type (string) as input parameter and returns points (integer).
Check if the provided card_type is present in the mem_card_types list
If card_type is not present, return -1
Otherwise, for the given card_type, find the corresponding points from the card_types_points list
Return the identified points in the above step
Note: Perform case in-sensitive comparison 
For Example: If card_type is 'GolD' and with the initial values of mem_card_types and card_type_points this method will return 4. 
add_point(cust_id, points):
This is a static method that accepts two parameters, cust_id (string) and points (integer), updates customer_point_details dictionary.
Check if the cust_id present in customer_point_details dictionary.
If found, add the points to the existing value of the cust_id in customer_point_details dictionary.
Otherwise, add a new entry with cust_id as key and points as value to customer_point_details dictionary.
Note: Perform case in-sensitive comparison 
 For Example:If cust_id is 'r1003', points is 400 and with the initial values of customer_point_details dictionary (as mentioned above), then the updated values of same dictionary is {'R1001':892, 'R1002':956, 'R1003':1752}
redeem_points(cust_id):
This is a static method that accepts cust_id (string) as a parameter, updates customer_point_details dictionary and returns redeem_value (integer)
Check if the cust_id is present in customer_point_details dictionary
If not present, return 0.
If cust_id is present, customer_point_details dictionary will be updated as discussed below –
The customer has to maintain a minimum of 1500 points
If the customer has greater than 1500 points, the redeem_value will be 75% of the points redeemed after maintaining the minimum points.
After calculating the redeem_value update the dictionary.
If the customer has less than or equal to 1500 points, points can't be redeemed and the redeem_value will be 0
Return the redeem_value.
Note: Perform case in-sensitive comparison.
For Example:If cust_id is 'r1003' and customer_point_details dictionary with values {'R1002': 956,'R1001': 892, R1003': 1752}, then this method will return 189.0 and the updated values of same dictionary is {'R1001':892, 'R1002':956, 'R1003':1500}
RegisteredCustomer Class:
validate_cust_details():
This method validates the instance variable cust_id (string), cust_name (string) and mem_card_type (string) and returns true if valid. Otherwise, returns false
If the cust_id, cust_name and mem_card_type are not None, return true
Otherwise, return false
For Example: cust_id is 'r1003', cust_name is 'John' and mem_card_type is 'GolD', this method should return true.
Bill Class: 
generate_bill_num() 
This method auto-generates bill_num (integer)
The bill_num would be auto-generated integer value starting from 5001.
The auto-generated integer value would be incremented by 1 for next bill_num
Use static variable counter appropriately to implement auto-generation logic
For Example: First bill_num would be 5001 and second would be 5002 and so on.
calculate_points(bill_amount):
This method takes bill_amount (float) as parameter and returns points (integer)
Invoke get_card_points() method by passing mem_card_type as a parameter of CustomerDetails class to identify the card_type_points
If card_type_points is equal to -1, return -1
Otherwise,
The points will be calculated using below formula – points = (bill_amount ×card_type_points) / 100  Note: Perform integer division
Return points
For Example:If custid is 'r1003',cust_name is 'John', mem_card_type is 'GolD', bill_amount is 10000 and with initial values of mem_card_types list and card_type_points list, this method should return 400.
calculate_final_bill_amount(bill_amount): 
This method takes bill_amount (float) as parameter to calculate and return final_bill_amount (float)
Invoke validate_cust_details method of Customer class
If bill_amount is greater than 100 and validate_cust_details() method returns true then,
Invoke calculate_points() method of Bill class by passing bill_amount as a parameter to identify the points
If points is equal to -1, then set final_bill_amount and bill_num to -1
Otherwise,
Invoke add_point()of CustomerDetails class by passing cust_id and points as parameters
Invoke generate_bill_num() method of Bill class.
If redemption_required(boolean), then invoke redeem_points() method of CustomerDetails class by passing cust_id as parameter and subtract the redeem_values from the bill_amount to get the final_bill_amount.
Otherwise, final_bill_amount is same as the bill_amount
Return final_bill_amount
For Example:If custid is 'r1003', cust_name is 'John' and mem_card_type is 'GolD' and with initial values of customer_point_detailsdictionary, mem_card_types list and card_type_points list, this method should return 9811.0, the updated customer_point_details will be {'R1002': 956, 'R1001': 892, 'R1003': 1500} and the bill_num will be 5001.
"""
#lex_auth_012761737764249600708
#Do Not Change any part of the code provided to you
from abc import ABCMeta, abstractmethod
class CustomerDetails:
    customer_points_details = {'R1001':892, 'R1002':956, 'R1003':1352}
    mem_card_types = ['Silver','Gold','Platinum']
    card_type_points = [2,4,5]

    #To Trainee
    @staticmethod
    def get_card_points(card_type): 
        if card_type.title() in CustomerDetails.mem_card_types: 
            return CustomerDetails.card_type_points[CustomerDetails.mem_card_types.index(card_type.title())]
        return -1
    
        #Remove pass and write your logic

    #To Trainee
    @staticmethod
    def add_point(cust_id,points):
        if cust_id.title() in CustomerDetails.customer_points_details:
            CustomerDetails.customer_points_details[cust_id.title()]+=points 
        else:
            CustomerDetails.customer_points_details[cust_id.title()]=points
 #Remove pass and write your logic

    #To Trainee
    @staticmethod
    def redeem_points(cust_id):
        if cust_id.title() in CustomerDetails.customer_points_details: 
            if CustomerDetails.customer_points_details[cust_id.title()]<=1500: 
                return 0
            else:
                d=CustomerDetails.customer_points_details[cust_id.title()]-1500
                CustomerDetails.customer_points_details[cust_id.title()]=1500
                return d*0.75
        else:       
            return 0
        
        #Remove pass and write your logic
class Customer(metaclass = ABCMeta):
    def __init__(self,cust_id,cust_name):
        self.__cust_id = cust_id
        self.__cust_name = cust_name

    def get_cust_id(self):
        return self.__cust_id

    def get_cust_name(self):
        return self.__cust_name

    @abstractmethod
    def validate_cust_details(self):
        pass


class RegisteredCustomer(Customer):
    def __init__(self,cust_id,cust_name,mem_card_type):
        super().__init__(cust_id, cust_name)
        self.__mem_card_type = mem_card_type

    def get_mem_card_type(self):
        return self.__mem_card_type

    #To Trainee
    def validate_cust_details(self):
        if (self.__mem_card_type==None or self.get_cust_name()==None or self.get_cust_id()==None): 
            return False
        return True
        #Remove pass and write your logic

class Bill:
    __counter = 5001
    def __init__(self,customer,redeemption_required):
        self.__customer = customer
        self.__redeemption_required = redeemption_required
        self.__bill_num = None

    def get_customer(self):
        return self.__customer

    def get_redeemption_required(self):
        return self.__redeemption_required

    def get_bill_num(self):
        return self.__bill_num

    #To Trainee
    def generate_bill_num(self):
        self.__bill_num=Bill.__counter 
        Bill.__counter+=1
        return self.__bill_num
        
        #Remove pass and write your logic

    #To Trainee
    def calculate_points(self,bill_amount):
        p=CustomerDetails.get_card_points(self.__customer.get_mem_card_type()) 
        if p==-1:
            return -1 
        else:
            return (bill_amount*p)/100 
        
        #Remove pass and write your logic

    #To Trainee
    def calculate_final_bill_amount(self,bill_amount):
        a=self.__customer.validate_cust_details() 
        if a and bill_amount>100:
            c=self.calculate_points(bill_amount) 
            if c==-1: 
                self.__bill_num=-1 
                final_bill_amount=-1 
                
            else: 
                CustomerDetails.add_point(self.__customer.get_cust_id(),c) 
                self.generate_bill_num() 
                if self.__redeemption_required: 
                    r=CustomerDetails.redeem_points(self.__customer.get_cust_id()) 
                    final_bill_amount=bill_amount-r 
                else: 
                    final_bill_amount=bill_amount 
        return final_bill_amount
            
        
        #Remove pass and write your logic


cust_obj = RegisteredCustomer('r1003', 'John', 'GolD')
bill_obj = Bill(cust_obj, True)
final_bill_amount = bill_obj.calculate_final_bill_amount(10000)
print('Bill Num :',bill_obj.get_bill_num())
print('Final Bill Amount :',final_bill_amount)
print(CustomerDetails.customer_points_details)
