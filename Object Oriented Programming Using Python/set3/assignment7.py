"""
Problem Statement
"Infinity" IT solution wants to automate their recruitment process. They have decided to accept 5 applications for each of the three job bands ("A", "B" and "C") in the company.
Write a Python program to implement the class diagram given below.
Method/Attribute description:
Initialize static variable, applicant_id_count to 1000
application_dict: Dictionary which store application count (value) for each job band (key)
generate_applicant_id(): Auto-generate applicant id starting from 1001 and initialize attribute, applicant_id
apply_for_job(job_band): Accept the job band for which the applicant is applying.
Check if application count for the applied job band has reached the maximum limit, 5. If so, return -1.
Else,
increment application count for the applied job band by 1 in the dictionary
generate applicant id and
initialize attribute, job_band with the applied job_band
For testing:
Create objects of Applicant class
Invoke apply_for_job(job_band) method on Applicant object by passing the job band for which applicant is applying
If application is accepted, display applicant id, name and job band
Else, display appropriate error message
"""
#lex_auth_012751878508396544244
#Start writing your code here
class Applicant:
    __applicant_id_count=1000
    __application_dict={"A":0,"B":0,"C":0}
    def __init__(self,applicant_name):
        self.__applicant_id=None 
        self.__job_band=None
        self.__applicant_name=applicant_name
    
    def generate_applicant_id(self): 
        if(Applicant.__applicant_id_count==None): 
            Applicant.__applicant_id_count=1000
        Applicant.__applicant_id_count+=1
        self.__applicant_id=Applicant.__applicant_id_count
    def apply_for_job(self,job_band):
        if Applicant.__application_dict[job_band]==5:
            return -1
        else:
            Applicant.__application_dict[job_band]+=1 
            self.generate_applicant_id()
            self.__job_band=job_band
    
    def get_applicant_id(self):
        return self.__applicant_id
    def get_job_band(self):
        return self.__job_band
    def get_applicant_name(self):
        return self.__applicant_name

    @staticmethod
    def get_application_dict():
        return Applicant.__application_dict
        
c=Applicant("sdf")
print(c.get_applicant_id())
