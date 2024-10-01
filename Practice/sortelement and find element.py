def search(lst, element):
    for i in range(len(lst)):
        if lst[i] == element:
            return i
    return -1

# Function to sort a list
def sort(lst):
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

# Main program
n = int(input("Enter the number of values: "))
values = []
for i in range(n):
    value = int(input("Enter value {}: ".format(i + 1)))
    values.append(value)

# Search for an element in the list
element = int(input("Enter the element to search for: "))
index = search(values, element)
if index == -1:
    print("Element not found")
else:
    print("Element found at index", index)

# Sort the list
sort(values)

# Display the sorted values
print("Sorted values:", values)