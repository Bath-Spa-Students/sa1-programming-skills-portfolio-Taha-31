while True: # runs a while loop continously until break is added into the while loop
    principle = float(input("Enter the principle amount: ")) # asks the user input for their principle amount
    if principle < 0: # if condition to check if principle is less than 0
        print("principle cant be less than 0") # displays only if our condition is met, and shows us that principle is less than 0
    else: # if our principle is more than 0 there is no error and the while loop is broken
        break

while True: # runs a while loop continously until break is added into the while loop
    rate = float(input("Enter the interest rate: "))
    if rate < 0: # if condition to check if rate is less than 0
        print("interest rate cant be less than 0")
    else: # if our rate is more than 0 there is no error and the while loop is broken
        break

while True: # runs a while loop continously until break is added into the while loop
    time = int(input("Enter the time in years: "))
    if time < 0: # if condition to check if time is less than 0
        print("time cant be less than 0")
    else: # if our time is more than 0 there is no error and the while loop is broken
        break

total = principle * pow((1 + rate / 100), time) # calculates the interest
print(f"Balance after {time} year/s: AED{total:.2f}") # displays using an f formatted string, shows how much our balance will be after n amount of years