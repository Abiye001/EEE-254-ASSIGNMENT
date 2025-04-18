def validate_inputs(x, power, epsilon):
    """Validates inputs for find_root.
    Args:
        x: a float
        power: a positive int
        epsilon: a positive float
    Returns:
        True if inputs are valid, False otherwise.
    """
    # Check if epsilon is positive and power is at least 1
    if epsilon <= 0 or power < 1:
        return False
    # Check if x is negative and power is even (no real roots exist in this case)
    if x < 0 and power % 2 == 0:
        return False
    # If all checks pass, inputs are valid
    return True

def find_root_bounds(x, power):
    """Args:
        x: a float, power: a positive int
    Returns:
        low, high such that low**power <= x and high**power >= x
    """
    # Set the lower bound to the smaller of -1 or x
    low = min(-1, x)
    # Set the upper bound to the larger of 1 or x
    high = max(1, x)
    # Return the calculated bounds
    return low, high

def bisection_loop(x, power, epsilon, low, high):
    """Core bisection loop for solving.
    Args:
        x, epsilon, low, high: floats
        power: int
        epsilon > 0
        low <= high and there is an ans between low and high s.t.
        ans**power is within epsilon of x
    Returns:
        ans s.t. ans**power within epsilon of x
    """
    # Initialize the midpoint of the interval [low, high]
    ans = (high + low) / 2
    # Continue the loop until the approximation is within epsilon
    while abs(ans**power - x) >= epsilon:
        # If the current answer raised to the power is less than x, adjust the lower bound
        if ans**power < x:
            low = ans
        # Otherwise, adjust the upper bound
        else:
            high = ans
        # Recalculate the midpoint of the interval
        ans = (high + low) / 2
    # Return the final approximation
    return ans

def bisection_solve(x, power, epsilon, low, high):
    """Args:
        x, epsilon, low, high: floats
        power: int
        epsilon > 0
        low <= high and there is an ans between low and high s.t.
        ans**power is within epsilon of x
    Returns:
        ans s.t. ans**power within epsilon of x
    """
    # Use the bisection loop to solve for the root
    return bisection_loop(x, power, epsilon, low, high)

def find_root(x, power, epsilon):
    """Assumes x a float, power an int, epsilon a float.
    Args:
        x: a float
        power: a positive int
        epsilon > 0 & power >= 1
    Returns:
        float y such that y**power is within epsilon of x.
        If x < 0 and power%2 == 0: number has no even-powered roots
        return None
    """
    # Validate the inputs; if invalid, return None
    if not validate_inputs(x, power, epsilon):
        return None
    # Determine the bounds for the root search
    low, high = find_root_bounds(x, power)
    # Solve for the root using bisection
    return bisection_solve(x, power, epsilon, low, high)