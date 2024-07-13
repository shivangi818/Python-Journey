# your code goes here

def sum_of_elements(arr):
    return sum(arr)

# Reading input
n = int(input().strip())  # Read the size of the array
arr = list(map(int, input().strip().split()))  # Read the array elements

# Calculate the sum of the elements
result = sum_of_elements(arr)

# Print the result
print(result)
