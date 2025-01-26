from datetime import datetime

# => Get current data and time
getdatetime = datetime.now() 

print("Current date and time = ", getdatetime) # 2025-01-26 22:18:59.366536

print("Year = ",getdatetime.year) # 2025
print("Month = ", getdatetime.month) # 1
print("Day = ", getdatetime.day) # 26
print("Hour = ", getdatetime.hour) # 22
print("Minute = ", getdatetime.minute) # 21 
print("Second = ", getdatetime.second) # 42

# => Create a specific datetime
setdatetime = datetime(2000,5,25,13,30,45)
print("My Birthday - ", setdatetime) #  My Birthday -  2000-05-25 13:30:45

# => strftime, String Formating Date time
getnow = datetime.now()
formatdatetime = getnow.strftime("%Y-%B-%d %H:%M:%S")
print("Formatted Date Time = ", formatdatetime)  # Formatted Date Time =  2025-January-26 22:31:07

# => strptime() , Convert a string to datetime
strdate = "2025-1-26 22:31:07"
converteddate = datetime.strptime(strdate, "%Y-%m-%d %H:%M:%S")
print("Converted datetime = ", converteddate) # Converted datetime =  2025-01-26 22:31:07

# https://docs.python.org/3/library/datetime.html

# 26DT