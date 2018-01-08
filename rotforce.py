"""
This is a Python3 script.

Usage:
python3 rotforce.py "Your message or ciphertext here!"
"""

import sys

upperCase = {ascii:chr(ascii) for ascii in range(65,91)}
lowerCase = {ascii:chr(ascii) for ascii in range(97,123)}
digit = {ascii:chr(ascii) for ascii in range(48,58)}

def rotateCipher(ciphertext, key):
    for character in ciphertext:
        asciichar = ord(character)
        # Do not change special characters
        if (asciichar not in upperCase and asciichar not in lowerCase) or asciichar in digit:
            yield asciichar
        else:
            # If it's in the upperCase case and that the rotation is within the upperCase
            if asciichar in upperCase and asciichar + key % 26 in upperCase:
                yield asciichar + key % 26
            # If it's in the lowerCase case and that the rotation is within the lowerCase
            elif asciichar in lowerCase and asciichar + key % 26 in lowerCase:
                yield asciichar + key % 26
            # Otherwise move back 26 spaces after rotation.
            else: # alphabet.
                yield asciichar + key % 26 -26

ciphertext = sys.argv[1]

print("============================================================\n")
print("%s written by brettyjames" % sys.argv[0])
print("Rotate Cipher Bruteforce for: %s. \n" % ciphertext)
print("============================================================\n")
for i in range(1,27): # The Bruteforce!!
    x = (''.join(map(chr, rotateCipher(ciphertext, i))))
    print("ROT{0} - {1} ...".format(i, x))

print("============================================================")
print("Bruteforce Complete.")
print("============================================================")
