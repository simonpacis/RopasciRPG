def createweapons():
	#argument order: name, shortname, tier, dmg, cost, type, lreq, treq
	global rock, paper, scissors, boulder, tinfoil, knife, anvil, duct, sword
	#tier 1
	rock = Weapon("Rock", "rock", "1", "1", "0", "r", "1", "0")
	paper = Weapon("Paper", "paper", "1", "1", "0", "p", "1", "0")
	scissors = Weapon("Scissors", "scissors", "1", "1", "0", "s", "1", "0")

	#tier 2
	boulder = Weapon("Boulder", "boulder", "2", "2", "15", "r", "2", "1")
	tinfoil = Weapon("Tinfoil", "tinfoil", "2", "2", "15", "p", "2", "1")
	knife = Weapon("Knife", "knife", "2", "2", "15", "s", "2", "1")

	#tier 3
	anvil = Weapon("Anvil", "anvil", "3", "3", "25", "r", "3", "2")
	duct = Weapon("Duct Tape", "duct", "3", "3", "25", "p", "3", "2")
	sword = Weapon("Sword", "sword", "3", "3", "25", "s", "3", "2")