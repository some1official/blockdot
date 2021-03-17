import string
import random
from src.captcha_trying import *

#verify if a user is robot or not
def captcha():
    string = captcha_string() #randomly generated string, that the user will need to type to get verified
    print(f"Verify that you are a robot. Enter the following string: \"{string}\"")
    print("Enter:", end="")
    try_string = str(input())

    #if the string entered by the user is incorrect
    if(try_string!=string):
        captcha_trying(captcha_string())