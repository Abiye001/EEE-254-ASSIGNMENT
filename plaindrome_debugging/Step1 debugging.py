# debug_step1_is_pal.py
# This file adds print statements to investigate the behavior of is_pal
# Focus: Check the behavior of temp and temp.reverse()

def is_pal(x):
    """Assumes x is a list
    Returns True if the list is a palindrome; False otherwise"""
    temp = x[:]
    print("temp before reverse:", temp)
    print("temp.reverse() returns:", temp.reverse())  # Reveals that reverse() returns None
    print("temp after reverse:", temp)
    return temp == x

def silly(n):
    """Assumes n is an int > 0
    Gets n inputs from user
    Prints 'YES' if the sequence of inputs forms a palindrome; 'NO' otherwise"""
    for i in range(n):
        result = []  # Still buggy
        elem = input('Enter element: ')
        result.append(elem)
    if is_pal(result):
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    silly(2)  # Test with inputs like "a" and "b"