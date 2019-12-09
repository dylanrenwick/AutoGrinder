import win32api, win32con
from enum import Enum

class InputCommand:
    def __init__(self, command_type, location, parameters=""):
        self.command_type = command_type
        self.location = location
        self.parameters = parameters

    def execute(self):
        if self.command_type == CommandType.KEYBOARD:
            self.execute_keyboard()
        else:
            self.execute_mouse()

    def execute_keyboard(self):
        if self.command_type != CommandType.KEYBOARD: return
        if isinstance(self.parameters[0], str):
            for c in self.parameters[0]:
                win32api.keybd_event(ord(c), 0)
                win32api.keybd_event(ord(c), 0, 2)
        else:
            win32api.keybd_event(self.parameters[0], 0)
            win32api.keybd_event(self.parameters[0], 0, 2)

    def execute_mouse(self):
        win32api.SetCursorPos(self.location)
        mouse_button_down = win32con.MOUSEEVENTF_LEFTDOWN
        mouse_button_up = win32con.MOUSEEVENTF_LEFTUP
        if self.command_type == CommandType.MOUSE_RIGHT:
            mouse_button_down = win32con.MOUSEEVENTF_RIGHTDOWN
            mouse_button_up = win32con.MOUSEEVENTF_RIGHTUP
        win32api.mouse_event(mouse_button_down, self.location[0], self.location[1], 0, 0)
        win32api.mouse_event(mouse_button_up, self.location[0], self.location[1], 0, 0)

class CommandType(Enum):
    KEYBOARD = 1,
    MOUSE_LEFT = 2,
    MOUSE_RIGHT = 3,
    MOUSE_SCROLL = 4