from turtle import title
import pyautogui,keyboard
def lu():
    return pyautogui.password(mask = '*',text = "Password",title = "Lock-Unlock")
lock = False
savepos = tuple(pyautogui.position())
while True:
    if keyboard.is_pressed('ctrl+alt+`'):
        if not lock:
            if lu() == "13921399":
                lock = True
                savepos = tuple(pyautogui.position())
        else:
            if lu() == "13921399":
                lock = False
    elif keyboard.is_pressed('ctrl+alt+m'):
        pyautogui.alert(text = 'Lock Mode:'+str(lock),title = "Mode",button = "Done")
    if lock:
        pyautogui.moveTo(savepos)