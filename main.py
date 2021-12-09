# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import webbrowser
import pyautogui
import time
import os
import datetime
from datetime import date

def renamedownloadedfile(newfilename):
    renamedfile = "c:\\Users\\dg145254\\Downloads\\" + newfilename + "_" \
                  + datetime.date.today().strftime("%m%d%y") + ".xml"
    os.rename("c:\\Users\\dg145254\\Downloads\\UASR_MILESTN_PROG.xml", renamedfile)

def

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    # webbrowser.open("https://www.google.com")
    webbrowser.open("https://ps.itsli.albany.edu/psp/ps92prod/?cmd=login&languageCd=ENG&")
    time.sleep(5)
    pyautogui.write("dg145254")
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(6)

    pyautogui.click(143, 135)
    time.sleep(6)
    pyautogui.click(159, 483)
    time.sleep(6)
    pyautogui.click(335, 476)
    time.sleep(6)
    pyautogui.click(520, 469)
    time.sleep(6)
    pyautogui.click(335, 476)
    time.sleep(6)
    pyautogui.click(462, 273)
    pyautogui.write("UASR_MILESTN_PROG")
    time.sleep(6)
    pyautogui.click(79, 291)
    time.sleep(6)
    pyautogui.click(701, 483)
    time.sleep(6)
    pyautogui.write("BIODM")
    time.sleep(6)
    pyautogui.click(41, 153)
    time.sleep(6)
    renamedownloadedfile("UASR_MILESTN_PROG_BIODM")
    time.sleep(6)

    # Reload page
    pyautogui.click(97, 69)
    time.sleep(6)
    # Position in textbox and enter text
    pyautogui.write("BIOFB")
    time.sleep(6)
    # Click "SUBMIT"
    pyautogui.click(41, 153)
    time.sleep(6)
    renamedownloadedfile("UASR_MILESTN_PROG_BIOFB")
    time.sleep(6)

    # Reload page
    pyautogui.click(97, 69)
    time.sleep(6)
    # Position in textbox and enter text
    pyautogui.write("BIOMC")
    time.sleep(6)
    # Click "SUBMIT"
    pyautogui.click(41, 153)
    time.sleep(6)
    renamedownloadedfile("UASR_MILESTN_PROG_BIOMC")
    time.sleep(6)

    # Reload page
    pyautogui.click(97, 69)
    time.sleep(6)
    # Position in textbox and enter text
    pyautogui.write("BIOMS")
    time.sleep(6)
    # Click "SUBMIT"
    pyautogui.click(41, 153)
    time.sleep(6)
    renamedownloadedfile("UASR_MILESTN_PROG_BIOMS")
    time.sleep(6)

    # Reload page
    pyautogui.click(97, 69)
    time.sleep(6)
    # Position in textbox and enter text
    pyautogui.write("BIOND")
    time.sleep(6)
    # Click "SUBMIT"
    pyautogui.click(41, 153)
    time.sleep(6)
    renamedownloadedfile("UASR_MILESTN_PROG_BIOND")
    time.sleep(6)

    # Reload page
    pyautogui.click(97, 69)
    time.sleep(6)
    # Position in textbox and enter text
    pyautogui.write("BIOPH")
    time.sleep(6)
    # Click "SUBMIT"
    pyautogui.click(41, 153)
    time.sleep(6)
    renamedownloadedfile("UASR_MILESTN_PROG_BIOPH")
    time.sleep(6)

    while 1==1:
        time.sleep(2)
        print(pyautogui.position())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
