## Exercise 10: Is it even? - 35 Marks

# Write a program that tests if a value is even or odd. Follow the instructions outlined below:

# Instructions:
# * The program should ask the user for a number from within the main function.
# * The entered number should be passed to a function that determines if the value is even or odd.
# * The function should return a message indicating whether the number is even or odd.
# * The message returned by the function should be printed from within the main function.



def is_it_even(num):  # defines the is_it_even function
    number = num % 2  # num inputted is divided by 2 and gives 0 or 1 due to remainder operator, then answer is saved in a variable
    if number == 0:   # checks if the number is even by checking if its equal to 0 
        return f"The number: {num} is even!" # if it is it equal to 0 it returns this string
    else:
        return f"The number: {num} is odd!"  # if the number isnt equal to 0 it returns this string


def main():   # defines the main function
    print("--------------------------------------------------")
    print("This program checks if your number is even or odd!")     
    print("--------------------------------------------------")
    while True: # while loop until valid input is given by user
        try: 
            num = int(input("Enter your number: "))  # asks the user input for a number
            result = is_it_even(num)  # result variable that stores whats returned from is_it_even() function
            print(result) # prints the variable result
            break
        except ValueError: # incase the user enters anything besides an integer/float
            print("------------------------------------") 
            print("Invalid input, Please enter a digit.")
            print("------------------------------------")

if __name__ == "__main__":
    main()   # runs the main function
