import functionality as f

def command(data):

	# get type and search out of way

	# if (typer in data):
	# 	f.type(data minus "type ")
	if (("google" in data) or ("search" in data) or ("Google" in data)):
		f.search(data[6:])

	elif (("click" in data) or ("clack" in data)):
		f.click()

	elif (("messenger" in data)):
		f.open_messenger()

	elif (("bookmark" in data) or ("mark" in data) or ("Mike" in data) or ("but like" in data) or ("look like" in data)):
		f.bookmark(None)

	elif ("close" in data):
		if (("tab" in data) or ("to" in data)):
			f.closeTab()
		elif (("window" in data) or ("enough" in data)):
			f.closeWindow()
		else:
			f.closeTab()

	elif ("kneeling" in data): #kneeling sounds like new win - dow is down.
		f.newWindow()

	elif (("new" in data) or ("you" in data) or ('ea' in data)):
		if (("tab" in data) or ("tap" in data) or ("tax" in data) or ("tag" in data) or ("have" in data) or ('ad' in data)):
			f.newTab()
		elif (("window" in data) or ('ow' in data)):
			f.newWindow()

	elif ("next" in data):
		if (("tab" in data) or ("tap" in data) or ("tax" in data) or ("tag" in data) or ("have" in data) or ('ad' in data)):
			f.nextTab()
		else:
			f.tab() #saying "next field to fall here"

	elif ("previous" in data):
		if (("tab" in data) or ("tap" in data) or ("tax" in data) or ("tag" in data) or ("have" in data) or ('at' in data)):
			f.prevTab()
		elif (("window" in data) or ("no" in data)):
			f.prevWindow()

	elif (("window" in data) or ("when" in data) or ("know" in data) or ("no" in data) or ("ough" in data)):
		if (('se ' in data)):
			f.closeWindow()
		elif (('s ' in data)):
			f.prevWindow()
		elif (('ew' in data) or ('Ew' in data) or ('ea' in data)):
			f.newWindow()

	elif (("tab" in data) or ("tap" in data) or ("tax" in data) or ("tag" in data) or ("have" in data) or ("tad" in data)):
		#something about tab
		if (('se ' in data) or ('s ' in data)):
			f.closeTab()
		elif (('you' in data) or ('ea' in data)):
			f.newTab()

	elif (("enter" in data)):
		f.enter()

	elif ("go" in data):
		if ("back" in data):
			f.back()
		elif ("forward" in data):
			f.forward()

	elif (("refresh" in data) or ('ress' in data) or ('reph' in data) or ('fresh' in data) or ('ref' in data)):
		f.refresh()

	elif (("fullscreen" in data) or (("first" in data) and ('ame' in data)) ):
		f.fullscreen()
