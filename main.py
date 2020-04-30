from win32gui import GetWindowText, GetForegroundWindow
from time import sleep
import serial
from easygui import msgbox
from re import match
from sys import argv, exit
try:
    ser = serial.Serial(argv[1], 9600)
except IndexError:
    msgbox("Include the desired COM port as the first argument", title="COM ERROR")
    exit(7)
while True:
    window_title = str(GetWindowText(GetForegroundWindow()))

    if("Microsoft Teams" in window_title) or ("Zoom" in window_title) or ("Skype" in window_title) or ("Google Hangouts" in window_title):
        ser.write(b"1")
    else:
        ser.write(b"0")
