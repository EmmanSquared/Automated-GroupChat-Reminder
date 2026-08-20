import subprocess
import pynput
import sys

from .chat_reminder import switch_website
from ewmhlib import EwmhRoot, EwmhWindow
from screeninfo import get_monitors
from pynput import mouse,keyboard
from rich import print
from time import sleep

x,y = (get_monitors()[0].width/16,2*get_monitors()[0].height/3)
kb = keyboard.Controller()
ms = mouse.Controller()

def mouse_press_release(x):
    ms.press(x)
    sleep(.3)
    ms.release(x)

def launch_browser():
    try:
        subprocess.run(["flatpak","run","io.github.ungoogled_software.ungoogled_chromium"])
        ms.position = (x,y)
        sleep(1.5)
        mouse_press_release(mouse.Button.left)
    except:
        subprocess.run(["flatpak-spawn", "--host","flatpak", "run", "io.github.ungoogled_software.ungoogled_chromium"])
        ms.position = (x,y)
        sleep(1.5)
        mouse_press_release(mouse.Button.left)

def close_browser():
    kb.press(keyboard.Key.alt)
    sleep(.05)
    kb.press(keyboard.Key.f4)
    sleep(.05)
    kb.release(keyboard.Key.f4)
    kb.release(keyboard.Key.alt)

def window_tasks():
    launch_browser()
    sleep(.5)
    switch_website()
    sleep(.5)
    close_browser()

# Below are for further development

# root = EwmhRoot()
# all_windows = root.getClientList()
# print('[bold green]EWMH ID; [/bold green]',"[bold green]EWMH Name; [/bold green]", "[bold green]PID[/bold green]" )
# for i in all_windows:
#     window = EwmhWindow(i)
#     print(i, ' ', window.getName(), ' ', window.getPid())
#     if window.getName() == 'New Tab - Chromium':
#         print('[bold green]You found chromium[/bold green]')
#         window.setActive()
#         switch_website()
#         break
#     # else:
#     #     sys.exit()
# sleep(1)
            