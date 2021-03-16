import string
from src.translate import translate_to_id, translate_encrypt

#encrypts a strings
def encrypt(string):
    n = len(string)
    enctrypted_string = ""
    for i in range(0,n):
        letter = string[i]
        letter = translate_to_id(letter)
        enctrypted_string = enctrypted_string + translate_encrypt(letter)

    return enctrypted_string