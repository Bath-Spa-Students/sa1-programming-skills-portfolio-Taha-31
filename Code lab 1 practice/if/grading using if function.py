grade = input("Enter the student's grade(A/B/C/D): ") # very simple grading system, just made this to make use of the f strings and if function :)

if grade =="A":
    print(f"Congrats you passed! Your grade is {grade}!")
elif grade =="B":
    print(f"Congrats you passed! Your grade is {grade}")
elif grade =="C":
    print(f"You passed but you could definitely improve! your grade is {grade}")
elif grade =="D":
    print(f"Unfortunately your grade is below C, which means you havent passed. Your grade is {grade}")
else:
    print(f"The {grade} you entered is invalid.")