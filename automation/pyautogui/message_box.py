import pyautogui

if __name__ == "__main__":
    response_alert = pyautogui.alert(text="alert body", title="alert", button="OK")
    response_confirm = pyautogui.confirm(
        text="confirm body", title="confirm", buttons=["OK", "Cancle"]
    )
    response_prompt = pyautogui.prompt(
        text="prompt body", title="prompt", default="default value"
    )
    response_passwd = pyautogui.password(
        text="password body", title="password", mask="*"
    )

    print(f"response of alert = {response_alert}, {type(response_alert)}")
    print(f"response of confirm = {response_confirm}, {type(response_confirm)}")
    print(f"response of prompt = {response_prompt}, {type(response_prompt)}")
    print(f"response of password = {response_passwd}, {type(response_passwd)}")

# * Output
# response of alert = OK, <class 'str'>
# response of confirm = Cancle, <class 'str'>
# response of prompt = default value, <class 'str'>
# response of password = 1234, <class 'str'>
