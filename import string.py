import string

def check_password_strength(password):
    score = 0
    remarks = []

    # Criteria checks
    if len(password) >= 8:
        score += 1
    else:
        remarks.append("Password should be at least 8 characters long.")

    if any(char.islower() for char in password):
        score += 1
    else:
        remarks.append("Include lowercase letters.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        remarks.append("Include uppercase letters.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        remarks.append("Include numbers.")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        remarks.append("Include special characters (e.g., @, #, $, %).")

    # Strength level
    if score == 5:
        strength = "Strong"
    elif 3 <= score < 5:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, remarks

# Example usage
password = input("Enter your password: ")
strength, feedback = check_password_strength(password)

print(f"\nPassword Strength: {strength}")
if feedback:
    print("Suggestions to improve your password:")
    for tip in feedback:
        print(f"- {tip}")