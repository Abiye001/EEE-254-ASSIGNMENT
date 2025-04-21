import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(1, 100)
ax.set_ylim(0, 10000)  # Adjust y-limit for visibility
ax.set_xlabel('Input Size (n)')
ax.set_ylabel('Operations')
ax.set_title('Time Complexity Classes')
ax.grid(True)

# Input sizes
n = np.linspace(1, 100, 1000)

# Initialize lines for each complexity class
line_o1, = ax.plot([], [], label='O(1)', color='black')
line_ologn, = ax.plot([], [], label='O(log n)', color='blue')
line_on, = ax.plot([], [], label='O(n)', color='green')
line_onlogn, = ax.plot([], [], label='O(n log n)', color='red')
line_on2, = ax.plot([], [], label='O(n²)', color='purple')
line_on3, = ax.plot([], [], label='O(n³)', color='orange')

ax.legend()

# Initialization function for animation
def init():
    line_o1.set_data([], [])
    line_ologn.set_data([], [])
    line_on.set_data([], [])
    line_onlogn.set_data([], [])
    line_on2.set_data([], [])
    line_on3.set_data([], [])
    return line_o1, line_ologn, line_on, line_onlogn, line_on2, line_on3

# Animation update function
def update(frame):
    x = n[:int(frame)]
    line_o1.set_data(x, [1] * len(x))  # O(1)
    line_ologn.set_data(x, np.log2(x))  # O(log n)
    line_on.set_data(x, x)  # O(n)
    line_onlogn.set_data(x, x * np.log2(x))  # O(n log n)
    line_on2.set_data(x, x**2)  # O(n²)
    line_on3.set_data(x, x**3)  # O(n³)
    return line_o1, line_ologn, line_on, line_onlogn, line_on2, line_on3

# Create animation
ani = FuncAnimation(fig, update, frames=np.linspace(1, 1000, 200), init_func=init, blit=True)

# Save or display the animation
# ani.save('complexity_animation.mp4', writer='ffmpeg', fps=30)  # Requires ffmpeg
plt.show()