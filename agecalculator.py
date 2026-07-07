from datetime import datetime

# Get user input
birth_year = int(input("Enter your birth year (YYYY): "))
birth_month = int(input("Enter your birth month (MM): "))
birth_day = int(input("Enter your birth day (DD): "))

# Current date
today = datetime.today()

# Calculate age
age = today.year - birth_year

# Adjust if birthday hasn't occurred yet this year
if (today.month, today.day) < (birth_month, birth_day):
    age -= 1

# Output result
print("Your age is:", age, "years")