import sys
import time

# sequential print function
def sprint(string, wait):
    wait = float(wait)
    for char in string:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(wait)

def main():
    noun = ''
    verb = ''
    person = ''
    sprint("test string", 0.2)

    input('Welcome to Mad-Libs! Press \'Enter\' to continue. . .')
    noun = input('Please enter a noun:   ')
    verb = input('Please enter a verb:   ')
    properNoun = input('Please enter a proper noun:   ')
    
    print(f'\nYour choices were:\n>>> noun - \'{noun}\'\n>>> verb - \'{verb}\'\n>>> proper noun - \'{properNoun}\'')
    input('Thank you for playing!!')
    
    
if __name__ == '__main__':
    main()
