def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

user_input = input("Enter a number to calculate its factorial: ")

number = int(user_input)
result = factorial(number)
print(f"The factorial of {number} is {result}")
