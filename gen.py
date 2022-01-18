from random import randrange

"""    
    lowercase: [97, 122]
    uppercase: [65, 90]
    numbers: [48, 57]
    special: [[33,47],[91,96],[123,126]]
"""

class PasswordGenerator:
    
    def gen_password(lowercase=True, uppercase=True):
        password = ""
                
    def gen_lowercase():
        return randrange(97, 122)
    
    def gen_uppercase():
        return randrange(65, 90)
    
    def gen_numbers():
        return randrange(48, 57)
    
    def gen_special_char():
        if randrange(1,3) == 1:
            return randrange(33,47)
        elif randrange(1,3) == 2:
            return randrange(91,96)
        else:
            return randrange(123,126)