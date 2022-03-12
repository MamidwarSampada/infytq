"""
roblem Statement
"Mysore cabs" wants to automate their booking service.
Write a python program to implement the class diagram given below.

Class description
CabRepository:

Initialize static lists, cab_type_list, charge_per_km and no_of_cars using the sample data given in the table

There is one to one correspondence between these static lists

Cab type list          Hatch Back        Sedan          SUV

Charge per km              9              12             5

Number of cars             2               5             10

CabService:
check_availability(): Check whether the requested cab type is available or not for booking by checking in CabRepository.cab_type_list. If available return index position of the cab type in CabRepository.cab_type_list. Else return -1
get_cab_charge(index): Find and return the charge per km for the car at the given index position from CabRepository.charge_per_km list
calculate_waiting_charge( waiting_time_mins): Calculate and return waiting charge based on the given waiting_time_mins
For first 30 minutes there is no waiting charge
After 30 minutes, 5 rupees should be charged for every extra minute
booking(waiting_time_mins): Calculate and return the final amount to be paid by the customer including the waiting charge for given waiting_time_mins. Also update the number of available cars and generate the service id for each booking starting from 1001. Return -1 if the car is not available.
Perform case sensitive string comparison.
Create objects of CabService class. Invoke booking() on CabService class by passing waiting time in mins and display the details.
"""
#lex_auth_012752552007221248305
#Start writing you code here 
class CabRepository:
    cab_type_list=["Hatch Back","Sedan","SUV"]
    charge_per_km=[9,12,5]
    no_of_cars=[2,5,10]


class CabService:
    __counter=1000
    def __init__(self,cab_type,distance_in_kms):
        self.__cab_type=cab_type
        self.__distance_in_kms=distance_in_kms
        self.__service_id=None
        self.__cab_charge=0
    def get_cab_type(self):
        return self.__cab_type
    def get_distance_in_kms(self):
        return self.__distance_in_kms
    def get_service_id(self):
        return self.__service_id
    def get_cab_charge(self):
        return self.__cab_charge
    
    def check_availability(self):
        if self.__cab_type in CabRepository.cab_type_list and CabRepository.no_of_cars[CabRepository.cab_type_list.index(self.__cab_type)]>0:
            return CabRepository.cab_type_list.index(self.__cab_type)
        else: 
            return -1
    
    def get_cab_charge(self,index):
        return CabRepository.charge_per_km[index]
    
    def calculate_waiting_charge(self,waiting_time_mins): 
        if waiting_time_mins<=30:
            wating_charge=0
        else:
            wating_charge=(waiting_time_mins-30)*5
        return wating_charge
        
    
    def booking(self,waiting_time_mins): 
        if self.check_availability()>=0:  
            final_amount=self.calculate_waiting_charge(waiting_time_mins)+(self.get_cab_charge(CabRepository.cab_type_list.index(self.__cab_type))*self.__distance_in_kms)
            CabRepository.no_of_cars[self.check_availability()]-=1
            CabService.__counter+=1
            self.__service_id=CabService.__counter 
            return final_amount
        else:
            return -1
        

