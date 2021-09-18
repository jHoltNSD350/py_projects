import pyperclip as pcl, sys, string as s, random as r
from random import sample

def generate_password():
    if len(sys.argv) == 1:
        length = input('Enter password length: ')
    else:
        length = sys.argv[1]

    print('Generating password...')

    chars = s.ascii_letters + s.digits + s.punctuation
    temp = r.choices(chars, k=int(length))
    password = ''.join(temp)
    pcl.copy(password)

    print('Password copied to clipboard')

def main():
    generate_password()

if __name__ == '__main__':
    main()
