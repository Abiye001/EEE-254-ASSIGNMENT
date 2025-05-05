# 1. E-commerce checkout: Apply discounts
def apply_discount(total):
    if total >= 100:
        return total * 0.8  # 20% discount
    elif total >= 50:
        return total * 0.9  # 10% discount
    else:
        return total  # No discount

# 2. Grade calculator
def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"

# 3. Simple login system
def login(username, password):
    correct_username = "admin"
    correct_password = "1234"
    
    if username == correct_username and password == correct_password:
        return "Login successful!"
    elif username != correct_username:
        return "Username not found."
    else:
        return "Incorrect password."

# Test the functions
print("🛒 Discounted Total:", apply_discount(120))       # Output: 96.0
print("🎓 Grade:", calculate_grade(65))                 # Output: B
print("🔐 Login:", login("admin", "1234"))              # Output: Login successful!
