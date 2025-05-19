print("\nLoading...")
import os
from matplotlib import pyplot as _pl
_CWD = os.getcwd()
os.chdir(os.path.split(__file__)[0])
from toolLib import (_CONF,
                     _Printer,
                     _Exit,
                     _title,
                     _run, _c)
from numpy.linalg import det, inv
os.chdir(_CWD)
# python-IDLE-Tools

## CONFIG ##
_CONF.CLEAR_ON_START = True
_CONF.CLEAR_ON_EXIT = True
_CONF.CONFIG_PATH = os.path.join(os.path.expanduser("~"), ".local", "share", ".IDLE-Tools")

## IMPORTS ##
from math import *
############

#### USER DEFINED FUNCTIONS ####
ln = lambda x: log(x, e)

def egcd(a, b, x=1, xx=0, y=0, yy=1):
    c = lambda a, b, q:(a-q*b)
    print(f"{a=}, {b=}, {x=}, {xx=}, {y=}, {yy=}")
    if b > 0:
        q = a//b
        egcd(b, c(a, b, q), xx, c(x, xx, q), yy, c(y, yy, q))
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

def draw(x:list, y:list):
    _pl.plot(x, y)
    _pl.savefig(os.path.join(_CONF.CONFIG_PATH, "plot.png"), transparent=True)
    os.system("kitten icat --clear --transfer-mode=memory --stdin=no "+os.path.join(_CONF.CONFIG_PATH, "plot.png"))

class Vec3:
    def __init__(self, a, b, c):
        self._vec = [a, b, c]
        self.normalize = self.nor # alias
    def size(self) -> str:
        return f"{len(self._vec)}x{1}"
    def nor(self):
        if self.length() < 1:
            return self.copy()
        return Vec3(
            self._vec[0] / self.length(),
            self._vec[1] / self.length(),
            self._vec[2] / self.length()
        )
    def length(self):
        return sqrt(pow(self._vec[0], 2)+pow(self._vec[1], 2)+pow(self._vec[2], 2))
    def clone(self):
        return Vec3(
            self._vec[0],
            self._vec[1],
            self._vec[2]
        )
    def round(self, n=4):
        v1 = self.clone()
        v1._vec[0] = round(v1._vec[0], n)
        v1._vec[1] = round(v1._vec[1], n)
        v1._vec[2] = round(v1._vec[2], n)
        return v1
    def __len__(self):
        return self.length()
    def __add__(self, other):
        if isinstance(other, Vec3):
            return Vec3(
                self._vec[0] + other._vec[0],
                self._vec[1] + other._vec[1],
                self._vec[2] + other._vec[2],
                )
        else:
            raise NotImplemented()
    def __ne__(self, other):
        if isinstance(other, Vec3):
            return Vec3(
                self._vec[0] - other._vec[0],
                self._vec[1] - other._vec[1],
                self._vec[2] - other._vec[2],
                )
        else:
            raise NotImplemented()
    def __mul__(self, other):
        if isinstance(other, int):
            return Vec3(
                self._vec[0] * other,
                self._vec[1] * other,
                self._vec[2] * other,
                )
        else:
            raise NotImplemented()
    def __repr__(self):
        return f"({self._vec[0]}, {self._vec[1]}, {self._vec[2]})"
    def draw(self):
        _pl.rcParams['grid.color'] = "white"
        fig = _pl.figure()
        ax = fig.add_subplot(111, projection='3d')

        # VECTOR 1
        ax.quiver(0, 0, 0, self._vec[0], self._vec[1], self._vec[2], color='r', arrow_length_ratio=0.1)

        ax.set_xlim([-3, 3])
        ax.set_ylim([-3, 3])
        ax.set_zlim([-3, 3])

        ax.set_xlabel('X', color='white')
        ax.set_ylabel('Y', color='white')
        ax.set_zlabel('Z', color='white')

        ax.xaxis.pane.fill = False
        ax.yaxis.pane.fill = False
        ax.zaxis.pane.fill = False

        ax.xaxis.pane.set_edgecolor('w')
        ax.yaxis.pane.set_edgecolor('w')
        ax.zaxis.pane.set_edgecolor('w')

        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.tick_params(axis='z', colors='white')

        fig.savefig(os.path.join(_CONF.CONFIG_PATH, "plot.png"), transparent=True)
        os.system("kitten icat --clear --transfer-mode=memory --stdin=no " + os.path.join(_CONF.CONFIG_PATH, "plot.png"))
class Mat:
    def __init__(self, *a):
        self._mat = [[0]]
        if not a: return
        if len(a) == 1:
            a = a[0]
            if type(a) is list:
                self._mat = a.copy()
            elif type(a) is str:
                if type(a) is str and a.count("x") == 1:
                    h, w = a.replace(" ", "").split("x")
                    self._mat = [[] for _ in range(int(h))]
                    row = 0
                    for i in range(int(h)*int(w)):
                        self._mat[row].append(0)
                        if (i + 1) % int(w) == 0:
                            row += 1
            else:
                print(_c.RED+"Invalid input for Matrix."+_c.RESET)
        else:
            size = a[-1]
            if type(size) is str and size.count("x") == 1:
                h, w = size.replace(" ", "").split("x")
                self._mat = [[] for _ in range(int(h))]
                if h.isnumeric() and w.isnumeric():
                    if int(h) * int(w) != len(a)-1:
                        print(_c.RED+f"Invalid Parameter-Length. Must be {int(h) * int(w)} numbers. Got {len(a)-1}."+_c.RESET)
                        return
                    row = 0
                    for i, j in enumerate(a[:-1]):
                        self._mat[row].append(j)
                        if (i+1) % int(w) == 0:
                            row += 1
                else:
                    print(_c.RED+"Invalid type/format last Param. Must be str in format: \"2x3\""+_c.RESET)
            else:
                print(_c.RED+"Invalid type/format last Param. Must be str in format: \"2x3\""+_c.RESET)
    def size(self) -> str:
        return f"{len(self._mat)}x{len(self._mat[0])}"
    def transpose(self):
        h, w = self.size().split("x")
        _mat = [[0 for _ in range(int(h))] for _ in range(int(w))]
        for i in range(int(h)):
            for j in range(int(w)):
                _mat[j][i] = self._mat[i][j]
        self._mat = _mat
        return self
    def fill(self, num:int):
        mat = self.clone()
        m, n = mat.size().split("x")
        for x in range(int(m)):
            for y in range(int(n)):
                mat._mat[x][y] = num
        return mat
    def det(self)->int:
        return det(self._mat)
    def inv(self):
        return Mat(list(i) for i in inv(self._mat))
    def clone(self):
        return Mat([i.copy() for i in self._mat])
    def round(self, n):
        mat = Mat(self.size())
        for indx, i in zip(range(len(self._mat)), self):
            for indy, k in zip(range(len(i)), i):
                mat[indx][indy] = round(self[indx][indy], n)
        return mat
    def __repr__(self):
        s = []
        l = []
        for x in range(len(self._mat[0])):
            _l = 0
            for y in range(len(self._mat)):
                _l = len(str(self[y][x])) if len(str(self[y][x])) > _l else _l
            l.append(_l)
        for r in self._mat:
            s.append("│"+" ".join([str(i).rjust(l[le], " ") for le, i in enumerate(r)])+"│")
        s.insert(0, "┌"+" "*(len(s[0])-2)+"┐")
        s.append("└"+" "*(len(s[0])-2)+"┘")
        return "\n".join(s)
    def __getitem__(self, item):
        return self._mat[item]
    def __add__(self, other):
        if not isinstance(other , Mat):
            print(_c.RED + f"Type does not match! Cannot add {type(self)} and {type(other)}" + _c.RESET)
            return
        if self.size() != other.size():
            print(_c.RED+f"Size does not match! Cannot add {self.size()} and {other.size}"+_c.RESET)
            return 0
        mat = Mat(self.size())
        for indx, i, j in zip(range(len(self._mat)), self, other):
            for indy, k, l in zip(range(len(i)), i, j):
                mat[indx][indy] = k + l
        return mat
    def __ne__(self, other):
        if not isinstance(other , Mat):
            print(_c.RED + f"Type does not match! Cannot add {type(self)} and {type(other)}" + _c.RESET)
            return
        if self.size() != other.size():
            print(_c.RED+f"Size does not match! Cannot add {self.size()} and {other.size}"+_c.RESET)
            return 0
        mat = Mat(self.size())
        for indx, i, j in zip(range(len(self._mat)), self, other):
            for indy, k, l in zip(range(len(i)), i, j):
                mat[indx][indy] = k - l
        return mat
    def __mul__(self, other):
        if type(other) is int:
            mat = Mat(self.size())
            for indx, i in zip(range(len(self._mat)), self):
                for indy, k in zip(range(len(i)), i):
                    mat[indx][indy] = k*other
            return mat
        elif isinstance(other, Mat):
            if self.size().split("x")[1] == other.size().split("x")[0]:
                mat = Mat(f"{self.size().split('x')[0]}x{other.size().split('x')[1]}")

                for i in range(len(self._mat)):
                    for j in range(len(other._mat[0])):
                        for k in range(len(other._mat)):
                            mat[i][j] += self._mat[i][k] * other._mat[k][j]

                return mat
            else:
                print(_c.RED + f"Cannot multiply! Size does not Match: {self.size()} and {other.size()}" + _c.RESET)
        else:
            print(_c.RED + f"Type does not match! Cannot multiply {type(self)} and {type(other)}" + _c.RESET)
    def __pow__(self, power, modulo=None):
        if type(power) is int:
            mat = Mat(self.size())
            for indx, i in zip(range(len(self._mat)), self):
                for indy, k in zip(range(len(i)), i):
                    mat[indx][indy] = k**power
            return mat
        print(_c.RED + f"Cannot pow! Type does not Match: {type(self)} and {type(power)}" + _c.RESET)
class Mati(Mat):
    def __init__(self, size:str):
        super().__init__(size)
        n, m = size.split("x")
        if n != m:
            print(f"Wrong size! {n}x{m}")
            return
        for n in range(int(m)):
            self._mat[n][n] = 1

#### USER DEFINED COMMANDS ####
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
    ] if _CONF.CLEAR_ON_START else [lambda: os._exit(0)]
)
if __name__ == '__main__':
    if not os.path.exists(_CONF.CONFIG_PATH):
        os.mkdir(_CONF.CONFIG_PATH)
    _run()
