import pyautogui as pa 

#second delays for input
pa.PAUSE = 0.5

#saves in default folder
def bookmark(name):
	pa.hotkey('ctrl', 'd')
	if name is not None:
		pa.typewrite(name)
	pa.press('enter')

def closeTab():
	pa.hotkey('ctrl', 'w')

def closeWindow():
	pa.hotkey('alt', 'f4')
	pa.press('enter')

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
# def type():

#def search():

# #saves in Pictures or default directory
# def screenShot(name):
# 	img = pa.screenshot('test.png')


#leapmotionn

def back():
	pa.hotkey('alt', 'left')

def forward():
	pa.hotkey('alt', 'right')