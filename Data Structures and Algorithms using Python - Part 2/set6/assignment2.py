"""
Problem Statement
The Bangalore railway authorities have decided to construct the required number of platforms in the station so that the trains need not wait in order to get the platforms.
Given the arrival and departure times of all the trains that reach a railway station. The task is to find the minimum number of platforms required for the railway station so that no train waits without the platform.
Write a python function which accepts the arrival time list and departure time list and returns the minimum number of platforms required.

Sample Input                                                             Expected Output

arrival_time_list = [800,850,600,1120,1050,900]
departure_time_list = [1110,1200,1400,1130,1700,2200]                        5

arrival_time_list = [800,850,600, 1350, 1120,1050,900]
departure_time_list = [1110,1200,830, 1400, 1055, 1130,1700,2200]            4

Note: Time is provided in 24 hour format.
Hint: Start by sorting the arrival time list and departure time list and then compare the arrival and departure time.
"""#lex_auth_0127667363417702403454
def find_number_of_platforms(arrival_time_list,departure_time_list):
    #Remove pass and test your progra
    arrival_time_list.sort()
    departure_time_list.sort() 
    a=departure_time_list[0]
    c=1
    for i in range(2,len(arrival_time_list)-1):
    		if  departure_time_list[i]>arrival_time_list[i+1] or a>arrival_time_list[i+1]:
    			c+=1
    return c

#Pass different values to the function and test your program
arrival_time_list = [800,810]
departure_time_list = [2300,2000]
print("The arrival time of the trains:", arrival_time_list)
print("The departure time of the trains:",departure_time_list)
print("Minimum number of platforms required :",find_number_of_platforms(arrival_time_list,departure_time_list))
