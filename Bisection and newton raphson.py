def bisection(f, a, b, tol=1e-6):
    """Bisection method: returns root and iteration count."""
    steps = 0  # Start or trigger step counter
    while (b - a) / 2 > tol:  # Continue until the interval is smaller than the tolerance
        c = (a + b) / 2  # Calculate the midpoint
        if f(c) * f(a) < 0:  # Check if the root is in the left half
            b = c  # put the interval to the left half
        else:
            a = c  # Put the interval to the right half
        steps += 1  # This will increase the step counter
    return (a + b) / 2, steps  # This will return the root and the number of steps

    # I am defining the function f(x) = x^2 - 4
def newton_raphson(f, df, x0, tol=1e-6):
    """Newton-Raphson method: returns root and iteration count."""
    x = x0  # Start with the initial guess
    steps = 0  # Initialize step counter
    while abs(f(x)) > tol:  # Continue until the function value is close to zero
        x = x - f(x) / df(x)  # Update the guess using Newton Raphson formula
        steps += 1  # Keep add to the step counter
    return x, steps  # Return the root and the number of steps

    #i am using the bisection and newton-raphson methods to find the root of f(x) = x^2 - 4 
def compare_methods():
    """Compare Bisection and Newton-Raphson for f(x) = x^2 - 4."""
    f = lambda x: x**2 - 4  # Define the function 
    df = lambda x: 2*x  # Define the derivative of the function
    # Define the function and the  derivative
    bisection_root, bisection_steps = bisection(f, 1, 3)  # Find root using Bisection
    newton_root, newton_steps = newton_raphson(f, df, 3)  # Find root using Newton-Raphson
    
    # Print the results for both methods
    print("Bisection: Root =", round(bisection_root, 6), ", Steps =", bisection_steps)
    print("Newton-Raphson: Root =", round(newton_root, 6), ", Steps =", newton_steps)

# Call the function to compare the methods
compare_methods()