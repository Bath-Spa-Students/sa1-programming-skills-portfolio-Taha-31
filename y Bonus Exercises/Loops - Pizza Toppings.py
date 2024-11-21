# Loops- Pizza Toppings :
# Write a loop that prompts the user to enter a series of pizza toppings until they enter a
# 'quit' value. As they enter each topping,
# Print a message saying you’ll add that topping to their pizza.

cart = []

while True:
    pizza_toppings = input("Enter your pizza toppings! (write quit to quit): ").lower()
    if pizza_toppings == "quit":
        break
    else:
        cart.append(pizza_toppings)

print("These toppings will be added into your pizza!")
for pizza_toppings in cart:
    print(pizza_toppings, end=" - ")