import pyautogui as pa 

#second delays for input
pa.PAUSE = 0.5

def prevWindow():
	pa.hotkey('alt', 'tab')

def newWindow():
	pa.hotkey('ctrl', 'n')

#saves in default folder
def bookmark(name):
	pa.hotkey('ctrl', 'd')
	if name is not None:
		pa.typewrite(name)
	pa.press('enter')

def back():
	pa.hotkey('alt', 'left')

def forward():
	pa.hotkey('alt', 'right')

def closeTab():
	pa.hotkey('ctrl', 'w')

def newTab():
	pa.hotkey('ctrl', 't')

def tab():
	pa.press('tab')

def enter():
	pa.press('enter')

def closeWindow():
	pa.hotkey('alt', 'f4')

def nextTab():
	pa.hotkey('ctrl', 'tab')

def prevTab():
	pa.hotkey('ctrl', 'shift', 'tab')