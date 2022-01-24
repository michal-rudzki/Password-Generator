from random import randrange
from gen import PasswordGenerator

def main():
    password = ""
    p = PasswordGenerator(length=12, lowercase=True, uppercase=True, numbers=True, special=False)
    print(p.gen_password())
    
#    for x in range(12):
#        buff = chr(p.gen_lowercase())
#        password += buff
#    print("{}".format(password))
    
if __name__ == '__main__':
    main()