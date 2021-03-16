import random

def generate_password(length): #generates a random passwords
    char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!"
    password = ""
    for i in range(0,length):
        password = password + random.choice(char)
    return password

def check_password(password):
    points = 0
    password = str(password) #converts the password into a string

    #checks for very weak passwords
    if(password.lower()=="password"):
        return points
    elif(password == "1234567890"):
        return points
    elif(password.lower()=="admin"):
        return points

    has_lower = False #is True if the password contains lowercase characters
    has_upper = False #is True if the password contains uppercase characters
    has_digit = False #is True if the password contains digits
    has_special_characters = False #is True if the password contains special characters

    for i in password:

        #checks if the password contains uppercase characters
        if i.isupper() == True and has_upper == False:
            has_upper = True

        #checks if the password contains lowercase characters
        if i.islower() == True and has_lower == False:
            has_lower = True

        #checks if the password contains digits
        if i.isdigit() == True and has_digit == False:
            has_digit = True

        #checks if the password contains special characters
        if (i == "!"  or i == "?") and has_special_characters == False:
            has_special_characters = True


    #adds points for every layer of the security of the password
    if(has_lower == True and has_upper == True):
        points = points + 1
    if(has_digit == True):
        points = points + 1
    if(has_special_characters == True):
        points = points + 1
    if(len(password)>=16):
        points = points + 1
    if(len(password)>=32):
        points = points + 1

    return points