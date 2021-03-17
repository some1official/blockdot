import string
from src.alphabet import * 

#translates characters to id
def translate_to_id(char):
    char = str(char)
    if(char=="a"):
        return a
    elif(char=="b"):
        return b
    elif(char=="c"):
        return c
    elif(char=="d"):
        return d
    elif(char=="e"):
        return e
    elif(char=="f"):
        return f
    elif(char=="g"):
        return g
    elif(char=="h"):
        return h
    elif(char=="i"):
        return i
    elif(char=="j"):
        return j
    elif(char=="k"):
        return k
    elif(char=="l"):
        return l
    elif(char=="m"):
        return m
    elif(char=="n"):
        return n
    elif(char=="o"):
        return o
    elif(char=="p"):
        return p
    elif(char=="q"):
        return q
    elif(char=="r"):
        return r
    elif(char=="s"):
        return s
    elif(char=="t"):
        return t
    elif(char=="u"):
        return u
    elif(char=="v"):
        return v
    elif(char=="w"):
        return w
    elif(char=="x"):
        return x
    elif(char=="y"):
        return y
    elif(char=="z"):
        return z
    elif(char=="A"):
        return A
    elif(char=="B"):
        return B
    elif(char=="C"):
        return C
    elif(char=="D"):
        return D
    elif(char=="E"):
        return E
    elif(char=="F"):
        return F
    elif(char=="G"):
        return G
    elif(char=="H"):
        return H
    elif(char=="I"):
        return I
    elif(char=="J"):
        return J
    elif(char=="K"):
        return K
    elif(char=="L"):
        return L
    elif(char=="M"):
        return M
    elif(char=="N"):
        return N
    elif(char=="O"):
        return O
    elif(char=="P"):
        return P
    elif(char=="Q"):
        return Q
    elif(char=="R"):
        return R
    elif(char=="S"):
        return S
    elif(char=="T"):
        return T
    elif(char=="U"):
        return U
    elif(char=="V"):
        return V
    elif(char=="W"):
        return W
    elif(char=="X"):
        return X
    elif(char=="Y"):
        return Y
    elif(char=="Z"):
        return Z
    elif(char=="0"):
        return zero
    elif(char=="1"):
        return one
    elif(char=="2"):
        return two
    elif(char=="3"):
        return three
    elif(char=="4"):
        return four
    elif(char=="5"):
        return five
    elif(char=="6"):
        return six
    elif(char=="7"):
        return seven
    elif(char=="8"):
        return eight
    elif(char=="9"):
        return nine
    elif(char=="?"):
        return question_mark
    elif(char==" "):
        return space
    elif(char=="!"):
        return exclamation_mark
    elif(char=="."):
        return dot
    else:
        return None

def translate_from_id(id):
    if(id==0):
        return "a"
    elif(id==1):
        return "b"
    elif(id==2):
        return "c"
    elif(id==3):
        return "d"
    elif(id==4):
        return "e"
    elif(id==5):
        return "f"
    elif(id==6):
        return "g"
    elif(id==7):
        return "h"
    elif(id==8):
        return "i"
    elif(id==9):
        return "j"
    elif(id==10):
        return "k"
    elif(id==11):
        return "l"
    elif(id==12):
        return "m"
    elif(id==13):
        return "n"
    elif(id==14):
        return "o"
    elif(id==15):
        return "p"
    elif(id==16):
        return "q"
    elif(id==17):
        return "r"
    elif(id==18):
        return "s"
    elif(id==19):
        return "t"
    elif(id==20):
        return "u"
    elif(id==21):
        return "v"
    elif(id==22):
        return "w"
    elif(id==23):
        return "x"
    elif(id==24):
        return "y"
    elif(id==25):
        return "z"
    elif(id==26):
        return "A"
    elif(id==27):
        return "B"
    elif(id==28):
        return "C"
    elif(id==29):
        return "D"
    elif(id==30):
        return "E"
    elif(id==31):
        return "F"
    elif(id==32):
        return "G"
    elif(id==33):
        return "H"
    elif(id==34):
        return "I"
    elif(id==35):
        return "J"
    elif(id==36):
        return "K"
    elif(id==37):
        return "L"
    elif(id==38):
        return "M"
    elif(id==39):
        return "N"
    elif(id==40):
        return "O"
    elif(id==41):
        return "P"
    elif(id==42):
        return "Q"
    elif(id==43):
        return "R"
    elif(id==44):
        return "S"
    elif(id==45):
        return "T"
    elif(id==46):
        return "U"
    elif(id==47):
        return "V"
    elif(id==48):
        return "W"
    elif(id==49):
        return "X"
    elif(id==50):
        return "Y"
    elif(id==51):
        return "Z"
    elif(id==52):
        return "0"
    elif(id==53):
        return "1"
    elif(id==54):
        return "2"
    elif(id==55):
        return "3"
    elif(id==56):
        return "4"
    elif(id==57):
        return "5"
    elif(id==58):
        return "6"
    elif(id==59):
        return "7"
    elif(id==60):
        return "8"
    elif(id==61):
        return "9"
    elif(id==62):
        return "?"
    elif(id==63):
        return " "
    elif(id==64):
        return "!"
    elif(id==65):
        return "."

def translate_encrypt(id):
    if(id==0):
        return "hjb"
    elif(id==1):
        return "dsv"
    elif(id==2):
        return "b1d"
    elif(id==3):
        return "ewv"
    elif(id==4):
        return "ffd"
    elif(id==5):
        return "wev"
    elif(id==6):
        return "b2b"
    elif(id==7):
        return "43b"
    elif(id==8):
        return "2bf"
    elif(id==9):
        return "bg8"
    elif(id==10):
        return "bfd"
    elif(id==11):
        return "bd9"
    elif(id==12):
        return "fb2"
    elif(id==13):
        return "b10"
    elif(id==14):
        return "as1"
    elif(id==15):
        return "jf4"
    elif(id==16):
        return "ek2"
    elif(id==17):
        return "mv3"
    elif(id==18):
        return "bk9"
    elif(id==19):
        return "kbf"
    elif(id==20):
        return "jsm"
    elif(id==21):
        return "ibm"
    elif(id==22):
        return "iem"
    elif(id==23):
        return "mve"
    elif(id==24):
        return "im3"
    elif(id==25):
        return "vm1"
    elif(id==26):
        return "843"
    elif(id==27):
        return "nb3"
    elif(id==28):
        return "dm2"
    elif(id==29):
        return "mb3"
    elif(id==30):
        return "mb8"
    elif(id==31):
        return "vda"
    elif(id==32):
        return "mkb"
    elif(id==33):
        return "mus"
    elif(id==34):
        return "mb6"
    elif(id==35):
        return "65m"
    elif(id==36):
        return "mbd"
    elif(id==37):
        return "nbs"
    elif(id==38):
        return "sfa"
    elif(id==39):
        return "dpa"
    elif(id==40):
        return "mid"
    elif(id==41):
        return "a53"
    elif(id==42):
        return "8gm"
    elif(id==43):
        return "jb7"
    elif(id==44):
        return "yus"
    elif(id==45):
        return "m02"
    elif(id==46):
        return "abd"
    elif(id==47):
        return "7a3"
    elif(id==48):
        return "75a"
    elif(id==49):
        return "92r"
    elif(id==50):
        return "m89"
    elif(id==51):
        return "mao"
    elif(id==52):
        return "k34"
    elif(id==53):
        return "lks"
    elif(id==54):
        return "vhd"
    elif(id==55):
        return "meb"
    elif(id==56):
        return "m6m"
    elif(id==57):
        return "8mv"
    elif(id==58):
        return "mk3"
    elif(id==59):
        return "84j"
    elif(id==60):
        return "yfs"
    elif(id==61):
        return "kms"
    elif(id==62):
        return "m8s"
    elif(id==63):
        return "mav"
    elif(id==64):
        return "lsa"
    elif(id==65):
        return "m8a"
    else:
        return None

def translate_decrypt(string):
    if(string=="hjb"):
        return 0
    elif(string=="dsv"):
        return 1
    elif(string=="b1d"):
        return 2
    elif(string=="ewv"):
        return 3
    elif(string=="ffd"):
        return 4
    elif(string=="wev"):
        return 5
    elif(string=="b2b"):
        return 6
    elif(string=="43b"):
        return 7
    elif(string == "2bf"):
        return 8
    elif(string=="bg8"):
        return 9
    elif(string=="bfd"):
        return 10
    elif(string=="bd9"):
        return 11
    elif(string=="fb2"):
        return 12
    elif(string=="b10"):
        return 13
    elif(string=="as1"):
        return 14
    elif(string=="jf4"):
        return 15
    elif(string=="ek2"):
        return 16
    elif(string=="mv3"):
        return 17
    elif(string=="bk9"):
        return 18
    elif(string=="kbf"):
        return 19
    elif(string=="jsm"):
        return 20
    elif(string=="ibm"):
        return 21
    elif(string=="iem"):
        return 22
    elif(string=="mve"):
        return 23
    elif(string=="im3"):
        return 24
    elif(string=="vm1"):
        return 25
    elif(string=="843"):
        return 26
    elif(string=="nb3"):
        return 27
    elif(string=="dm2"):
        return 28
    elif(string=="mb3"):
        return 29
    elif(string=="mb8"):
        return 30
    elif(string=="vda"):
        return 31
    elif(string=="mkb"):
        return 32
    elif(string=="mus"):
        return 33
    elif(string=="mb6"):
        return 34
    elif(string=="65m"):
        return 35
    elif(string=="mbd"):
        return 36
    elif(string=="nbs"):
        return 37
    elif(string=="sfa"):
        return 38
    elif(string=="dpa"):
        return 39
    elif(string=="mid"):
        return 40
    elif(string=="a53"):
        return 41
    elif(string=="8gm"):
        return 42
    elif(string=="jb7"):
        return 43
    elif(string=="yus"):
        return 44
    elif(string=="m02"):
        return 45
    elif(string=="abd"):
        return 46
    elif(string=="7a3"):
        return 47
    elif(string=="75a"):
        return 48
    elif(string=="92r"):
        return 49
    elif(string=="m89"):
        return 50
    elif(string=="mao"):
        return 51
    elif(string=="k34"):
        return 52
    elif(string=="lks"):
        return 53
    elif(string=="vhd"):
        return 54
    elif(string=="meb"):
        return 55
    elif(string=="m6m"):
        return 56
    elif(string=="8mv"):
        return 57
    elif(string=="mk3"):
        return 58
    elif(string=="84j"):
        return 59
    elif(string=="yfs"):
        return 60
    elif(string=="kms"):
        return 61
    elif(string=="m8s"):
        return 62
    elif(string=="mav"):
        return 63
    elif(string=="lsa"):
        return 64
    elif(string=="m8a"):
        return 65
    else:
        return None
