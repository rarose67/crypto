#import the alphabet_position and rotate_character functions from the helpers module 
from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    """This function takes a message and an integer shift value, and use a caesar cipher to return an encrypted message."""

    encrypted = ""  #initialize the encrypted string
    for char in text:
        encrypted += rotate_character(char, rot) #for each letter in the message, call the rotate_character function then append the resulting character to the encrypted string

    return encrypted  #return the encrypted string


def main():
    from sys import argv, exit  #import the argv list and the exit function from the sys module 

     #If the user doesn't provide a command line argument, or that argument isn't a digit; print error message, then exit the program.
    if((len(argv) <= 1) or (argv[1].isdigit() == False)):
        print("usage: python caesar.py n")
        exit()

    message = input("Type a message:\n")  #prompt the user for message to encrypt
    rotate = int(argv[1])  #comvert the command line argument to an iteger.
    result = encrypt(message, rotate) #encrypt the message, and return the result

    print(result)  #output the encrypted message
    

if __name__ == "__main__":
    main()