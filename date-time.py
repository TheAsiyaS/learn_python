# import datetime

# # Get the exact current date and time
# now = datetime.datetime.now()
# print("Raw Time:", now)
# # Format the time nicely (e.g., DD-MM-YYYY)
# # %d = day, %m = month, %Y = year
# formatted_date = now.strftime("%d-%m-%Y")
# print("Formatted Date:", formatted_date)

# # Calculate the difference between two dates
# past_date = datetime.datetime(2023, 1, 1)
# difference = now - past_date
# print(f"Days since Jan 1, 2023: {difference.days} days")



#----------- my  code ---------------- days left 

from datetime import date

# 1. Get today's date
today = date.today()

# 2. Define your custom target date (Year, Month, Day)
custom_date = date(2026, 11, 12)
# shows custom date in month 
formate_custom_date = custom_date.strftime("%b %d ").lower()

print ("Date : " + formate_custom_date)
# 3. Subtract today from the custom date
days_left = (custom_date - today).days

print(f"There are {days_left} days left.")
