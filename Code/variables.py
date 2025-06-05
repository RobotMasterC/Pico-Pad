from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

A = Keycode.A
B = Keycode.B
C = Keycode.C
D = Keycode.D
E = Keycode.E
F = Keycode.F
G = Keycode.G
H = Keycode.H
I = Keycode.I
J = Keycode.J
K = Keycode.K
L = Keycode.L
M = Keycode.M
N = Keycode.N
O = Keycode.O
P = Keycode.P
Q = Keycode.Q
R = Keycode.R
S = Keycode.S
T = Keycode.T
U = Keycode.U
V = Keycode.V
W = Keycode.W
X = Keycode.X
Y = Keycode.Y
Z = Keycode.Z

ZERO = Keycode.ZERO
ONE = Keycode.ONE
TWO = Keycode.TWO
THREE = Keycode.THREE
FOUR = Keycode.FOUR
FIVE = Keycode.FIVE
SIX = Keycode.SIX
SEVEN = Keycode.SEVEN
EIGHT = Keycode.EIGHT
NINE = Keycode.NINE

CTRL = Keycode.CONTROL
SHIFT = Keycode.SHIFT
ALT = Keycode.ALT
GUI = Keycode.GUI  # Windows key

LEFT = Keycode.LEFT_ARROW
RIGHT = Keycode.RIGHT_ARROW
UP = Keycode.UP_ARROW
DOWN = Keycode.DOWN_ARROW

ENTER = Keycode.ENTER
ESC = Keycode.ESCAPE
TAB = Keycode.TAB
SPACE = Keycode.SPACEBAR
BACKSPACE = Keycode.BACKSPACE
DELETE = Keycode.DELETE
HOME = Keycode.HOME
END = Keycode.END
PAGE_UP = Keycode.PAGE_UP
PAGE_DOWN = Keycode.PAGE_DOWN
F1 = Keycode.F1
F2 = Keycode.F2
F3 = Keycode.F3
F4 = Keycode.F4
F5 = Keycode.F5
F6 = Keycode.F6
F7 = Keycode.F7
F8 = Keycode.F8
F9 = Keycode.F9
F10 = Keycode.F10
F11 = Keycode.F11
F12 = Keycode.F12

_REPLACEMENTS = {
    "CONTROL": "CTRL",
    "LEFT_CONTROL": "CTRL",
    "RIGHT_CONTROL": "CTRL",
    "SHIFT": "SHIFT",
    "LEFT_SHIFT": "SHIFT",
    "RIGHT_SHIFT": "SHIFT",
    "ALT": "ALT",
    "LEFT_ALT": "ALT",
    "RIGHT_ALT": "ALT",
    "GUI": "WIN",
    "LEFT_GUI": "WIN",
    "RIGHT_GUI": "WIN",
    "ESCAPE": "ESC",
    "RETURN": "ENTER",
    "SPACEBAR": "SPACE",
    "LEFT_ARROW": "←",
    "RIGHT_ARROW": "→",
    "UP_ARROW": "↑",
    "DOWN_ARROW": "↓",
}


KEY_LABELS = {
    getattr(Keycode, name): _REPLACEMENTS.get(name, name)
    for name in dir(Keycode)
    if not name.startswith("__") and isinstance(getattr(Keycode, name), int)
}
