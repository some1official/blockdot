import string
import os

class ErrorMessage(Exception):
    pass

class fopen:

    def __init__(self, ffile_name, oopen_type):
        self.file_name = str(ffile_name)
        self.open_type = str(oopen_type)

        if(self.open_type=="0" or self.open_type=="create"):
            try:
                open(self.file_name, "x")
                self.open_type_id = "x"
            except IOError:
                raise ErrorMessage(f"Blockdot: File Already Exists (\"{self.file_name}\")")

        elif(self.open_type=="1" or self.open_type=="write"):
            open(self.file_name, "a")
            self.open_type_id = "w"

        elif(self.open_type=="2" or self.open_type=="append"):
            open(self.file_name, "a")
            self.open_type_id = "a"
        else:
            raise ErrorMessage(f"Blockdot: The Open Type is invalid! (\"{self.open_type}\")")


    def write(self, string):
        f = open(self.file_name, self.open_type_id)
        f.write(string)

    def close(self):
        f = open(self.file_name, self.open_type_id)
        f.close

    def read(self, number=-1):
        f = open(self.file_name, "r")
        
        if(number==-1):
            print(f.read())
        else:
            print(f.read(number))

    def readline(self, number=-1):
        f = open(self.file_name, "r")

        if(number==-1):
            print(f.readline())
        else:
            print(f.readline(number))

    def lines(self): #returns the numbers of lines in the file
        number_of_lines = len(open(self.file_name).readlines())
        return number_of_lines

    def characters(self, arg="None"): #returns the numbers of characters in the file
        
        arg = str(arg)
        if(arg == "None"):
            number_of_characters = len(open(self.file_name, "r").read())
            return number_of_characters
        elif(arg == "nospace"):
            number_of_characters = len(open(self.file_name, "r").read().replace(" ","").replace("\n",""))
            return number_of_characters
        else:
            raise ErrorMessage(f"Blockdot: Invalid Extra Argument (\"{arg}\")")

    
def fdelete(string):
    string = str(string) #converts the given variable 'string' to a string
    if os.path.exists(string):
        os.remove(string)
    else:
        raise ErrorMessage(f"Blockdot: File does not exists (\"{string}\")")