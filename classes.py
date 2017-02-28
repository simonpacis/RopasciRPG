#classes start
class Player(object):
	name = ""
	gender = ""
	race = ""
	lives = ""
	tothp = ""
	curhp = ""
	level = ""
	exp = ""
	bp = ""
	weapons = {}
	items = {}
	apoth = ""
	smith = ""
	oot = ""
	merchant = ""
	location = ""

	def __init__(self, name, gender, race, lives = "3", tothp = "4", curhp = "4", level = "1", exp = "0", bp = "0", weapons = {"r": "rock", "p": "paper", "s": "scissors"}, items = {"hp": "1"}, apoth = "0", smith = "0", oot="0", merchant="0", location="town"):
		self.name = name
		self.gender = gender
		self.race = race
		self.lives = lives
		self.tothp = tothp
		self.curhp = curhp
		self.level = level
		self.exp = exp
		self.bp = bp
		self.weapons = weapons
		self.items = items
		self.apoth = apoth
		self.smith = smith
		self.oot = oot
		self.merchant = merchant
		self.location = location

class Enemy(object):
	name=""
	shortname=""
	taunts=[]
	pref = {}
	weapons = {}
	tothp=""
	curhp=""
	level=""
	loot=""
	maxloot=""

	def __init__(self, name, shortname, taunts=["Fight me!"], pref = {"r":1,"p":1,"s":1}, weapons = {"r": "rock", "p": "paper", "s": "scissors"}, tothp = "3", curhp = "3", level = "1", loot = {}, maxloot = 0):
		self.name = name
		self.shortname = shortname
		self.taunts = taunts
		self.pref = pref
		self.weapons = weapons
		self.tothp = tothp
		self.curhp = curhp
		self.level = level
		self.loot = loot
		self.maxloot = maxloot

	def reset(self):
		self.curhp = self.tothp

class Weapon(object):
	name = ""
	shortname = ""
	tier = "" #1, 2 or 3
	dmg = ""
	cost = ""
	type = "" #r, p or s
	lreq = "" #level requirement
	treq = "" #1, 2 or 3 - is the tiers of the weapons. Everyone starts with tier 1 weapons.

	def __init__(self, name, shortname, tier, dmg, cost, type, lreq, treq):
		self.name = name
		self.shortname = shortname
		self.tier = tier
		self.dmg = dmg
		self.cost = cost
		self.type = type
		self.lreq = lreq
		self.treq = treq

class Item(object):
	name = ""
	shortname = ""
	desc = ""
	failed = "" #message to print if item failed to be usedd
	cost = ""
	effect = "" #effect applied when used
	value = "" #amount of effect
	levelreq = ""

	def __init__(self, name, shortname, desc, failed, cost, effect, value="0", levelreq="1"):
		self.name = name
		self.shortname = shortname
		self.desc = desc
		self.failed = failed
		self.cost = cost
		self.effect = effect
		self.value = value
		self.levelreq = levelreq
#classes end