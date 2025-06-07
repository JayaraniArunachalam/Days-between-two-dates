"""A simple Program to calculate days between two days.
Here I have used this program to calculate age in days.
"""

import datetime

# Get date as string input
date_str = input("Enter a your Date of Birth (in DD-MM-YYYY format): ")

# Convert to date object
try:
    date_obj = datetime.datetime.strptime(date_str, "%d-%m-%Y").date()
    print("The DOB you have entered is :", date_obj.strftime("%d-%B-%Y"))
    #Calculating age in days
    if date_obj > datetime.date.today():
        print("The date of birth cannot be in the future.")
    else:
        age_in_days = datetime.date.today() - date_obj
        print("You are", age_in_days.days,"days old")
except ValueError:
    print("Invalid date format. Please use DD-MM-YYYY.")

except Exception as e:
    print("Unexpected Error:",e)