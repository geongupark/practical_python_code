import pyautogui

if __name__ == "__main__":
    # move to
    pyautogui.moveTo(1923, 540)  # move to (1923, 540)
    pyautogui.moveTo(200, 300, duration=1)  # move to (200, 300) during 1 sec

    # click
    pyautogui.click()  # click left, 1 time
    pyautogui.click(
        clicks=3, interval=1, button="right"
    )  # click right, 3 times, interval 1 sec

    # drag to
    pyautogui.dragTo(1923, 540)  # drag to (1923, 540)
    pyautogui.dragTo(200, 300, duration=1)  # drag to (200, 300) during 1 sec

    # get mouse info
    # "F2" button means copying the current point(x, y)
    pyautogui.mouseInfo()
