"""
Problem Statement
Informatica, a consultancy services company has planned to offer cashless transaction service to its employees. The employees can use their smart cards any transaction (credit/debit).
Write a python program to implement the class diagram given below.

Class description

SmartCard class:
    set_account_balance(account_balance): Initialize account_balance to 500.

Employee class:
validate_employee_id(): Employee id should be in the range of 1000 (not inclusive) to 700000(inclusive). If valid return true. Else return false
validate_card_no(): Validate employee's smart card number.
Smart card number should have 9 characters
It should begin with "INF" and
It should not contain alphabets in any other positions
    If the above rules are satisfied, return true. Else return false

Transaction class:
top_up_card(employee, amount): Accept the object of the employee whose smart card should be topped up with given amount.
If the given amount is between 500 and 10000 (both inclusive),
If employee.employee_id and employee.smart_card.card_no are valid, add the given amount to employee.smart_card.account_balance
Else, return -1
Else, return -1
make_payment(employee,amount): Debit the given amount from the employee’s smart card and auto-generate attribute transaction_id starting with "T" followed by first digit of the employee id and first two numeric values of the card number, if the below rules are satisfied
Enough balance should be present in employee's smart card
employee.employee_id and employee.smart_card.account_balance should be valid
It should be possible to maintain minimum balance of Rs.500 in the smart card even after the transaction is made
      If any of the above rules are not satisfied, return -1

Perform case sensitive string comparison.
Create an object of SmartCard class, create an object of Employee using the SmartCard object.
Create objects of Transaction class for the Employee object, invoke make_payment() and top_up_card() methods and display the details.
"""
#lex_auth_012752557061865472306
#Start writing you code her
class SmartCard: 
    def __init__(self,card_no):
        self.__card_no=card_no
        self.__account_balance=500
    
    def get_card_no(self):
        return self.__card_no
    def get_account_balance(self):
        return self.__account_balance
    def set_account_balance(self,account_balance):
        self.__account_balance=account_balance 

class Employee:
    def __init__(self,employee_name,employee_id,smart_card):
        self.__employee_id=employee_id
        self.__employee_name=employee_name  
        self.smart_card=smart_card
    def get_employee_id(self):
        return self.__employee_id 
        
    def get_employee_name(self):
        return self.__employee_name
        
    def validate_employee_id(self):
        if 1000<self.__employee_id<=700000:
            return True
        else:
            return False
    
    def validate_card_no(self):
        if len(self.smart_card.get_card_no())==9 and self.smart_card.get_card_no()[:3]=="INF" and self.smart_card.get_card_no()[3:].isdigit():
            return True
        return False 
        
        
class Transaction:
    def __init__(self): 
        self.__transaction_id=None
    def get_transaction_id(self):
        return self.__transaction_id
    
    def top_up_card(self,employee,amount): 
        if 500<=amount<=10000:
            if employee.validate_employee_id() and employee.validate_card_no():
                a=employee.smart_card.get_account_balance()+amount
                employee.smart_card.set_account_balance(a)
            return -1
        return -1
        
    def make_payment(self,employee,amount):
        if amount<=employee.smart_card.get_account_balance() and employee.validate_card_no() and employee.validate_employee_id() and employee.smart_card.get_account_balance()-amount>=500: 
            employee.smart_card.set_account_balance(employee.smart_card.get_account_balance()-amount)
            self.__transaction_id="T"+str(employee.get_employee_id())[0]+str(employee.smart_card.get_card_no()[3:5])
        return -1
        
