def createitems():
	#Adding more items? Remember to declare the global as well, and create it as an empty variable in the declarations block in declarations.py

	global hp, majhp, mindetector, majdetector, fleer, majfleer

	hp = Item("Health Potion", "hp", "heals 1 HP", "You do not need a Health Potion right now.", "10", "heal", "1", "1")
	majhp = Item("Major Health Potion", "majhp", "heals 2 HP", "You do not need a Major Health Potion right now.", "15", "heal", "2", "2")

	mindetector = Item("Minor Revelation Potion", "mindetector", "tries to detect enemy weapon preferences", "You did not manage to detect your enemy's weapon preferences.", "5", "detect", "0", "1")
	majdetector = Item("Major Revelation Potion", "majdetector", "detects enemy weapon preferences", "You did not manage to detect your enemy's weapon preferences.", "7", "detect", "1", "2")

	fleer = Item("Smoke Bomb", "fleer", "tries to flee from your enemy", "You did not manage to flee from your enemy.", "15", "flee", "0.70", "1")

	majfleer = Item("Vanish Poison", "majfleer", "flee from your enemy and lose 4 HP towards next fight", "You did not manage to flee from your enemy.", "3", "flee", "1.1", "3")