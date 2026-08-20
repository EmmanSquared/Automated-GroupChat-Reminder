import math
import os

from pynput.keyboard import Key,Controller
from dotenv import load_dotenv
from .time_checker import *
from time import sleep

load_dotenv()

msg_reminder = os.environ["MSG_REMINDER"]
link = os.environ["GROUP_LINK"]
kb = Controller()

def multi_line_type(text_to_type):
    text = [list(line) for line in text_to_type.strip().splitlines()]
    to_print = []
    sleep(3)
    node = 0
    for i in range(0,len(text),1):
        if node == i:
            for j in range(0,len(text[i]),1):
                if text[i][j] == 'n' and text[i][j+1] == ' ' and text[i][j-1] == ' ':
                    to_print.append(str(math.floor(meet_reminder.timeleft_till_next_reminder/3600)))
                elif text[i][j] == 'm' and text[i][j+1] == ' ' and text[i][j-1] == ' ':
                    to_print.append(str(round(60*((meet_reminder.timeleft_till_next_reminder/3600) - math.floor(meet_reminder.timeleft_till_next_reminder/3600)))))
                else:
                    to_print.append(text[i][j])
            print(to_print)
            for row in to_print:
                kb.type(row)
            to_print.clear()
            kb.press(Key.shift)
            sleep(.01)
            kb.press(Key.enter)
            sleep(.01)
            kb.release(Key.enter)
            kb.release(Key.shift)
            node += 1

def press_release_keyboard(x:str):
    kb.press(x)
    sleep(.3)
    kb.release(x)

def to_chat(x,y,z):
    kb.press(x)
    sleep(.5)
    kb.press(y)
    sleep(.5)
    kb.press(z)
    sleep(.5)
    kb.release(x)
    kb.release(y)
    kb.release(z)

def switch_website():
    press_release_keyboard(Key.f6)
    kb.type(link)
    press_release_keyboard(Key.enter)
    sleep(25)
    to_chat(Key.alt,Key.ctrl_l,'w')
    multi_line_type(msg_reminder)
    sleep(1)
    press_release_keyboard(Key.enter)
