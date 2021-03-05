import pyautogui
import time


def isShiftCharacter(character):
    return character.isupper() or character in set('~1234567890°+>?./§%µ')


def download_file(pathname):
    screenWidth, screenHeight = pyautogui.size()  # Get the size of the primary monitor.

    # currentMouseX, currentMouseY = pyautogui.position()  # Get the XY position of the mouse.

    print("Largeur : {}  Hauteur : {}".format(screenWidth, screenHeight))

    # pyautogui.moveTo(960, 540) # Move the mouse to XY coordinates.

    pyautogui.isShiftCharacter = isShiftCharacter

    dl_button = None
    ok_button = None
    download_window = None

    while dl_button is None:
        dl_button = pyautogui.locateOnScreen('dl_button.png')

    pyautogui.click('dl_button.png')

    while ok_button is None:
        ok_button = pyautogui.locateOnScreen('ok.png')

    while download_window is None:
        download_window = pyautogui.locateOnScreen('download.png')

    pyautogui.click('download.png')
    # pyautogui.moveTo('ok.png')

    pyautogui.press('f4')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.write(pathname, interval=0.1)
    pyautogui.press('enter')
    time.sleep(10)

i = 0


while True:
    time.sleep(600)
    #i+= 1

    pyautogui.drag(200, 0, duration=0.5)
    time.sleep(600)
    pyautogui.drag(-200, 0, duration=0.5)
    time.sleep(600)
    pyautogui.drag(200, 0, duration=0.5)

# print(pyautogui.moveTo('skype.png'))
