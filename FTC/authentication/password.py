import re

class PasswordChecker:
    def __init__(self, password) :
        if not password:
            raise ValueError("You did not enter any password.")
        self.password = password
        
    def isstrong(self):
        
        if not re.search(r"[A-Z]", self.password) or not re.search(r"[a-z]", self.password):
            return False
        
        if len(self.password) < 8:
            return False
        
        if not re.search(r"[\d]", self.password):
            return False
        
        if not re.search(r"[!@#$%^&*()\"'\/:;{}|?><,.]", self.password):
            return False
        
        return True
    
def main():
    password = input("Enter your password ")
    passstrength = PasswordChecker(password)
    
    if passstrength.isstrong():
        print("The password is strong.")
        
    else:
        print("The password is weak.")
        
if __name__ == "__main__":
    main()