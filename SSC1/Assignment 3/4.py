def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Get user input for a number
user_number = int(input("Enter a number to check if it is prime: "))

# Test if the user input number is prime
if is_prime(user_number):
    print(f"{user_number} is a prime number")
else:
    print(f"{user_number} is not a prime number")