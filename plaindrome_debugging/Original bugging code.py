# buggy_palindrome.py
# This is the original buggy code from Figure 8-3
# It incorrectly identifies non-palindromes as palindromes due to two bugs

def is_pal(x):
    """Assumes x is a list
    Returns True if the list is a palindrome; False otherwise"""
    temp = x[:]
    temp.reverse()  # Bug 1: reverse() modifies temp in place but returns None
    return temp == x

def silly(n):
    """Assumes n is an int > 0
    Gets n inputs from user
    Prints 'YES' if the sequence of inputs forms a palindrome; 'NO' otherwise"""
    for i in range(n):
        result = []  # Bug 2: result is reset on each iteration, only keeps last input
        elem = input('Enter element: ')
        result.append(elem)
    if is_pal(result):
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    silly(2)  # Test with inputs like "a" and "b" (should print "NO" but prints "YES")