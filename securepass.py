import hashlib

password = input("Enter your password: ")

score = 0

if len(password) >= 8:
    score += 1

if any(char.isupper() for char in password):
    score += 1

if any(char.islower() for char in password):
    score += 1

if any(char.isdigit() for char in password):
    score += 1

if any(char in "!@#$%^&*()_+-=" for char in password):
    score += 1

if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Medium"
else:
    strength = "Strong"

hashed_password = hashlib.sha256(password.encode()).hexdigest()

print("\n===== SECUREPASS =====")
print("Password Strength:", strength)
print("Score:", score, "/ 5")
print("SHA-256 Hash:", hashed_password)