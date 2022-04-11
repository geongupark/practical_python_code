import pyautogui

if __name__ == "__main__":
    current_mouse_position = pyautogui.position()
    current_screen_size = pyautogui.size()
    is_in_the_screen = pyautogui.onScreen(-20, 100)

    print(
        f"current mouse position : {current_mouse_position}\n",  # class 'pyautogui.Point'
        f"x : {current_mouse_position.x}\n",  # int
        f"y: {current_mouse_position.y}",  # int
    )
    print(
        f"current screen size : {current_screen_size}\n",  # class 'pyautogui.Size'
        f"width : {current_screen_size.width}\n",  # int
        f"height : {current_screen_size.height}",  # int
    )
    print(f"is in the screen : {is_in_the_screen}")  # bool

# * Output
# current mouse position : Point(x=1029, y=341)
#  x : 1029
#  y: 341
# current screen size : Size(width=1920, height=1080)
#  width : 1920
#  height : 1080
# is in the screen : False
