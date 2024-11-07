# Write a program that tells a user how many days there are in a specific month.
# Use a dictionary to map the month numbers (1-12) to the number of days in
# each month.
# Instructions:

# 1. Create a Dictionary: Define a dictionary where the keys are month num-
# bers and the values are the number of days in those months.

# 2. Input Handling: Ask the user to input the month number.
# 3. Check and Output: Use an if-else statement to check if the input is valid
# and print the number of days in the corresponding month.
# Advanced Requirement:
# Leap Year Adjustment: Modify the program to account for leap years. For
# February, ask the user if the year is a leap year and adjust the number of days
# accordingly.

days_in_month = {
    1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31} # dictionary mapping month numbers to number of days (assuming February has 28 days by default)

month_names = {
    1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
    7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"} # dictionary mapping month numbers to month names



is_running = True

while is_running:
    month = int(input("Enter the month number you want the days of (1-12): ")) # asks the user to input the month number
    if 1 <= month <= 12: # check if the input is valid
        print(f"The number of days in the month {month_names[month]} is {days_in_month[month]}") # print the number of days in the month inputted if true
        is_running = False
    else:
        print("Invalid month number, Please enter a number between 1 and 12") # error given if our input is outside of range
        break



