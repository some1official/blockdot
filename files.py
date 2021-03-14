import string

class ErrorMessage(Exception):
    pass

class bopen:

    def __init__(self, ffile_name, oopen_type):
        self.file_name = str(ffile_name)
        self.open_type = str(oopen_type)

        if(self.open_type=="0" or self.open_type=="create"):
            try:
                open(self.file_name, "x")
                self.open_type_id = "x"
            except IOError:
                raise ErrorMessage(f"Blockdot: File Already Exists ({self.file_name})")

        elif(self.open_type=="1" or self.open_type=="write"):
            open(self.file_name, "a")
            self.open_type_id = "w"

        elif(self.open_type=="2" or self.open_type=="append"):
            open(self.file_name, "a")
            self.open_type_id = "a"
        else:
            raise ErrorMessage(f"Blockdot: The Open Type is invalid! ({self.open_type})")


    def write(self, string):
        f = open(self.file_name, self.open_type_id)
        f.write(string)

    def close(self):
        f = open(self.file_name, self.open_type_id)
        f.close



f = bopen("test.txt", "append")
f.write("Something\n")
f.write("something")
f.write("something")
