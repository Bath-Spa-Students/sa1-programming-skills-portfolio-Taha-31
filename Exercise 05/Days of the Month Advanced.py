
# Advanced requirement
# Leap Year Adjustment: Modify the program to account for leap years. For
# February, ask the user if the year is a leap year and adjust the number of days
# accordingly.

# Advanced Days of the months

days_in_month = {
    1: 31,
    2: 29,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30, 
    10: 31,
    11: 30,
    12: 31} # dictionary mapping month numbers to number of days (assuming February has 28 days by default)

month_names = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"} # dictionary mapping month numbers to month names

is_running = True

while is_running: # Start a loop to prompt for month number input until valid input is given
    month = int(input("Enter the month number you want the days of (1-12): ")) # asks the user to input the month number
    if 1 <= month <= 12: # check if the input is valid
        if month == 2: # check if February needs a leap year adjustment
            is_leap_year = input("Is it a leap year? (yes/no): ").lower()
            if is_leap_year == "yes" and is_leap_year == "no":
                days = 29 if is_leap_year == "yes" else 28
                print(f"The number of days in {month_names[month]} is {days}")
                is_running = False # exit loop since everything is valid
            else:
                print("Thats not a valid answer.")
        else:  # print the number of days for months other than February
            print(f"The number of days in {month_names[month]} is {days_in_month[month]}.")
            is_running = False # exit loop since everything is valid
    else: # else statement if the number inputted is outside of range
        print("Invalid month number, Please enter a number between 1 and 12")