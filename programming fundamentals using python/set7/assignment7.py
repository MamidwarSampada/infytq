"""
Problem Statement
Write a python program to validate the details provided by a user as part of registering to a web application.
Write a function validate_name(name) to validate the user name
    Name should not be empty, name should not exceed 15 characters
    Name should contain only alphabets
Write a function validate_phone_no(phoneno) to validate the phone number
    Phone number should have 10 digits
    Phone number should not have any characters or special characters
    All the digits of the phone number should not be same.
    Example: 9999999999 is not a valid phone number
Write a function validate_email_id(email_id) to validate email Id
    It should contain one '@' character and '.com'
    '.com' should be present at the end of the email id.
    Domain name should be either 'gmail', 'yahoo' or 'hotmail'
Note: Consider the format of email id to be username@domain_name.com
All the functions should return true if the corresponding value is valid. Otherwise, it should return false.
Write a function validate_all(name,phone_no,email_id) which should invoke appropriate functions to validate the arguments passed to it and display appropriate message. Refer the comments provided in the code.
Note: You may use str.isalpha(), str.isdigit() methods to check whether a string contains alphabets or digits alone.
"""
#lex_auth_012694465248329728100

def validate_name(name): 
    if(len(name)!=0 and len(name)<16):
    	for i in name:
    		if(not i.isalpha()):
    			return False
    	return True
    else:
    	return False
    #Start writing your code here

def validate_phone_no(phno): 
    if(len(phno)==10 ): 
        if(phno.count(phno[1])!=10): 
            for i in phno: 
                if(not i.isdigit()): 
                    return False
            return True
        
        else:
            return False
    
    else:
    	return False
    #Start writing your code here

def validate_email_id(email_id):  
    if(email_id[-4:]==".com" and '@' in email_id and email_id.count(".")==1):
    	if(email_id[email_id.index('@')+1:-4]=="gmail" or email_id[email_id.index('@')+1:-4]=="yahoo" or email_id[email_id.index('@')+1:-4]=="hotmail"):
    		return True
    	else:
    		return False
    else:
    	return False
    #Start writing your code here

def validate_all(name,phone_no,email_id): 
    if(not validate_name(name)):
        print("Invalid Name")
    elif(not validate_phone_no(phone_no)):
        print("Invalid phone number")
    elif(not validate_email_id(email_id)):
        print("Invalid email id")
    else:
        print("All the details are valid")
    
    #Start writing your code here
    
    # Use the below given print statements to display appropriate messages
    # Also, do not modify them for verification to work
    #print("Invalid Name")
    #print("Invalid phone number")
    #print("Invalid email id")
    #print("All the details are valid")


#Provide different values for name, phone_no and email_id and test your program
validate_all("Tina", "9994599998", "tina@yahoo.com")


''' OTHER SOLUTION
#lex_auth_012694465248329728100

def validate_name(name):
    if 0<len(name)<=15 and name.isalpha():
        return True
    return False
    #Start writing your code here

def validate_phone_no(phno):
    phno=str(phno)
    if len(phno)==10 and phno.isdigit() and phno.count(phno[0])!=10:
        return True
    return False
    #Start writing your code here

def validate_email_id(email_id):
    if '@' in email_id and email_id.endswith('.com') and email_id.count('.com')==1:
        ind=email_id.index('@')
        if email_id[ind+1:-4] in ['gmail','yahoo','hotmail']:
            return True
        return False
    return False
    #Start writing your code here

def validate_all(name,phone_no,email_id):
    if validate_name(name):
        if validate_phone_no(phone_no):
            if validate_email_id(email_id):
                print("All the details are valid")
            else:
                print("Invalid email id")
        else:
            print("Invalid phone number")
    else:
        print("Invalid Name")
    #Start writing your code here
    # Use the below given print statements to display appropriate messages
    # Also, do not modify them for verification to work
    #print("Invalid Name")
    #print("Invalid phone number")
    #print("Invalid email id")
    #print("All the details are valid")


#Provide different values for name, phone_no and email_id and test your program
validate_all("Tina", "9994599998", "tina@yahoo.com")
'''
