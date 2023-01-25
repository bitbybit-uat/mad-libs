import sys
import time

def sprint(string, wait):
    wait = float(wait)
    for char in string:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(wait)
    print('\n', end='')

def sinput(string, wait, ends): # ends >>> end separator as a string
    wait = float(wait)
    for char in string:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(wait)
    uInput = input(ends)
    return uInput

def main():
    sprint('Welcome to MadLibs!!', 0.05)
    sinput('Testing sinput', 0.1, ': ')

if __name__ == '__main__':
    main()
