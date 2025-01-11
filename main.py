import PySimpleGUI as sg
from gui import *
from mss import mss
from win32gui import FindWindow, GetWindowRect
import mss.tools
from datetime import datetime

def main():

    window = sg.Window("Lafay", layout, keep_on_top=True, no_titlebar=True, grab_anywhere=True)

    timer = 0
    while True:
        event, values = window.read(timeout=1000 if timer else None)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == "Save":
            coords = get_coords()
            screenshot(*coords)
            sg.popup("Saved", auto_close=True, auto_close_duration=1, keep_on_top=True)
            break
        if timer > 0:
            timer -= 1
        if event == "25 sec":
            timer = 25
        elif event == "3 min":
            timer = 180
        window["clock"].update(timer)

    window.close()



def get_coords():
    window_handle = FindWindow(None, "Lafay")
    window_rect   = GetWindowRect(window_handle)
    x = window_rect[0]
    y = window_rect[1]
    w = window_rect[2] - x
    h = window_rect[3] - y

    return [x, y, w, h]

def screenshot(x, y, w, h):
    with mss.mss() as sct:
        date = datetime.now().strftime("%d-%m-%Y")
        # The screen part to capture
        monitor = {"top": y, "left": x, "width": w, "height": h}
        output = f"carnet/{date}.png".format(**monitor)

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)

if __name__ == "__main__":
    main()
    