import re

class PasswordChecker:
    def __init__(self, password):
        self.password = password

    def is_strong(self):
        # Criteria 1: Check minimum length
        if len(self.password) < 8:
            return False

        # Criteria 2: Check for a mix of uppercase and lowercase letters
        if not re.search(r"[a-z]", self.password) or not re.search(r"[A-Z]", self.password):
            return False

        # Criteria 3: Check for at least one digit
        if not re.search(r"\d", self.password):
            return False

        # Criteria 4: Check for at least one special character
        if not re.search(r"[!@#$%^&*()\"'\/:;{}|?><,.]", self.password):
            return False

        return True

def main():
    password_input = input("Enter password: ")
    checker = PasswordChecker(password_input)
    if checker.is_strong():
        print("Strong password!")
    else:
        print("Weak password!")

if __name__ == "__main__":
    main()
