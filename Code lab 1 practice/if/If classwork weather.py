# classwork to print 2 statements depending on the condition fulfilled, if its more than 40 it prints Nice weather we're having!" and if its less than 40
# it prints "A little cold, isn't it?"

print("Enter the temperature outside, and itll tell you if its cold or not!")

temperature = float(input("Enter your temperature value: "))

if  temperature < 40:
    print("A little cold, isn't it?")
else:
    print("Nice weather we're having!")