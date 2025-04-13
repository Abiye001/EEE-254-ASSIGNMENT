#Using the Define function to check if a number is prime
def is_prime(n):
    if n <= 1: 
        return False #because 0 and 1 are not prime numbers if i pick any of them as my value of n it wont return true
    
    # it is going to iterates through numbers starting from 2, Check for the square root of what i choose to be the value of n
    for i in range(2, int(n**0.5) + 1):  
        
    #this is going to check if the number is divisible by any number from 2 to the square root of n
        if n % i == 0:
            return False #this will tell us that n is not a prime number
    return True # If the number is not divisibe by any number from 2 to the square root of n, it is a prime number

#using the Define function to sum prime numbers in a given range (start, end)
def sum_primes_in_range(start, end):
    total = 0
    for num in range(start, end + 1):
#still using a Function, but this functon is the prime number function, it is going to check if the number is a prime
        if is_prime(num):
            total += num
    return total

# Get input from user
# the try helps me to handle the user input
# it is going to check if the user input is a number
try:
    start_range = int(input("Enter the starting number: "))
    end_range = int(input("Enter the ending number: "))

#the if statement is going to check if the starting number is greater than the ending number
    if start_range > end_range:
        print("Starting number should be less than or equal to the ending number.")

#and of course the else statement is going to check if the starting number is less than or equal to the ending number
    else:
        result = sum_primes_in_range(start_range, end_range)
        print(f"Sum of prime numbers from {start_range} to {end_range} is: {result}")
        
#If the user decides to be funny and enters a letter or even a special character instead of a number
#It is going to print "please enter valid integers"

except ValueError:
    print("Please enter valid integers.")
