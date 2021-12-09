# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import webbrowser
import pyautogui
import time
import os
import datetime
from datetime import date

def renamedownloadedfile_milestone(newfilename):
    renamedfile = "c:\\Users\\dg145254\\Downloads\\" + newfilename + "_" \
                  + datetime.date.today().strftime("%m%d%y") + ".xml"
    os.rename("c:\\Users\\dg145254\\Downloads\\UASR_MILESTN_PROG.xml", renamedfile)


def renamedownloadedfile_coursebyacadorg(newfilename):
    renamedfile = "c:\\Users\\dg145254\\Downloads\\" + newfilename + "_" \
                  + datetime.date.today().strftime("%m%d%y") + ".xml"
    os.rename("c:\\Users\\dg145254\\Downloads\\UADW_CRSE_BY_ACAD_ORG.xml", renamedfile)

def downloadmilestonereports():

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
    renamedownloadedfile_milestone("UASR_MILESTN_PROG_BIODM")
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
    renamedownloadedfile_milestone("UASR_MILESTN_PROG_BIOFB")
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
    renamedownloadedfile_milestone("UASR_MILESTN_PROG_BIOMC")
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
    renamedownloadedfile_milestone("UASR_MILESTN_PROG_BIOMS")
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
    renamedownloadedfile_milestone("UASR_MILESTN_PROG_BIOND")
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
    renamedownloadedfile_milestone("UASR_MILESTN_PROG_BIOPH")
    time.sleep(6)


def downloadcoursebyacadorgreports():

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
    pyautogui.write("UADW_CRSE_BY_ACAD_ORG")
    time.sleep(6)
    pyautogui.click(79, 291)
    time.sleep(6)

    # terms = ['2101', '2103', '2106', '2109', '2111', '2113', '2116', '2119', '2121', '2123', '2126', '2129', '2131',
    #          '2133', '2136', '2139', '2141', '2143', '2146', '2149', '2151', '2153', '2156', '2159', '2161', '2163',
    #          '2166', '2169', '2171', '2173', '2176', '2179', '2181', '2183', '2186', '2189', '2191', '2193', '2196',
    #          '2199', '2201', '2203', '2206', '2209', '2211', '2213', '2216', '2219']
    terms = ['2213', '2216', '2219']
    plan10s = ['BIO-MS', 'BIO-MSBCP', 'BIO-MSCMB', 'BIO-MSCT', 'BIO-MSFBM', 'BIO-MSFMB', 'BIO-MSFOR',
               'BIO-NON', 'BIO-PHD']


    for term in terms:

        for plan10 in plan10s:

            GetAcadOrgReport(term, "BIOSCI", plan10)
            renamedownloadedfile_coursebyacadorg("UADW_CRSE_BY_ACAD_ORG_" + plan10 + "_" + term)

        # GetAcadOrgReport("2219", "BIOSCI", "BIO-MSBCP")
        # renamedownloadedfile_coursebyacadorg("UADW_CRSE_BY_ACAD_ORG_BIO-MSBCP")
        #
        # GetAcadOrgReport("2219", "BIOSCI", "BIO-MSFBM")
        # renamedownloadedfile_coursebyacadorg("UADW_CRSE_BY_ACAD_ORG_BIO-MSFBM")


def GetAcadOrgReport(term, acadorg, plan10):

    # Longish wait
    time.sleep(6)
    # Click on "XML" output link
    pyautogui.click(706, 487)
    time.sleep(6)
    # Select "Career"
    pyautogui.click(282, 132)
    time.sleep(6)
    pyautogui.click(137, 182)
    time.sleep(6)
    # Select "Term"
    pyautogui.click(92, 157)
    time.sleep(6)
    pyautogui.write(term)
    time.sleep(6)
    pyautogui.click(90, 184)
    time.sleep(6)
    pyautogui.write(acadorg)
    time.sleep(6)
    pyautogui.click(101, 203)
    time.sleep(6)
    pyautogui.write(plan10)
    time.sleep(6)

    # Click "View Results"
    pyautogui.click(51, 226)
    time.sleep(6)

    # Close tab
    pyautogui.click(429, 21)
    time.sleep(6)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    # downloadmilestonereports()
    downloadcoursebyacadorgreports()

    while 1==1:
        time.sleep(2)
        print(pyautogui.position())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
