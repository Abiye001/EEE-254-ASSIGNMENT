# corrected_palindrome.py
# This is the final corrected code after applying PRAGMATIC debugging strategies
# Fixes:
# 1. Replaced temp.reverse() with temp = temp[::-1] in is_pal
# 2. Moved result = [] outside the loop in silly

def is_pal(x):
    """Assumes x is a list
    Returns True if the list is a palindrome; False otherwise"""
    temp = x[:]
    temp = temp[::-1]  # Correctly creates a reversed copy
    return temp == x

def silly(n):
    """Assumes n is an int > 0
    Gets n inputs from user and stores them in a list
    Prints 'YES' if the sequence forms a palindrome; 'NO' otherwise"""
    result = []  # Moved outside the loop to collect all inputs
    for i in range(n):
        elem = input('Enter element: ')
        result.append(elem)
    if is_pal(result):
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    silly(2)  # Test with inputs like "a" and "b" (correctly prints "NO")