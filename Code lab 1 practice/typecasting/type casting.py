# type casting an input into another data type

item_price = float(input("Enter the price of your item: ")) # asks the user to enter the price of their item and changes the price into a float since its currency
price_paid = float(input("How much are you paying?: ")) # asks the user to enter how mcuh they'll be paying and converts to float since its also going to be currency
item_change = price_paid - item_price # the change theyll be getting is calculated through simple calculation using the subtraction operator
print(f"The price of your item is AED {item_price} and the price paid is AED {price_paid}, your remaining change is AED {item_change}")
# and finally in the end it shows the price of the item, paid and the item change