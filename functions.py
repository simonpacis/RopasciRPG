#functions start
def buy(item):
	global player
	#c = str_to_class(item) #no eval, yo
	c = items[item]
	if int(player.bp) >= int(c.cost) and int(player.bp) > 0:
		if c.shortname in player.items: #if item exists in inventory
			player.items[c.shortname] = str(int(player.items[c.shortname]) + 1) #add to the quantity
		else: #if it does not exist in inventory
			player.items[c.shortname] = '1' #create it
		player.bp = str(int(player.bp) - int(c.cost)) #convert to int, subtract, convert to string and add to player class
		return "1"
	else:
		return "0"

def sell(item):
	global player
	c = items[item]
	if item in player.items:
		if int(player.items[item]) != 1:
			player.items[item] = str(int(player.items[item]) - 1)
		else:
			del player.items[item]
		player.bp = player.bp = str(int(player.bp) + int(float(c.cost)/2))
		return "1"
	else:
		return "0"

def upgrade(type):
	global player
	a = int(str_to_class(player.weapons[type]).tier) #current tier in selected weapon type/category
	if a == 3: #maxed out
		return "2"
	b = str_to_class(str_to_class(type + "tiers")[a]) #weapon in next tier, in selected type/category
	if player.level >= b.lreq and a == int(b.treq) and int(player.bp) >= int(b.cost) and int(player.bp) > 0: #if all reqs are met (player level, current tier in selected category is)
		player.bp = str(int(player.bp) - int(b.cost))
		player.weapons[type] = b.shortname
		return "1"
	else:
		return "0"

def use(item):
	global player
	def mainuse():
		if int(player.items[item]) == 1: #if it is the last of item - delete it from dictionary
			application = applyeffect(item)
			if application != 0:
				del player.items[item]
				return(application)
			else:
				return(0)
		else: #if not the last, remove one from quantity
			application = applyeffect(item)
			if application != 0:
				player.items[item] = str(int(player.items[item]) - 1)
				return(application)
			else:
				return(0)
	return mainuse()

def location(loc):
	global player
	print(bold("Location: ") + locations[loc] + "\n")
	player.location = loc

def createplayer(name, gender, race):
	global player
	player = Player(name, gender, race)

def create(name, gender, race):
	createplayer(name, gender, race)
	createnoplayer()

def createnoplayer():
	#createitems()
	createweapons()

def lreq():
	return levelreqs[str(int(player.level) + 1)]

def clear():
	# Clear Windows command prompt.
	if (os.name in ('ce', 'nt', 'dos')):
		os.system('cls')

	# Clear the Linux terminal.
	elif ('posix' in os.name):
		os.system('clear')

def bold(strng):
	return("\033[1m" + strng + "\033[0m")

def yellow(strng):
	return("\033[33m" + strng + "\033[0m")

def blue(strng):
	return("\033[94m" + strng + "\033[0m")

def red(strng):
	return("\033[91m" + strng + "\033[0m")

def underline(strng):
	return("\033[4m" + strng + "\033[0m")

def str_to_class(str): # no need to use eval. Eval is bad for you.
	return getattr(sys.modules[__name__], str)

def handleinterrupt():
	try:
		if player != 0 and player.location == "town":
			clear()
			print("Would you like to save before exiting? (y/n/cancel)")
			selec = input("> ")
			if selec == "y":
				save(1)
			elif selec == "cancel":
				mg()
			else:
				gameexit()
		elif player != 0 and player.location != "town":
			clear()
			print("If you would like to save before exiting, you have to return to town. Would you like to return to what you were previously doing? (y/n)")
			selec = input("> ")
			if selec == "y":
				if player.location == "apoth" or player.location == "smith" or player.location == "merchant":
					exec(player.location + "()")
				elif player.location == "oot":
					fight()
			else:
				gameexit()
		else:
			gameexit()
	except KeyboardInterrupt:
		handleinterrupt()
#functions end