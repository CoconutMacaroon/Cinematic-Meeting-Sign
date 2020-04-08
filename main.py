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
    # does window title contain "Microsoft Teams" or match "Zoom Meeting ID: xxx-xxx-xxx"*
    # *This was un-regex-ified for simplicity, but it acctually uses regex
    if(
        "Microsoft Teams" in window_title
        or match(r"(Zoom Meeting ID: )\d{3}-\d{3}-\d{3}", window_title)):
        ser.write(b"1")
    else:
        ser.write(b"0")
