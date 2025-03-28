def largest_k_palindromic(n, k):
    # Function to create the largest palindrome
    max_num = '9' * n

    # Check if the number is divisible by k
    for i in range(int(max_num), 0, -1):
        str_num = str(i)
        if len(str_num) != n:
            continue  # Skip numbers that do not have n digits
        if str_num == str_num[::-1] and i % k == 0:  # Check if palindrome and divisible by k
            return str_num

    return ""  # If no such number exists

# Example usage:
print(largest_k_palindromic(3, 5))  # Output: "595"
print(largest_k_palindromic(1, 4))  # Output: "8"
print(largest_k_palindromic(5, 6))  # Output: "89898"