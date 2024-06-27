# Initialize an empty array
array = []

# Take input from the user for number of elements
n = int(input("Enter number of elements: "))

# Take input from the user for each element and add to the array
for i in range(n):
    element = int(input("Enter element: "))
    array.append(element)

# Print the final array
print("Final array:", array)
