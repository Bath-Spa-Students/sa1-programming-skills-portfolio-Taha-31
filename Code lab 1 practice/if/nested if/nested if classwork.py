# CLASSWORK nested if

salary = float(input("Enter your salary: ")) # asks the user to input the salary and type casts it into floating point

if salary >= 30000: # if function with the condition greater than or equals to, the condition is if the variable salary is greater than or equal to 30K
        years_on_job = float(input("Enter the amount of years you have worked in this field: ")) # this code only runs if the above if condition is true, it asks the user to input how many years theyve worked in their job (how much experience they have)
        if years_on_job >= 2: # if function with the condition greater than or equals to, the condition is if the variable years_on_job is greater than or equal to 2 years
            print("You qualify for the loan") # print statement that only runs if the above if condition is true, prints you qualify the for the loan if both the above if conditions are met
        else: # else function if the nested if condition is false
            print("You must have been on your current job for at least two years to qualify") # prints only if the nested if is false
else: # else function if the MAIN if condition is false
    print("You must earn at least 30k per year to qualify") # prints only if the MAIN if is false
