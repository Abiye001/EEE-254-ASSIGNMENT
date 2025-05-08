import matplotlib.pyplot as plt

# Parameters
initial_population = 100
growth_rate = 5
time_steps = 50

# For loop growth
pop_for = [initial_population]
for t in range(1, time_steps):
    pop = initial_population + growth_rate * t
    pop_for.append(pop)

# While loop growth
pop_while = [initial_population]
t = 1
while t < time_steps:
    pop = initial_population + growth_rate * t
    pop_while.append(pop)
    t += 1

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(range(time_steps), pop_for, 'b-', label='For Loop Growth')
plt.plot(range(time_steps), pop_while, 'r--', label='While Loop Growth')
plt.title('Simple Population Growth')
plt.xlabel('Time')
plt.ylabel('Population')
plt.grid(True)
plt.legend()

# Save plot
plt.savefig('simple_population_growth.png')