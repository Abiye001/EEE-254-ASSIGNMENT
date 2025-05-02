import time
import matplotlib.pyplot as plt

# === Cube Root Finder ===
def simple_cube_root(n):
    steps = 0
    is_negative = n < 0
    n = abs(n)
    low = 0
    high = n
    precision = 1e-10

    while low <= high:
        steps += 1
        mid = (low + high) / 2
        cube = mid * mid * mid

        if abs(cube - n) < precision:
            return (-mid if is_negative else mid), steps

        elif cube < n:
            low = mid
        else:
            high = mid

    return (-mid if is_negative else mid), steps

# === Plotting Function ===
def draw_cube_root_graphs(digits, step_counts, time_taken):
    fig, (left, right) = plt.subplots(1, 2, figsize=(12, 5))

    left.plot(digits, step_counts, marker='o', color='blue', label='Steps')
    left.set_title("Steps vs. Number of Digits")
    left.set_xlabel("Digits in Number")
    left.set_ylabel("Steps to Find Cube Root")
    left.grid(True)
    left.legend()

    right.plot(digits, time_taken, marker='s', color='red', label='Time')
    right.set_title("Time vs. Number of Digits")
    right.set_xlabel("Digits in Number")
    right.set_ylabel("Time (seconds)")
    right.grid(True)
    right.legend()

    plt.tight_layout()
    plt.show()

# === Main Program ===
if __name__ == "__main__":
    digits_list = []
    steps_list = []
    time_list = []

    print("Enter numbers to find their cube root. Type 'done' when finished.\n")

    while True:
        user_input = input("Enter a number (or 'done'): ")
        if user_input.lower() == 'done':
            break

        try:
            number = int(user_input)
            digits = len(str(abs(number)))

            start = time.time()
            result, steps = simple_cube_root(number)
            end = time.time()

            time_taken = end - start

            print(f"Cube root of {number} ≈ {result:.6f}")
            print(f"Steps taken: {steps}")
            print(f"Time taken: {time_taken:.8f} seconds\n")

            digits_list.append(digits)
            steps_list.append(steps)
            time_list.append(time_taken)

        except ValueError:
            print("Please enter a valid integer.\n")

    # After all inputs, show graph if there is data
    if digits_list:
        draw_cube_root_graphs(digits_list, steps_list, time_list)
    else:
        print("No valid numbers entered. No graph to show.")
