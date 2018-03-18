from win32api import GetKeyState, mouse_event
from win32con import MOUSEEVENTF_WHEEL

def key_down(key):
    keystate = GetKeyState(key)
    if (keystate==0) or (keystate==1):
        return 0
    else:
        return 1

def scroll_wheel_forward(x,y):
    if mouse_event(MOUSEEVENTF_WHEEL,x,y) > 0:
        return 1
    else:
        return 0

def scroll_wheel_backward(x,y):
    if mouse_event(MOUSEEVENTF_WHEEL,x,y) < 0:
        return 1
    else:
        return 0
