import string
import random

'''
if the user doesn't get the captcha right in the first time this functions loops itself until 
the user enters the corect string
'''
def captcha_trying(string):
    print("Invalid Captcha!")
    print(f"Verify that you are a robot. Enter the following string: \"{string}\"")
    print("Enter:",end="")
    try_number = str(input())
    
    #runs the function again if the string that the user entered is incorect
    if(try_number != string):
        #generates a new string that the user will need to type to get verified
        captcha_trying(captcha_string())
    
def captcha_string(): #generates string that will be used by captcha
    char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!"
    string = ""
    for i in range(0,8):
        string = string + random.choice(char)
    return string
