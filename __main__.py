import win32api, pythoncom, pyHook
from InputCommand import InputCommand, CommandType
from Rect import Rect

start_pos = (-1448, 413)
end_pos = (-473, 1052)
calibrate = False
if calibrate:
    done = False

    def on_mouse_down(event):
        global start_pos
        start_pos = event.Position
        return True
    def on_mouse_up(event):
        global end_pos
        global done
        end_pos = event.Position
        done = True
        return True

    hm = pyHook.HookManager()
    hm.SubscribeMouseLeftDown(on_mouse_down)
    hm.SubscribeMouseLeftUp(on_mouse_up)
    hm.HookMouse()
    while not done:
        pythoncom.PumpWaitingMessages()
    hm.UnhookMouse()

    print(start_pos)
    print(end_pos)

game_rect = Rect(start_pos, end_pos)

def global_to_game(coords):
    global game_rect
    return (coords[0] - start_pos[0], coords[1] - start_pos[1])

reset_sequence = list(map(global_to_game, [(-499, 1021), (-1198, 983), (-1033, 778), (-1012, 749), (-1036, 810)]))

while False:
    done = False
    hm.HookMouse()
    while not done:
        pythoncom.PumpWaitingMessages()
    hm.UnhookMouse()

    print(end_pos)

print(reset_sequence)
for com in reset_sequence:
    command = InputCommand(CommandType.MOUSE_LEFT, com)

