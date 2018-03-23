#import the alphabet_position and rotate_character functions from the helpers module 
from helpers import alphabet_position, rotate_character

def encrypt(text, key):
    """This function takes a message and an encyption key, and use a vigenere cipher to return an encrypted message."""

    encrypted = ""  #initialize the encrypted string
    shifts = []  #initialize the list of shift values
    index = 0  #initialize the shift list index counter

    for letter in key:
        shifts += [alphabet_position(letter)]  #for each letter in the key, call the alphabet_position function then append the resulting number to the shifts list

    for char in text: 
        if (char == " ") or not(char.isalpha()):  #if the current character is a space or non-alphabetic, then append it to the encrypted string
            encrypted += char 
        else:  #otherwise
            #for each character in the message, call the rotate_character functio with arguments of the that character the item in the shifts list at the current index 
            #then append the resulting character to the encrypted string
            new_char = rotate_character(char, shifts[index])
            encrypted += new_char
            index = ((index + 1) % len(shifts))  # add 1 to index, if it is then equal to the length of the shifts list, the cycle back to the begining
            

    return encrypted   #return the encrypted string


def main():
    from sys import argv, exit #import the argv list and the exit function from the sys module 

    #If the user doesn't provide a command line argument, or that argument contains non-alphabetic characters; print error message, then exit the program.
    if((len(argv) <= 1) or (argv[1].isalpha() == False)):
        print("usage: python vigenere.py keyword\n\n" + 
        "Arguments:\n\n" +
        """-keyword : The string to be used as a "key" to encrypt your message. Should only contain alphabetic characters-- no numbers or special characters.""")
        exit()

    message = input("Type a message:\n") #prompt the user for message to encrypt
    key = str(argv[1])

    result = encrypt(message, key) #encrypt the message, and return the result

    print(result)  #output the encrypted message

if __name__ == "__main__":
    main()