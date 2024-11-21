# Functions -Favorite Book:
# Write a function called favorite_book() that accepts one parameter, title. The function
# should print a message, such as One of my
# favorite books is Alice in Wonderland. Call the function, making sure to include a book
# title as an argument in the function call.

def favorite_book(title):
    return f"Your favourite book title is: {title}!"


def main():
    title = input("Enter your favorite book title: ")
    result = favorite_book(title)
    print(result)

if __name__ == "__main__":
    main()
    
