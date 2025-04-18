# Calculate the square root of x1 using bisection search
x1 = 25
epsilon = 0.01
if x1 < 0:
    print('Does not exist')  # Square root of a negative number does not exist
else:
    low = 0
    high = max(1, x1)
    ans = (high + low) / 2
    while abs(ans**2 - x1) >= epsilon:  # Continue until the approximation is within epsilon
        if ans**2 < x1:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
x1_root = ans  # Store the calculated square root

# Calculate the cube root of x2 using bisection search
x2 = -8
if x2 < 0:
    is_pos = False  # Track if the number is negative
    x2 = -x2  # Work with the absolute value
else:
    is_pos = True
low = 0
high = max(1, x2)
ans = (high + low) / 2
while abs(ans**3 - x2) >= epsilon:  # Continue until the approximation is within epsilon
    if ans**3 < x2:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2
if is_pos:
    x2_root = ans  # Store the calculated cube root for positive numbers
else:
    x2_root = -ans  # Negate the result for negative numbers
    x2 = -x2
print('Sum of square root of', x1, 'and cube root of', x2, 'is close to', x1_root + x2_root)

# Function to find the maximum of two values
def max_val(x, y):
    # Returns the larger of x and y
    if x > y:
        return x
    else:
        return y

# Function to find the root of a number using bisection search
def find_root(x, power, epsilon):
    # Returns a float y such that y**power is within epsilon of x
    # If x < 0 and power is even, return None (no real root exists)
    if x < 0 and power % 2 == 0:
        return None
    low = min(-1, x)
    high = max(1, x)
    ans = (high + low) / 2
    while abs(ans**power - x) >= epsilon:  # Continue until the approximation is within epsilon
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    return ans

# Function to test the find_root function with multiple inputs
def test_find_root(xvals, powers, epsilons):
    # Iterates through all combinations of xvals, powers, and epsilons
    # and prints the result of find_root
    for x in xvals:
        for p in powers:
            for e in epsilons:
                result = find_root(x, p, e)
                if result == None:
                    val = 'No root exists'  # No valid root found
                else:
                    val = 'Okay'
                    if abs(result**p - x) > e:  # Check if the result is within epsilon
                        val = 'Bad'
                print(f'x = {x}, power = {p}, epsilon = {e}: {val}')

# Test the test_find_root function with sample inputs
x_vals = (0.25, 8, -8)
powers = (1, 2, 3)
epsilons = (0.1, 0.001, 1)
test_find_root(x_vals, powers, epsilons)

# Modularized find_root function with helper functions
def find_root_bound(x, power):
    """Finds the interval [low, high] such that low**power <= x and high**power >= x"""
    low = min(-1, x)
    high = max(1, x)
    return low, high

def bisection_solve(x, power, epsilon, low, high):
    """Uses bisection search to find the root of x within the given interval [low, high]"""
    ans = (high + low) / 2
    while abs(ans**power - x) >= epsilon:  # Continue until the approximation is within epsilon
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    return ans

def find_root(x, power, epsilon):
    """Finds the root of x using modularized helper functions"""
    if x < 0 and power % 2 == 0:
        return None  # Negative number has no even-powered roots
    low, high = find_root_bound(x, power)
    return bisection_solve(x, power, epsilon, low, high)

# Factorial functions
def fact_iter(n):
    """Calculates n! iteratively"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def fact_rec(n):
    """Calculates n! recursively"""
    if n == 1:
        return n
    else:
        return n * fact_rec(n - 1)

# Fibonacci functions
def fib(n):
    """Calculates the nth Fibonacci number recursively"""
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def test_fib(n):
    """Tests the Fibonacci function for all values from 0 to n"""
    for i in range(n + 1):
        print('fib of', i, '=', fib(i))

test_fib(14)

# Palindrome functions
def is_palindrome(s):
    """Checks if a string is a palindrome, ignoring non-letters and capitalization"""
    def to_chars(s):
        """Converts a string to lowercase and removes non-letter characters"""
        s = s.lower()
        letters = ""
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters
    def is_pal(s):
        """Checks if a string is a palindrome recursively"""
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])
    return is_pal(to_chars(s))

print(is_palindrome('Able was I ere I saw Elba'))  # True
print(is_palindrome('Able was I ere I saw Atlanta'))  # False
