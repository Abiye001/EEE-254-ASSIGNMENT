# debug_step2_silly.py
# This file adds print statements to investigate the behavior of silly
# Focus: Check the content of result before calling is_pal

def is_pal(x):
    """Assumes x is a list
    Returns True if the list is a palindrome; False otherwise"""
    temp = x[:]
    temp.reverse()
    return temp == x

def silly(n):
    """Assumes n is an int > 0
    Gets n inputs from user
    Prints 'YES' if the sequence of inputs forms a palindrome; 'NO' otherwise"""
    for i in range(n):
        result = []  # Still buggy
        elem = input('Enter element: ')
        result.append(elem)
    print("result before is_pal:", result)  # Reveals that result only contains the last input
    if is_pal(result):
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    silly(2)  # Test with inputs like "a" and "b"