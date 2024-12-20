# Exercise 6: Brute Force Attack - 30 Marks
# Write a program that simulates a password entry system. The correct password
# is defined as 12345. The program should keep asking the user to enter the

# password until they provide the correct one.
# Basic Requirements:
# 1. Define the correct password.
# 2. Use a while loop to repeatedly ask the user for the password until the
# correct one is entered.
# 3. Output an appropriate message when the correct password is entered.
# Optional Requirements:
# Modify the program to include a maximum of 5 password attempts. If the
# user enters the wrong password, inform them of the remaining attempts. If the
# maximum number of attempts is reached, inform the user that the authorities
# have been alerted.

right_password = "12345" # correct password is defined as a string since there is no comparison operators in the program
username = input("Enter your username: ") # asks the for the username

counter = 0 # counter for tracking the number of attempts

print("-------------------------------------------------------")
print("------------------- PASSWORD ENTRY --------------------")
print("-------------------------------------------------------")
print("-------You have 5 attempts to unlock this phone.-------")
print("-------------------------------------------------------")

while True: # start a while loop to repeatedly ask for the password
    print("Enter a 5 digit password to gain access.") # displays to tell us what the user should do
    password = input("Enter the password: ") # User input for the correct password
    
    if password == right_password: # check if the entered password is correct 
        print(f"Access granted, Welcome {username}!")
        print("-------------------------------------------------------")
        print("-------------------- ACCESS GRANTED -------------------")
        print("-------------------------------------------------------")
        break # exit the loop if the correct password is entered
    else:
        counter += 1 # adds 1 to the attempts/counter
        remaining_attempts = 5 - counter # calculates and informs the user of how many attempts remaining
        if remaining_attempts > 0:
            print(f"Incorrect password, You have {remaining_attempts} attempts remaining.")
        else:
            print(f"Maximum amount of attempts reached, The authorities have been alerted")
            print("-------------------------------------------------------")
            print("-------------------- ACCESS DENIED --------------------")
            print("-------------------------------------------------------")
            break # exit loop since all attempts are used
        