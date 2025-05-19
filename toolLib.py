import os, sys
from colorama import init as _init, Fore as _c

_init()
VERSION = 1.8

def _run():
    try:
        if _lock():
            _title(True)
    except KeyboardInterrupt:
        os._exit(0)


class _CONF:
    CLEAR_ON_START = None
    CLEAR_ON_EXIT = None
    CAN_EXIT_CTRL_C = None
    CONFIG_PATH = None

def _lock():
    _lockVar = os.environ.get("RUN_LOCK", "false")
    if _lockVar == "false":
        os.environ["RUN_LOCK"] = "true"
        return True
    return False

def _title(_s=False):
    if not _s or _CONF.CLEAR_ON_START: os.system("clear")
    c = sys.version_info
    print(_c.GREEN+f"Python-{c.major}.{c.minor}.{c.micro}"+_c.RESET)
    print(_c.GREEN+f"IDLE-Tool-Version: {VERSION} | \u00A9 Robert Langhammmer"+_c.RESET)


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
