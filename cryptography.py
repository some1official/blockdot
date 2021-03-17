import string
from src.translate import *

#decrypts a string
def decrypt(string):
    n = len(string)
    dectrypted_string = "" #the string that is decrypted
    for i in range(0,n):
        if(n-i<3):
            break
        letter = string[i] + string[i+1] + string[i+2]
        i = i + 2
        letter = translate_from_id(translate_decrypt(letter))
        if(letter == None):
            continue
        else:
            dectrypted_string = dectrypted_string + str(letter)

    return dectrypted_string

#encrypts a strings
def encrypt(string):
    n = len(string)
    enctrypted_string = ""
    for i in range(0,n):
        letter = string[i]
        letter = translate_to_id(letter)
        enctrypted_string = enctrypted_string + translate_encrypt(letter)

    return enctrypted_string