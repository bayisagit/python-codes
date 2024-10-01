# Create a dictionary to store the frequency of each number
freq = {}

# Get the number of elements in the array
n = int(input("How many numbers are you going to enter: "))

# Get the array elements
arr = []
for i in range(n):
    num = int(input("Enter a number: "))
    arr.append(num)

    # Increment the frequency of the current number
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

# Find the number with the highest frequency
max_freq = 0
max_freq_num = None
for num, count in freq.items():
    if count > max_freq:
        max_freq = count
        max_freq_num = num

# Print the number with the highest frequency
print("The number with the highest frequency is:", max_freq_num)
print("Its frequency is:", max_freq)