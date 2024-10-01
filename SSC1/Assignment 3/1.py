def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Get user input for the number
user_number = int(input("Enter a number: "))

# Call the function with the user input
result = check_even_odd(user_number)
print(f"The number {user_number} is {result}")