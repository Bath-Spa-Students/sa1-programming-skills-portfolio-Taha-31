# python calculator using if and elif.

operator = input("Enter an operator(+ - * /): " ) # asks the user to input which one of the operators to add
num1 = float(input("Enter the 1st number: ")) # asks the user to input their first number and saves to the variable num1
num2 = float(input("Enter the 2nd number: ")) # asks the user to input their second number and saves to the variable num2


if operator == "+": #if function with the condition equals to, the condition is if our operator is equal to "+"
   result = round(num1 + num2, 2) # our 2 numbers we entered previously will be addiction according to the operator we wrote, and then be saved to the variable "results", this code will only run if the above condition is true
   print(result) # print statement that prints the result variable, only runs if the above condition is true
elif operator == "-": # if function with the condition equals to, the condition is if our operator is equal to "-"
   result = round(num1 - num2, 2) #our 2 numbers we entered previously will be subtracted according to the operator we wrote, and then be saved to the variable "results", this code will only run if the above condition is true
   print(result) # print statement that prints the result variable, only runs if the above condition is true
elif operator == "*": # if function with the condition equals to, the condition is if our operator is equal to "*"
   result = round(num1 * num2, 2) # our 2 numbers we entered previously will be multiplied according to the operator we wrote, and then be saved to the variable "results", this code will only run if the above condition is true
   print(result) # print statement that prints the result variable, only runs if the above condition is true
elif operator == "/": # if function with the condition equals to, the condition is if our operator is equal to "/"
   result = round(num1 / num2, 2) # our 2 numbers we entered previously will be divided according to the operator we wrote, and then be saved to the variable "results", this code will only run if the above condition is true
   print(result) # print statement that prints the result variable, only runs if the above condition is true
else: # else function if all the above conditions are false.
   result = f"{operator} is not valid. please try again!" # the string is saved to result
   print(result) # print statement prints the variable result