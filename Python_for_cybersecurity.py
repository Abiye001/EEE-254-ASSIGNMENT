import re  # Import the regular expressions module for pattern matching
import matplotlib.pyplot as plt  # Import Matplotlib for plotting

def check_strength(password):
    # Calculate the length score (max score is 10 for passwords with 10+ characters)
    length_score = min(len(password), 10)
    
    # Check if the password contains at least one uppercase letter
    upper = bool(re.search(r'[A-Z]', password))
    
    # Check if the password contains at least one lowercase letter
    lower = bool(re.search(r'[a-z]', password))
    
    # Check if the password contains at least one digit
    digit = bool(re.search(r'\d', password))
    
    # Check if the password contains at least one special character
    special = bool(re.search(r'[@$!%*?&]', password))

    # Initialize the score with the length score
    score = length_score
    
    # Add 2 points if the password contains an uppercase letter
    score += 2 if upper else 0
    
    # Add 2 points if the password contains a lowercase letter
    score += 2 if lower else 0
    
    # Add 2 points if the password contains a digit
    score += 2 if digit else 0
    
    # Add 4 points if the password contains a special character
    score += 4 if special else 0

    # Return the total score and a breakdown of the scores
    return score, {
        'Length': length_score,  # Length score
        'Uppercase': 2 if upper else 0,  # Uppercase letter score
        'Lowercase': 2 if lower else 0,  # Lowercase letter score
        'Digit': 2 if digit else 0,  # Digit score
        'Special': 4 if special else 0,  # Special character score
    }

def plot_strength(details, password):
    # Extract the categories (e.g., Length, Uppercase) and their scores
    categories = list(details.keys())
    values = list(details.values())

    # Create a bar chart to visualize the password strength breakdown
    plt.figure(figsize=(8, 5))  # Set the figure size
    bars = plt.bar(categories, values, color='teal')  # Create the bar chart
    plt.title(f"Password Strength Breakdown: '{password}'")  # Set the chart title
    plt.ylabel("Score")  # Label the y-axis
    plt.ylim(0, 10)  # Set the y-axis limit (max score per category is 10)
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)  # Add a grid for better readability

    # Add the score values on top of each bar
    for bar in bars:
        yval = bar.get_height()  # Get the height of the bar (score value)
        plt.text(bar.get_x() + 0.1, yval + 0.2, yval)  # Display the score above the bar

    plt.tight_layout()  # Adjust the layout to prevent overlap
    plt.show()  # Display the plot

# Example usage
password = input("Enter a password to test: ")  # Prompt the user to enter a password
score, breakdown = check_strength(password)  # Check the strength of the password
print(f"Total Score: {score}/20")  # Print the total score (out of 20)
plot_strength(breakdown, password)  # Plot the password strength breakdown