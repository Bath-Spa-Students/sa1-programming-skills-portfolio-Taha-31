# CLASSWORK simple program to tell you which number that youve entered is greater, or if its the same number itll tell you its equal.

import time

number_1 = int(input("Enter your first number: ")) # input statement that asks the user to input their first number 
time.sleep(1) # time delay function to ask run the next code after a slight delay
number_2 = int(input("Enter your second number: ")) # input statement that asks the user to input their second number
time.sleep(1) # time delay function to ask run the next code after a slight delay

if number_1 > number_2: # if function with the condition if our first number is greater than number 2
    print(f"Your first number ({number_1}) is greater than your second number ({number_2})") # print statement that runs if the if condition above is true.
    #                                                                                          f string thatll show our first number is greater than second number and display the values too.
elif number_2 > number_1: # elif function with the condition if our second number is greater that number 2
    print(f"Your second number ({number_2} is greater than first number ({number_1})") # print statement that runs only if our elif condition is true and shows that our number 2 is greater than number 1, includes f string to show our numbers we entered
elif number_1 == number_2: # elif function with the condition if our number 1 is equal to number 2
    print(f"The two numbers you have entered, {number_1} and {number_2}, are equal!") # print statement that runs only if the above elif condition is true, f string used to include our 2 values inputted to show that their both equal
else: # else statement to end the if else, and if all the above conditions are not true
    print("INVALID!")

# CLASSWORK to tell what grade a student gets based on his score.

import time # import time function to import the time functions.

score = int(input("Enter the student's score: ")) # asks the user to input the student's score
time.sleep(1) 
if score >= 90: # if condition with greater than equal to function to check if the score is above 90 or equal to
    time.sleep(0.5) 
    print(f"Your grade is A! ({score})") # print statement that only runs after the above condition is true, it shows our grade and the score.
elif score >= 80: # elif condition with greater than equal to function to check if the score is above 80 or equal to
    time.sleep(0.5) 
    print(f"Your grade is B! ({score})") # print statement that only runs after the above condition is true, it shows our grade and the score.
elif score >= 70: # elif condition with greater than equal to function to check if the score is above 70 or equal to 
    time.sleep(0.5)
    print(f"Your grade is C :c ({score})") # print statement that only runs after the above condition is true, it shows our grade and the score.
elif score >= 60:# elif condition with greater than equal to function to check if the score is above 60 or equal to
    time.sleep(0.5) 
    print(f"Your grade is D, try harder next time. ({score})") # print statement that only runs after the above condition is true, it shows our grade and the score.
else: 
    time.sleep(0.5)
    print(f"Your grade is F. its a fail buddy. hardluck :c ({score})") # print statement that only runs after the above condition is true, it shows our grade and the score.

