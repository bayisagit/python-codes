class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=str(x)
        if a==a[::-1]:
            return True
        return False   

        # Create an instance of the Solution class
solution = Solution()

# Get user input
num = int(input("Enter a number: "))

# Check if the number is a palindrome
is_palindrome = solution.isPalindrome(num)

# Print the result
if is_palindrome:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")