def alphabet_position(letter):
    """This function takes a letter, and returns it's position in the alphabet.  a is considered to be at position 0 """

    alphabet = "abcdefghijklmnopqrstuvwxyz"  #initialize the in the alphabet string.

    return (alphabet.find(letter.lower()))  #convert the leter to lowercase and retun it's position in the in the alphabet string.

def rotate_character(char, rot):
    """This function takes a character and an integer shift value(rot), and returns the character which is rot places to right  """

    alphabet = "abcdefghijklmnopqrstuvwxyz"  #initialize the in the alphabet string.

    if ((char not in alphabet) and (char not in alphabet.upper())):  #If the character is non-alphabetic, return it unchanged
        return char

    pos = alphabet_position(char)  #determine the character's position
    new_pos = (pos + rot) % 26  #shift the character right by rot places, if you reach the end of the alphabet, cycle back to the begining.
    new_char = alphabet[new_pos]  #get the character at the new position

    if (char == alphabet[pos].upper()):  #If the original character was uppercase, convert the shifted character to uppercase.
        new_char = new_char.upper()
    
    return new_char