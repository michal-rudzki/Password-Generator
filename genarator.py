from random import randrange
from gen import PasswordGenerator

def main():
    p = PasswordGenerator(length=12, lowercase=True, uppercase=True, numbers=True, special=True)
    for x in range(10000):
        print("Your pass: {}".format(p.gen_password()))
    
if __name__ == '__main__':
    main()