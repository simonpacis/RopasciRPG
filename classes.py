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
	l1mobs = []
	l2mobs = []
	l3mobs = []

	def __init__(self, name, gender, race, lives = "3", tothp = "4", curhp = "4", level = "1", exp = "0", bp = "0", weapons = {"r": "rock", "p": "paper", "s": "scissors"}, items = {"hp": "1"}, apoth = "0", smith = "0", oot="0", l1mobs = [], l2mobs = [], l3mobs = []):
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
		self.l1mobs = l1mobs
		self.l2mobs = l2mobs
		self.l3mobs = l3mobs

class Enemy(object):
	name=""
	shortname=""
	taunts=[]
	pref = {}
	weapons = {}
	tothp=""
	curhp=""
	level=""

	def __init__(self, name, shortname, taunts=["Fight me!"], pref = {"r":1,"p":1,"s":1}, weapons = {"r": "rock", "p": "paper", "s": "scissors"}, tothp = "3", curhp = "3", level = "1"):
		self.name = name
		self.shortname = shortname
		self.taunts = taunts
		self.pref = pref
		self.weapons = weapons
		self.tothp = tothp
		self.curhp = curhp
		self.level = level


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
	failed = ""
	cost = ""
	effect = "" #heal
	value = "" #amount of heal
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