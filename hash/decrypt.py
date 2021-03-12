from translate import translate_from_id, translate_decrypt

def decrypt(string):
    n = len(string)
    dectrypted_string = ""
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