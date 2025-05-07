import numpy as np
import matplotlib.pyplot as plt

# Generate data for numbers 1 to 1000 and their squares
x = np.arange(1, 1001)  # Numbers from 1 to 1000
y = x**2  # Calculate the square of each number

# Create the first plot (linear scale)
plt.figure(figsize=(10, 6))  # Set the figure size
plt.plot(x, y, label='y = x²', color='blue', linewidth=2)  # Plot x vs y
plt.xlabel('Number (x)')  # Label for the x-axis
plt.ylabel('Square (x²)')  # Label for the y-axis
plt.title('Squares of Numbers from 1 to 1000')  # Title of the plot
plt.grid(True)  # Add a grid to the plot
plt.legend()  # Add a legend
plt.show()  # Display the plot

# Create the second plot (logarithmic scale on y-axis)
plt.figure(figsize=(10, 6))  # Set the figure size
plt.plot(x, y, label='y = x²', color='blue', linewidth=2)  # Plot x vs y
plt.yscale('log')  # Use a logarithmic scale for the y-axis
plt.xlabel('Number (x)')  # Label for the x-axis
plt.ylabel('Square (x²) [Log Scale]')  # Label for the y-axis
plt.title('Squares of Numbers from 1 to 1000 (Log Scale)')  # Title of the plot
plt.grid(True, which="both", ls="--")  # Add a grid with dashed lines
plt.legend()  # Add a legend
plt.show()  # Display the plot