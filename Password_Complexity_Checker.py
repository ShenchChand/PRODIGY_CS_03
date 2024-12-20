import re

# Common weak passwords (dictionary example for validation)
COMMON_PASSWORDS = ["123456", "password", "qwerty", "abc123", "letmein", "welcome"]

def assess_password_strength(password):
    """Assess the strength of a password and provide feedback."""
    strength = 0
    feedback = []

    # Criteria 1: Length of the password
    if len(password) >= 16:
        strength += 3
        feedback.append("Excellent length (16+ characters).")
    elif len(password) >= 12:
        strength += 2
        feedback.append("Good length (12-15 characters).")
    elif len(password) >= 8:
        strength += 1
        feedback.append("Fair length (8-11 characters). Consider using 12+.")
    else:
        feedback.append("Too short. Use at least 12 characters.")

    # Criteria 2: Uppercase and lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        strength += 2
        feedback.append("Has both uppercase and lowercase letters.")
    else:
        feedback.append("Add both uppercase and lowercase letters.")

    # Criteria 3: Digits
    if re.search(r'[0-9]', password):
        strength += 1
        feedback.append("Includes numbers.")
    else:
        feedback.append("Add some numbers.")

    # Criteria 4: Special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 2
        feedback.append("Includes special characters.")
    else:
        feedback.append("Add special characters like !@#$%.")

    # Criteria 5: Common patterns and dictionary matches
    if password.lower() in COMMON_PASSWORDS or re.search(r'(123|password|qwerty|letmein|abc)', password.lower()):
        strength -= 3
        feedback.append("Avoid common patterns or weak passwords like '123456' or 'password'.")

    # Criteria 6: Sequential or repeated characters
    if re.search(r'(.)\1\1', password):
        strength -= 2
        feedback.append("Avoid repeated characters (e.g., 'aaa').")
    if re.search(r'(1234|abcd|qwerty)', password.lower()):
        strength -= 2
        feedback.append("Avoid sequential patterns like '1234' or 'abcd'.")

    # Determine overall strength level
    if strength >= 8:
        status = "Strong"
    elif 5 <= strength < 8:
        status = "Moderate"
    else:
        status = "Weak"

    return {
        "strength": strength,
        "status": status,
        "feedback": feedback
    }

if __name__ == "__main__":
    print("Password Strength Assessment Tool")
    user_password = input("Enter your password: ")

    result = assess_password_strength(user_password)

    print(f"\nPassword Strength: {result['status']} (Score: {result['strength']}/10)")
    print("Feedback:")
    for item in result['feedback']:
        print(f"- {item}")
