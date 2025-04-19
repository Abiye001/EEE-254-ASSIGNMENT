# Create a tuple of colors
colors = ('red', 'blue', 'green', 'yellow')

# Create a list to store numbers
numbers = []

# Use range to generate numbers from 1 to 10
for num in range(1, 11):
    numbers.append(num)

# Print the tuple, range based list, and some combinations
print("Colors tuple:", colors)
print("Numbers list from range:", numbers)
print("First color:", colors[0])
print("Last number:", numbers[-1])
print("Even numbers:", [num for num in numbers if num % 2 == 0])