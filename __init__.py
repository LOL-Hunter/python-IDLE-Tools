import os
_CWD = os.getcwd()
os.chdir(os.path.split(__file__)[0])
from toolLib import (_CONF,
                     _Printer,
                     _Exit,
                     _title,
                     _lock,
                     _run)

# python-IDLE-Tools

## CONFIG ##
_CONF._CLEAR_ON_START = True
_CONF._CLEAR_ON_EXIT = True
_CONF._CAN_EXIT_CTRL_C = True

## IMPORTS ##
from math import *
############

#### USER DEFINED FUNCTIONS ####
def egcd(a, b, x=1, xx=0, y=0, yy=1, printStep=False):
   c = lambda a, b, q:(a-q*b)

   if printStep: print(f"{a=}, {b=}, {x=}, {xx=}, {y=}, {yy=}")
   if b > 0:
       q = a//b
       egcd(b, c(a, b, q), xx, c(x, xx, q), yy, c(y, yy, q), printStep)
   else:
        return x

def isbn10(isbn:str)->bool:
    if len(isbn) != 10:
        print("isbn is not length 10.")
        return False
    _isbnArr = [int(j)*(10-i) for i, j in enumerate(isbn)]
    return sum(_isbnArr)%11 == 0

def isbn13(isbn:str)->bool:
    if len(isbn) != 13:
        print("isbn is not length 13.")
        return False
    _sum = 0
    for i, j in enumerate(isbn):
        _sum += int(j) * (1 if i%2==0 else 3)
    return _sum%10 == 0

def isbn10x(isbn:str)->int:
    if len(isbn) != 9:
        print("isbn is not length 9.")
        return False
    _isbnArr = [int(j)*(10-i) for i, j in enumerate(isbn)]
    return sum(_isbnArr)%11 == 0


#### USER  DEFINED COMMANDS ####
clear = cls = _Printer(
    commands=[
        _title
    ],
    return_="",
    desc="",
    usage=""
)
exit = _Exit(
    commands=[
        lambda: os.system("clear"),
        lambda: os._exit(0)
    ] if _CONF._CLEAR_ON_START else [lambda: os._exit(0)]
)
if __name__ == '__main__':
    _run()