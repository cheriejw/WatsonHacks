import pyautogui as pa 
from google_search import launch_google
import webbrowser
import re
from datetime import datetime
from time import gmtime, strftime
from voice import speak

#second delays for input
pa.PAUSE = 0.25

#saves in default folder
def bookmark(name):
	pa.hotkey('ctrl', 'd')
	if name is not None:
		pa.typewrite(name)
	pa.press('enter')

def time():
	minute = datetime.now().strftime('%M')
	hour = datetime.now().strftime('%H')
	speak("The current time is " + hour + minute)

def date():
	speak("Today's date is " + strftime(",%A, %d" + " of " + "%B %Y"))

def inspect():
	pa.press('f12')

def open_messenger():
    webbrowser.open_new("https://www.messenger.com/")

def closeTab():
	pa.hotkey('ctrl', 'w')

def closeWindow():
	pa.hotkey('alt', 'f4')
	# pa.press('enter')

def newWindow():
	pa.hotkey('ctrl', 'n')

def newTab():
	pa.hotkey('ctrl', 't')

def nextTab():
	pa.hotkey('ctrl', 'tab')

def prevTab():
	pa.hotkey('ctrl', 'shift', 'tab')

def prevWindow():
	pa.hotkey('alt', 'tab')

def click():
	pa.click()

def tab():
	pa.press('tab')

def enter():
	pa.press('enter')

def zoomin():
	pa.hotkey('ctrl', '=')

def zoomout():
	pa.hotkey('ctrl', '-')

def resetZoom():
	pa.hotkey('ctrl', '0')

def refresh():
	pa.press('f5')

def fullscreen():
	pa.press('f11')

#WIP
def type(words):
	pa.typewrite(words, interval=0.1)

def search(query):
	launch_google(query)

# #saves in Pictures or default directory
# def screenShot(name):
# 	img = pa.screenshot('test.png')


#leapmotionn

def back():
	pa.hotkey('alt', 'left')

def forward():
	pa.hotkey('alt', 'right')