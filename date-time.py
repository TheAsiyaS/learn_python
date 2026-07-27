import datetime

# Get the exact current date and time
now = datetime.datetime.now()
print("Raw Time:", now)

# Format the time nicely (e.g., DD-MM-YYYY)
# %d = day, %m = month, %Y = year
formatted_date = now.strftime("%d-%m-%Y")
print("Formatted Date:", formatted_date)

# Calculate the difference between two dates
past_date = datetime.datetime(2023, 1, 1)
difference = now - past_date
print(f"Days since Jan 1, 2023: {difference.days} days")



#----------- my  code ----------------

