# Create an empty list
numbers = []

# Take the number of elements from the user
n = int(input("Enter the number of elements: "))

# Take each element from the user and add it to the list
for i in range(0, n):
    num = int(input())
    numbers.append(num)

# Traverse the list to find the maximum number
max_number = numbers[0]  # Assume the first number is the maximum initially
for num in numbers:
    if num > max_number:
        max_number = num

# Print the list and the largest number
print("The list of numbers is:", numbers)
print("The largest number is:", max_number)
