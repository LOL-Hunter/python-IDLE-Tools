
# python-IDLE-Tools

## CONFIG ##
_CLEAR_ON_START = True

## IMPORTS ##
from math import *
############










import sys, os
from colorama import init as _init, Fore as _c
def _lock():
    _lockVar = os.environ.get("RUN_LOCK", "false")
    if _lockVar == "false":
        os.environ["RUN_LOCK"] = "true"
        return True
    return False

def _title(_s=False):
    if not _s or _CLEAR_ON_START: os.system("clear")
    c = sys.version_info
    print(_c.GREEN+f"Python-{c.major}.{c.minor}.{c.micro}"+_c.RESET)
    print(_c.GREEN+f"Tool-Version: {VERSION} | \u00A9 Robert Langhammmer"+_c.RESET)
class _Printer:
    def __init__(self, commands=None, return_="", desc="", usage=""):
        self.commands = commands
        self.return_ = return_

    def __repr__(self):
        for i in self.commands:
            i()
        return self.return_
class _Exit(_Printer):
    def __init__(self, commands=None, return_="", desc="", usage=""):
        super().__init__(commands, return_, desc, usage)

    def __call__(self, *args, **kwargs):
        os._exit(0)
## commands ##
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
        lambda: os._exit(0)
    ]
)
if __name__ == '__main__':
    if _lock():
        _init()
        VERSION = 1.2
        _title(True)