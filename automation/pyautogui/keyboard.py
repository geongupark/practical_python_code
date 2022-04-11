import pyautogui
import pyperclip

if __name__ == "__main__":
    # write keyboard at the current cursor (only English, not Korean)
    pyautogui.write("# only Englilsh", interval=0.25)

    # key
    pyautogui.press("enter")
    pyautogui.press("up")

    # multiple key
    pyautogui.hotkey("ctrl", "c")

    # write Korean (with pyperclip.copy)
    pyperclip.copy("한글은 이렇게...")
    pyautogui.hotkey("ctrl", "v")
