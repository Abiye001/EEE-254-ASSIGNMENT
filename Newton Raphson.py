# Newton-Raphson method implementation without NumPy
# Based on Numerical Recipes approach for root finding

def newton_raphson(func, deriv, x0, tol=1e-7, max_iter=100):
    """
    Find a root of func(x) = 0 using Newton-Raphson method.
    
    Parameters:
    func : function, the target function f(x)
    deriv : function, the derivative f'(x)
    x0 : float, initial guess
    tol : float, convergence tolerance
    max_iter : int, maximum number of iterations
    
    Returns:
    float, the root, or None if no convergence
    """
    # Initialize the current guess to the initial guess
    x = x0
    for i in range(max_iter):
        # Evaluate the function and its derivative at the current guess
        fx = func(x)
        dfx = deriv(x)
        
        # Check for zero derivative to avoid division by zero
        if abs(dfx) < 1e-15:
            print("Error: Derivative too small")  # Derivative is too small to proceed
            return None
        
        # Newton-Raphson step: x_new = x - f(x)/f'(x)
        dx = fx / dfx  # Calculate the change in x
        x = x - dx  # Update the current guess
        
        # Check for convergence (if the change is smaller than the tolerance)
        if abs(dx) < tol:
            return x  # Root found, return the result
    
    # If the loop completes without finding a root, print a warning
    print("Warning: Maximum iterations reached")
    return None

# Example function: f(x) = x^2 - 2
# This function represents the equation whose root we want to find
def func(x):
    return x * x - 2

# Derivative: f'(x) = 2x
# This is the derivative of the function f(x)
def deriv(x):
    return 2 * x

# Test the Newton-Raphson method
if __name__ == "__main__":
    # Initial guess for the root
    x0 = 1.0
    # Call the Newton-Raphson method with the function, its derivative, and the initial guess
    root = newton_raphson(func, deriv, x0)
    if root is not None:
        # If a root is found, print the root and the function value at the root
        print(f"Root found at x = {root}")
        print(f"Function value at root: {func(root)}")
    else:
        # If no root is found, print a failure message
        print("Failed to find root")