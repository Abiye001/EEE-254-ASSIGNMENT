# I am importing a module that is used to measure the time taken to compute the cube root
import time
#I am also importing a module that is used to create graphs for Visualizing the results
import matplotlib.pyplot as plt


#Using the define function named simple_cube_root that calculates the cude of the number (n)
def simple_cube_root(n):
    steps = 0

#checks if the input is negative, if it is then n = abs(n) converts the value (n) to simplify the cube root
    is_negative = n < 0
    n = abs(n)
    low = 0 #This is like the lower boundary of the binary search which is 0
    high = n #while this is the upper boundary search
    precision = 1e-5#This helps us to be precised it will keep the number in 5 decimal place even if it's a whle number

    while low <= high: #Using a while loop, Knowing that a while loop keeps going on as long as it remains true
        steps += 1 #This says that keep increasing the number of steps for each iteration
        mid = (low + high) / 2
        cube = mid * mid * mid

        if abs(cube - n) < precision:
            return (-mid if is_negative else mid), steps

        elif cube < n:
            low = mid
        else:
            high = mid

    return (-mid if is_negative else mid), steps

#Again ia m using the define function, this time to draw a cube root graph
def draw_cube_root_graphs(digits, step_counts, time_taken):
    fig, (x_axis, y_axis) = plt.subplots(1, 2, figsize=(12, 5))

#so i am ploting the number of digits against the number of steps taken to find the cube root
#The number of digis is the x-axis
    x_axis.plot(digits, step_counts, marker='o', color='blue', label='Steps')
    x_axis.set_title("Steps vs. Number of Digits")
    x_axis.set_xlabel("Digits in Number")
    x_axis.set_ylabel("Steps to Find Cube Root")
    x_axis.grid(True)
    x_axis.legend()
# The nnumber of digits in the y-axis and 
    y_axis.plot(digits, time_taken, marker='s', color='red', label='Time')
    y_axis.set_title("Time vs. Number of Digits")
    y_axis.set_xlabel("Digits in Number")
    y_axis.set_ylabel("Time (seconds)")
    y_axis.grid(True)
    y_axis.legend()
    
#This is to adjust the layout of the plots to make them look better
    plt.tight_layout()
#This is to display the graph, i almost removed this line of the code
    plt.show()

# This is function that make sure the code run when the script is executed directly
if __name__ == "__main__":
    digits_list = [] # Numbers of digits in the input
    steps_list = [] # Steps taken to find the cube root
    time_list = [] # Time taken to find the cube root

# This is for the user to enter the numbers
    print("Enter numbers to find their cube root. Type 'done' when finished.\n")

    while True:
        user_input = input("Enter a number (or 'done'): ")
        if user_input.lower() == 'done':
            break

        #converts the user input to an Integer
        try:
            number = int(user_input)
            digits = len(str(abs(number)))

            start = time.time()
            result, steps = simple_cube_root(number)
            end = time.time()

            time_taken = end - start # It calculates the tme taken to compute the cube root 
            
            #This will print out the result of the cube root, steps taken, and time taken 
            print(f"The cube root of {number} ≈ {result:.6f}")
            print(f"The steps taken: {steps}")
            print(f"The time taken: {time_taken:.8f} seconds\n")

            digits_list.append(digits)
            steps_list.append(steps)
            time_list.append(time_taken)
        # This is for users that wants to play a prank on the code, trying to input a value that is not an integer
        except ValueError:
            print("Please enter a valid integer.\n")
        #Using the if and else statement, if all the inputs were provided 
    if digits_list:
        draw_cube_root_graphs(digits_list, steps_list, time_list)
    else:
        print("No valid numbers entered. No graph to show.")
