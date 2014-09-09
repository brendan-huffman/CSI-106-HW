
1.)

def showTwoPictures()

	setMediaPath()
	file=pickAFile()
	picture=makePicture(file)
	show(picture)
	setMediaPath()
	file=pickAFile()
	picture=makePicture(file)
	show(picture)

2.)

def printInvite()
  
	txt1=Please help me celebrate!  Party takes place this next Saturday at 2.  Bring some food or drink to share.  RSVP ASAP
  	print txt1


3.)

def printDisclaimer()

	txt2=I am not liable for any harm inflicted upon you at said party.  You assume some measure of risk entering my house.  I cannot promise that you or any guest you choose to bring will leave my house unharmed.
	print txt2

4.)

def printFullInvite()

	txt=Please help me celebrate!  Party takes place this next Saturday at 2.  Bring some food or drink to share.  RSVP ASAP
  	
	txt2=I am not liable for any harm inflicted upon you at said party.  You assume some measure of risk entering my house.  I cannot promise that you or any guest you choose to bring will leave my house unharmed.
	
	print txt1+txt2