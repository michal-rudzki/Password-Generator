from random import randrange, randint

"""    
    lowercase: [97, 122]
    uppercase: [65, 90]
    numbers: [48, 57]
    special: [[33,47],[91,96],[123,126]]
"""

class PasswordGenerator:
    
    def __init__(self, length=1, lowercase=True, uppercase=True, \
        numbers=True, special=False):
        self.length = length
        self.lowercase = lowercase
        self.uppercase = uppercase
        self.numbers = numbers
        self.special = special
    
    def gen_password(self):
        password = []
        DEBUG = False
        if DEBUG == True:
            print(f"length: {self.length}")
            print(f"lowercase: {self.lowercase}")
            print(f"uppercase: {self.uppercase}")
            print(f"numbers: {self.numbers}")
            print(f"special: {self.numbers}")
            
        for l in range(self.length):
            if self.lowercase == True:
                password.append(chr(self.gen_lowercase()))
            if self.uppercase == True:
                password.append(chr(self.gen_uppercase()))
            if self.numbers == True:
                password.append(chr(self.gen_numbers()))
            if self.special == True:
                password.append(chr(self.gen_special()))
        return (f"Password: {password}")
                
    def gen_lowercase(self):
        return randrange(97, 122)
    
    def gen_uppercase(self):
        return randrange(65, 90)
    
    def gen_numbers(self):
        return randrange(48, 57)
    
    def gen_special_char():
        if randrange(1,3) == 1:
            return randrange(33,47)
        elif randrange(1,3) == 2:
            return randrange(91,96)
        else:
            return randrange(123,126)