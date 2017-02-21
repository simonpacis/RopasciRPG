#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

#import start
import sys
import os
import random
import pathlib
import pickle
#import end

#main gameloop start
def main():
	initiate()
#main gameloop end

#gameloops start
def initiate(rerun=0):
	clear()
	print("Welcome to RopasciRPG.")

	if rerun == 0:
		print("\n")
	elif rerun == 1:
		print("\nOption does not exist. Please try again.")

	print("Please select an option.\n1) New game\n2) Load game\n3) Instructions\n4) About\n5) Exit game")
	menuselection = input("> ")
	if menuselection == "1":
		ng1()
	elif menuselection == "2":
		load()
	elif menuselection == "3":
		instructions()
	elif menuselection == "4":
		about()
	elif menuselection == "5":
		gameexit()
	else:
		initiate(1)

#maingame gameloops start
def mg():
	clear()
	location("town")
	print(player.name + "\tHP: " + player.curhp + "/" + player.tothp + "\t\tLives: " + player.lives + "\nLvl: " + player.level + "\tExp: " + player.exp + "/" + lreq() + "\tGold: " + player.bp + "\n" + player.race + "\t" + player.gender + "\n") #print player information
	if player.items: #if inventory is not empty
		print("Inventory:", end=" ")
		for item in player.items: #iterate over items in inventory
			c = str_to_class(item) #string to class without using eval
			print(c.name + ": " + player.items[item] + "\t", end=" ") #print item and tab it at the end + no newline
	else:
		print("Inventory: (empty)", end=" ")

	print("\n\nCurrent weapons:\nRock: " + str_to_class(player.weapons["r"]).name + " (" + str_to_class(player.weapons["r"]).tier + ")\nPaper: " + str_to_class(player.weapons["p"]).name + " (" + str_to_class(player.weapons["p"]).tier + ")\nScissors: " + str_to_class(player.weapons["s"]).name + " (" + str_to_class(player.weapons["s"]).tier + ")\n")

	print("Please select an option\n1) Look for trouble\n2) Go to \"Ole Apothecary\"\n3) Go to \"Ye Smithe o'er All\"\n4) Save game\n5) Exit to main menu")#options
	selection = input("> ")

	if selection == "1":
		initfight()
	elif selection == "2":
		apoth()
	elif selection == "3":
		smith()
	elif selection == "4":
		save()
	elif selection == "5":
		clear()
		print("Are you sure? All unsaved changes will be lost.\n1) Yes\n2) No")
		sure = input("> ")
		if sure == "1":
			initiate()
		else:
			mg()
	else:
		mg()
#maingame gameloops end

#fighting gameloops start
def initfight():
	global player, enemy, playerselect, thug, bandit, eblob, chorse, wolf, magician, madp, lordling, bleader, mmagician, cblob, mlumberjack, osailor, gnometroll, eknight, slayerman, deserter, lord, wyvern, lynx, kblob, gmad, cminelo, hbandit, cunicorn, kgnometroll, enlord, mcriminal, ebear, king
	clear()
	if player.oot == "0":
		location("oot")
		print("As you leave behind the town, and enter out into the wild nature and fresh air, you begin to slowly grow more and more worried. You think you hear sounds around every single corner. You're slowly, slowly walking. Wh-what was that s-sound?\n\n" + player.name + ": \"Hello? Anyone there?\"")
		input("> ")
		clear()
		player.oot = "1"
	#create and select the opponent
	createenemies() #create enemies
	newenemy = 0
	while (newenemy == 0): #make sure that a new enemy is selected
		enemy = str_to_class(random.choice((str_to_class("l" + player.level + "mobs")))) #random enemy from current player level
		if enemy in getattr(player, 'l%dmobs' % int(player.level)):
			newenemy = 0
		else:
			newenemy = 1
			l = getattr(player, 'l%dmobs' % int(player.level))
			l.append(enemy.shortname)
			l is getattr(player, 'l%dmobs' % int(player.level))
	location("oot")
	if enemy.name.lower()[0] in "aeiou":
		print('An', end=" ")
	else:   
		print('A', end=" ")
	print(enemy.name + " appeared!")
	print(enemy.name + ": \"" + random.choice(enemy.taunts) + "\"\n")
	print("1) Fight\n2) Run")
	fiorun = input("> ")
	if fiorun == "1":
		fight()
	elif fiorun == "2":
		escape = random.random()
		if escape > 0.60:
			print("Got away safely. (Press enter to continue)")
			input("> ")
			mg()
		else:
			print("Can't escape! (Press enter to continue)")
			input("> ")
			fight()
	else:
		fight()

def fight():
	global playerselect
	clear()
	def battlescreen():
		print(player.name + "\tHP: " + player.curhp + "/" + player.tothp + "\t\tLives: " + player.lives + "\nLvl: " + player.level + "\tExp: " + player.exp + "/" + lreq() + "\n") #print player information
		if player.items: #if inventory is not empty
			print("Inventory:", end=" ")
			for item in player.items: #iterate over items in inventory
				c = str_to_class(item) #string to class without using eval
				print(c.name + ": " + player.items[item] + "\t", end=" ") #print item and tab it at the end + no newline
		else:
			print("Inventory: (empty)", end=" ")

		print("\n\nCurrent weapons:\nRock: " + str_to_class(player.weapons["r"]).name + " (" + str_to_class(player.weapons["r"]).tier + ")\nPaper: " + str_to_class(player.weapons["p"]).name + " (" + str_to_class(player.weapons["p"]).tier + ")\nScissors: " + str_to_class(player.weapons["s"]).name + " (" + str_to_class(player.weapons["s"]).tier + ")\n")

		print("\n" + enemy.name + "\tHP: " + enemy.curhp + "/" + enemy.tothp + "\n")
	def mainbattle():
		global playerselect
		if int(player.curhp) <= 0:
			playerdie()
		elif int(enemy.curhp) <= 0:
			enemydie()

		battlescreen()

		print("\n1) (or r) " + str_to_class(player.weapons["r"]).name + "\n2) (or p) " + str_to_class(player.weapons["p"]).name + "\n3) (or s) " + str_to_class(player.weapons["s"]).name + "\n4) Use item")
		fsel = input("> ")
		if fsel == "1" or fsel == "r":
			playerselect = "r"
			turn()
		elif fsel == "2" or fsel == "p":
			playerselect = "p"
			turn()
		elif fsel == "3" or fsel == "s":
			playerselect = "s"
			turn()
		else:
			fightinventory()

	def turn():
		global playerweapon, enemyweapon
		clear()
		battlescreen()
		enemyselectseed = random.random()
		prefr = enemy.pref["r"] * 0.33
		prefp = enemy.pref["p"] * 0.33 + prefr
		if enemyselectseed > 0 and enemyselectseed <= prefr:
			enemyselect = "r"
		elif enemyselectseed > prefr and enemyselectseed <= prefp:
			enemyselect = "p"
		else:
			enemyselect = "s"

		enemyweapon = str_to_class(enemy.weapons[enemyselect])
		playerweapon = str_to_class(player.weapons[playerselect])
		if playerselect == enemyselect:
			turntied()
		else:
			if playerselect == "r": #player selects rocktype
				if enemyselect == "p": #enemy selects papertype
					turnplose()
				else: #player selects rocktype - enemy does not select papertype
					turnpwin()
			elif playerselect == "p": #if player selects papertype
				if enemyselect == "s": #if enemy selects scissortype - player loses round
					turnplose()
				else: #if enemy does not select scissortype
					turnpwin()
			else: #player selects s
				if enemyselect == "r": #player selects r
					turnplose()
				else:
					turnpwin()

	def fightinventory():
		global player
		items = []
		clear()
		i=1
		if player.items: #if inventory is not empty
			print("Inventory:\n")
			print("Please select an item to use")
			for item in player.items: #iterate over items in inventory
				c = str_to_class(item) #string to class without using eval
				print(str(i) + ") Use 1 x " + c.name + " (Qty: " + player.items[item] + ")")
				items.append(item)
				i=i+1
		else:
			print("Inventory: (empty)\n")
		print(str(i) + ") Back to fight")
		selection = input("> ")
		for x in range(1, i): #create the actual options - iterating over the amount of items in inventory
			if selection == str(x): #if the selected item is item being iterated right now
				usage = use(items[x-1]) #use selected item
				if usage == 1:
					clear()
					mainbattle() #back to fight
				else:
					clear()
					print("You do not need a Health Potion right now. (Press enter to go back to fight)") #fix this if more effects are added
					input("> ")
					clear()
					mainbattle()

		if selection == str(i): #if the last option is selected - which is back to fight
			clear()
			mainbattle()
		else:
			clear()
			mainbattle()

	def turnpwin():
		global player, enemy
		enemy.curhp = str(int(enemy.curhp) - int(playerweapon.dmg))
		clear()
		battlescreen()
		print("\n" + player.name + " used " + playerweapon.name)
		print(enemy.name + " used " + enemyweapon.name)
		print(player.name + "'s attack succeeded. " + enemy.name + " loses " + playerweapon.dmg + " HP.")
		input("> ")
		clear()
		mainbattle()

	def turnplose():
		global player, enemy
		player.curhp = str(int(player.curhp) - int(enemyweapon.dmg))
		clear()
		battlescreen()
		print("\n" + player.name + " used " + playerweapon.name)
		print(enemy.name + " used " + enemyweapon.name)
		print(player.name + "'s attack failed. " + player.name + " loses " + enemyweapon.dmg + " HP.")
		input("> ")
		clear()
		mainbattle()

	def turntied():
		global player, enemy
		clear()
		battlescreen()
		print("\n" + player.name + " used " + playerweapon.name)
		print(enemy.name + " used " + enemyweapon.name)
		print(player.name + " and " + enemy.name + " are tied.")
		input("> ")
		clear()
		mainbattle()

	def playerdie():
		global player
		clear()
		player.lives = str(int(player.lives) - 1)
		player.curhp = player.tothp
		if int(player.lives) == int(0):
			print("You took a huge amount of beatings, and therefore you have perished. It is indeed a sad day.")
			input("> ")
			initiate()
		else:	
			print(enemy.name + " won the fight.")
			print(player.name + " fainted! You can only faint " + player.lives + " more times. (Press enter to continue)")
			input("> ")
			mg()

	def enemydie():
		global player, enemy
		clear()
		eexp = str(int(enemy.tothp) * 2)
		ebp = str((int(player.curhp) + int(enemy.level)) + 2)
		player.exp = str(int(player.exp) + int(eexp))
		player.bp = str(int(player.bp) + int(ebp))
		player.curhp = player.tothp
		print("Congratulations!\n" + player.name + " won the fight, and " + enemy.name + " died!\n")
		print("You earned " + eexp + " exp and " + ebp + " gold!")
		if int(player.exp) >= int(lreq()):
			player.exp = str(int(player.exp) - int(lreq()))
			player.level = str(int(player.level) + 1)
			player.lives = "3"
			player.tothp = str(int(player.tothp) + 2)
			player.curhp = player.tothp
			print("Your HP has been fully restored.")
			print("\nDING! You've leveled up. You are now in level " + player.level + "!")
			print("You do now have " + player.tothp + "HP!")
			print("Your lives have been fully restored.\n")
		else:
			print("Your HP has been fully restored. (Press enter to continue)")
		input("> ")
		mg()

	mainbattle()
#fighting gameloops end

#general action gameloops start
def apoth():
	clear()
	global player
	location("apoth")
	if player.apoth == "0":
		print("As you enter through the door of \"Ole Apothecary\", the stench of leeches, and probably medicine which you assume is uncertified, hits your nose.\nBehind the counter sits an old and mysterious looking man. He beckons you over.\n")
		print("Shopkeeper: \"Would you like to purchase something? Well, as a matter of fact I only have health potions for sale, but those will do as good as any medicine.\"")
		player.apoth = "1" #player has visited apoth before
	else:
		print("Shopkeeper: \"Would you like to purchase something?\"")
	print("\nCurrent balance: " + player.bp + " gold")

	i=1
	for n in apothstock: #fetch items from the apothstock list. Awesomeness, and possibility for more items. Ooh.
		c = str_to_class(n) #no eval here - thanks so
		if(int(player.level) >= int(c.levelreq)):
			print(str(i) + ") Buy 1 x " + c.name + ": " + c.desc + " - costs " + c.cost + " gold - requires level " + c.levelreq) #print the items based on apothstock list
			i=i+1
	print(str(i) + ") Back to town")

	purchase = input("> ")

	for x in range(1, i): #create the actual options - iterating over the amount of products in shop
		if purchase == str(x): #if the purchase is the current item
			finbuy = buy(apothstock[x-1]) #buy selected item
			if finbuy == "1": #if palyer has enough bp
				clear()
				c = str_to_class(apothstock[x-1]) #no eval here
				location("apoth")
				print("You have purchased one \"" + c.name + "\" at the price of " + c.cost + " gold.\n1) Back to Ole Apothecary\n2) Back to town")
				selection = input("> ")
				if selection == "1":
					apoth()
				else:
					mg()
			else: #not enouugh bp
				clear()
				location("apoth")
				print("You do not have enough gold to purchase this item.\n1) Back to Ole Apothecary\n2) Back to town")
				selection = input("> ")
				if selection == "1":
					apoth()
				else:
					mg()

	if purchase == str(i): #if the last option is selected - which is back to town
		mg()
	else:
		apoth()

def smith():
	clear()
	global player
	location("smith")
	if player.smith == "0":
		print("As you come closer to the town's blacksmith, the noise of a hammer clanking is easily heard. The smell is a mix of fire and sweat, and your resolve to approach the big and scary looking blacksmith diminishes a bit. But you do so anyway.\n")
		print("Smith: \"Eh, what will it be? I can fix yer weapons or give yer new ones. Take a look o'er there at the weapons rack.\"")
		player.smith = "1" #player has visited apoth before
	else:
		print("Smith: \"Eh, what will it be?\"")
	print("\nCurrent balance: " + player.bp + " gold\tCurrent level: " + player.level + "\nCurrent weapons: Rock: " + str_to_class(player.weapons["r"]).name + " (" + str_to_class(player.weapons["r"]).tier + ")\tPaper: " + str_to_class(player.weapons["p"]).name + " (" + str_to_class(player.weapons["p"]).tier + ")\tScissors: " + str_to_class(player.weapons["s"]).name + " (" + str_to_class(player.weapons["s"]).tier + ")\n") #print player information. Look for the players current weapons, and find the corresponding weapon object/class.

	i=1
	for n in smithr:
		c = str_to_class(n)
		if int(str_to_class(player.weapons[c.type]).tier) == int(c.tier) - 1: #only print items that require one tier above the currently held tier
			print(str(i) + ") Upgrade weapon type \"" + weaponcategories[c.type] + "\" to \"" + c.name + "\" - damages: " + c.dmg + " (" + c.cost + " gold)\n\tRequires: Level: " + c.lreq + "\t" + weaponcategories[c.type] + " tier: " + c.treq + "\n") #print the items based on smithr list
			i=i+1
		elif int(str_to_class(player.weapons[c.type]).tier) == int(c.tier) + 1: #if you are maxed out
			print(str(i) + ") You can not upgrade weapon type \"" + weaponcategories[c.type] + "\" any more.\n")
			i=i+1

	for n in smithp:
		c = str_to_class(n)
		if int(str_to_class(player.weapons[c.type]).tier) == int(c.tier) - 1:#only print items that require one tier above the currently held tier
			print(str(i) + ") Upgrade weapon type \"" + weaponcategories[c.type] + "\" to \"" + c.name + "\" - damages: " + c.dmg + " (" + c.cost + " gold)\n\tRequires: Level: " + c.lreq + "\t" + weaponcategories[c.type] + " tier: " + c.treq + "\n") #print the items based on smithp list
			i=i+1
		elif int(str_to_class(player.weapons[c.type]).tier) == int(c.tier) + 1: #if you are maxed out
			print(str(i) + ") You can not upgrade weapon type \"" + weaponcategories[c.type] + "\" any more.\n")
			i=i+1
	for n in smiths:
		c = str_to_class(n)
		if int(str_to_class(player.weapons[c.type]).tier) == int(c.tier) - 1:#only print items that require one tier above the currently held tier
			print(str(i) + ") Upgrade weapon type \"" + weaponcategories[c.type] + "\" to \"" + c.name + "\" - damages: " + c.dmg + " (" + c.cost + " gold)\n\tRequires: Level: " + c.lreq + "\t" + weaponcategories[c.type] + " tier: " + c.treq + "\n") #print the items based on smiths list
			i=i+1
		elif int(str_to_class(player.weapons[c.type]).tier) == int(c.tier) + 1: #if you are maxed out
			print(str(i) + ") You can not upgrade weapon type \"" + weaponcategories[c.type] + "\" any more.\n")
			i=i+1

	print(str(i) + ") Back to town")

	upg = input("> ")

	for x in range(1, i): #create the actual options - iterating over the amount of products in shop
		if upg == str(x): #if the purchase is the current item
			finupg = upgrade(weapontypes[x-1]) #upgrade selected weapon type
			if finupg == "1": #if all requirements are met
				clear()
				location("smith")
				print("You have upgraded your weapon in weapon type \"" + weaponcategories[weapontypes[x-1]] + "\" to \"" + str_to_class(player.weapons[weapontypes[x-1]]).name + "\" at the price of " + c.cost + " gold.\n1) Back to Ye Smithe o'er All\n2) Back to town")
				selection = input("> ")
				if selection == "1":
					smith()
				else:
					mg()
			elif finupg == "0": #does not meet requirements
				clear()
				location("smith")
				print("You do not meet the requirements to upgrade this weapon.\n1) Back to Ye Smithe o'er All\n2) Back to town")
				selection = input("> ")
				if selection == "1":
					smith()
				else:
					mg()
			elif finupg == "2":
				clear()
				location("smith")
				print("You are currently maxed out in this weapon type, and can therefore not upgrade.\n1) Back to Ye Smithe o'er All\n2) Back to town")
				selection = input("> ")
				if selection == "1":
					smith()
				else:
					mg()
	if upg == str(i): #if the last option is selected - which is back to town
		mg()
	else:
		smith()
#general action gameloops end

#newgame gameloops start
def ng1():
	clear()
	print("Welcome hither, new one.\nWhat is your name?")
	name = input("> ")
	print("Aha. Welcome to the lands of Ropasci, " + name + ".\n\nRopasci is the great and wonderful land of rock-paper-scissors.\nIn this land you will meet bandits, monsters, lords and blobs, and there's even a chance you might meet our evil king. Though, I wouldn't wish that for anyone.\n\nBefore we begin, would you want me to introduce you to the rules of the game?\n1) Yes \n2) No\n3) Hold up! My name's wrong\n4) Exit to main menu")
	initinstruct = input("> ")
	if initinstruct == "1":
		instructions(1, name)
	elif initinstruct == "2":
		ng2(name, 1) #go to step two and tell it we skipped
	elif initinstruct == "3":
		ng1()
	elif initinstruct == "4":
		initiate()
	else:
		ng1()

def ng2(name, skip = 0):
	clear()
	if skip == 1:
		print("So, " + name + ". Here we are.")
	else:
		print("So, " + name + ". Now you know the rules to RopasciRPG.")

	print("\nBefore we begin the actual adventure, I would like to get to know you a bit.\nSo, tell me, what is your gender?\n1) Male\n2) Female")
	gender = input("> ")

	if gender == "1":
		gender = "Male"
	elif gender == "2":
		gender = "Female"
	else:
		ng2(name, skip)

	print("What is your race?\n1) Elf\n2) Human\n3) Troll\n4) Fairy")
	race = input("> ")

	if race == "1":
		race = "Elf"
	elif race == "2":
		race = "Human"
	elif race == "3":
		race = "Troll"
	elif race == "4":
		race = "Fairy"
	else:
		ng2(name, skip)

	print("Marvelous, " + name + ". It seems you're a \"" + gender + " " + race + "\". Is this correct?\n1) Yes\n2) No")
	correctinfo = input("> ")

	if correctinfo == "1":
		create(name, gender, race)
		mg()
	elif correctinfo == "2":
		ng2(name, skip)
#newgame gameloops end

def instructions(init=0, name=""):
	clear()
	if init == 1:
		print("Alright, " + name + " the rules are as follow:\n")
	print("RopasciRPG is a rock-paper-scissors game with RPG elements, as the name sort of implies.\nLet's take it bite for bite.\n")
	print("When you create a new character, you get to choose a name, a gender and a race. As of current version, gender and race will not make a difference in-game (this might change if I make future updates).\nHereafter, you will arrive at the Town Center. This is the \"hub\" of the game, and from here you get to choose what you want to do. The options are:\n1) Look for trouble\n2) Go to \"Ole Apothecary\"\n3) Go to \"Ye Smithe o'er All\"\n4) Save game\n5) Exit to main menu\n")
	print("1) Look for trouble\nLook for trouble initiates a fight. You will meet an NPC that is the same level as you, and you will get to fight him. You have a single chance to flee from your opponent, but there's only a 40 percent chance of success. Failing will force you to fight the opponent.\n")
	input("> (Press enter for next page)")
	clear()
	print("2) Go to \"Ole Apothecary\"\nThe \"Ole Apothecary\" is the medical shop of the town. Here, you can buy Health Potions and Health Potions. How it works is pretty self-explanatory.\n")
	print("3) Go to \"Ye Smithe o'er All\"\nThe \"Ye Smithe o'er All\" is the town's blacksmith. Here, you get to upgrade your weapons to their next tier.\n")
	print("4) Save game\nThis option is pretty self-explanatory. You get to save your game, so you can return to it later. Please check that after you have saved, a \"saves\" folder with the chosen name exists next to the .py file. If not, perhaps some permissions are off.\n")
	print("5) Exit to main menu\nThis options puts you back to the main menu. But don't worry, it asks you if you're sure before doing so.")
	input("> (Press enter for next page)")
	clear()
	print("Fighting:\nA fight is a normal rock-paper-scissors duel as you would expect it. Rock beats scissors, scissors beat paper, paper beats rock.\nA fight is a battle between an NPC and you as the player. It ends when either of you hit 0HP.\nWhen you initiate in a fight, you get 4 options. They are:\n1) Rock\n2) Paper\n3) Scissors\n4) Use item\n\nYou simply select the weapon that you wish to use, and then you get to know whether you, in this turn, beat the opponent or not.\nIf you hit, you damage the amount of damage that your current weapon deals. In the beginning, this will be 1HP, but as you upgrade your weapons, you get to deal more damage.\nPlease note that an upgraded weapon in a particular weapon-type does not win over a non-upgraded weapon in it's defeating type.\nFor example: A tier 2 rock-type weapon will not beat a tier 1 paper-type weapon, as paper beats rock.")
	input("> (Press enter for next page)")
	clear()
	print("4) Use items\nThis will open a menu where you can select and use your items. In the current version, you can only buy Health Potions, so you could call the inventory a potion bag. Whatever. Also, everyone starts with 1 Health Potion.\n")
	print("Lives:\nIn RopasciRPG you start with 3 lives. This is the amount of times you're allowed to lose a fight. If your lives reach 0, you die. But, don't despair, whenever you level up, your lives go back up to full again!")
	input("> (Press enter for next page)")
	clear()
	print("Leveling:\nYou level once you reach the amount of experience points required for the next level. You can always see how many experience points you have, and how many you need, in the Town Center.\nLeveling up gives you 2 more HP, and unlocks new weapon upgrades. The max level is 3.\n")
	print("How is exp calculated?\nIt is simple. You get the amount of total HP your opponent had, multiplied by 2. So, if you're in level 1, you will always get 6 exp for beating the opponent. Level 2 is 10 exp and so on and so forth.\n")
	print("How is gold calculated? And what is gold?\nThere are two factors which determine how many gold you win from a fight. These two factors added together and then adding 2 on top of that gives you your earned gold.\nFactor 1: Your remaining HP at the end of a fight, multiplied by 2. So, if you end the fight with 4HP, you get 4 gold from that. If you end it with 1HP, you get 1 gold from that factor.\nFactor 2: The opponent's level. So, if you fight against a level 1 Thug, you get 1 gold from that factor. And then, as mentioned, we add 2 to that value to get the final earned gold.")
	input("> (Press enter for last page)")
	clear()
	print("What are the weapon tiers?\nRock-type:\nTier 1: Rock\nTier 2: Boulder\nTier 3: Anvil\n\nPaper-type:\nTier 1: Paper\nTier 2: Tinfoil\nTier 3: Duct Tape\n\nScissors-type:\nTier 1: Scissors\nTier 2: Knife\nTier 3: Sword\n")
	print("Anything else I need to know?\nI don't think so. If you experience any bugs, let me know over at GitHub.\n\nHave fun!")
	if init == 1:
		input("> (Press enter to go to character creation)")
		ng2(name)
	else:
		input("> (Press enter to return to the main menu)")
		initiate()

def about():
	clear()
	print("Read the instructions for a detailed \"about\" on RopasciRPG. I'd just like to tell you why this game was made.\n")
	print("This game was made as an entry to www.teamtreehouse.com's \"Forum contest\", where you're supposed to create a rock-paper-scissors-ish game. And so I did. I hope you enjoy it throughly.\n")
	print("If you're a developer yourself, and want to contribute to this project, you can do so via GitHub. I don't know if I'll be developing more on it myself, but I might. Please note that the source is only sporadically commented, and thus a bit troublesome to maintain. But, I believe I commented the most complicated pieces of the code pretty well. At least I think so.\n")
	print("License: This is released under the \"DWYWWIJDSI\" (Do whatever you want with it, just don't sell it) license. Enjoy!")
	input("> (Press enter to return to the main menu)")
	initiate()

def save():
	clear()
	print("What would you like to call your savegame? (Type \"Back\" to go back to the menu)")
	filename = input("> ")
	filename = filename.lower()
	if filename == "back":
		mg()

	if not os.path.exists("saves"):
		os.makedirs("saves")

	file = pathlib.Path('saves/' + filename + ".rps")
	if file.exists():
		print("A savegame with this name already exists. Would you like to overwrite?\n1) Yes\n2) No")
		selection = input("> ")
		if selection == "1":
			f = open("saves/" + filename + ".rps", "wb")
			pickle.dump(player, f, pickle.HIGHEST_PROTOCOL) #dump object using pickle
			f.close()
			print("Your game has been saved. Press enter to continue.")
			enter = input("> ")
			if enter == "":
				mg()
			else:
				mg()
		else:
			save()
	else:
		f = open("saves/" + filename + ".rps", "wb")
		pickle.dump(player, f, pickle.HIGHEST_PROTOCOL)
		f.close()
		print("Your game has been saved. Press enter to continue.")
		enter = input("> ")
		if enter == "":
			mg()
		else:
			mg()

def load():
	clear()
	global player
	savedgames = []
	if os.path.exists("saves"):
		for file in os.listdir("saves"):
			if file.endswith(".rps"):
				savedgames.append(file[:-4])

	if not savedgames:
		print("No savegames exist. Press enter to return to the main menu.")
		enter = input("> ")
		if enter == "":
			initiate()
		else:
			initiate()
	else:
		print('The following savegames exist:\n%s' % '\t'.join(map(str, savedgames)) + "\nWhich one would you like to load? (type \"Back\" to return to the main menu)")
		loadfile = input("> ")
		if loadfile == "back":
			initiate()
		else:
			file = pathlib.Path('saves/' + loadfile + ".rps")
			if file.exists():
				with open('saves/' + loadfile + '.rps', 'rb') as f:
					player = pickle.load(f)
					createnoplayer()
				mg()
			else:
				load()

def gameexit():
	clear()
	print("Goodbye.")
	exit()
#gameloops end

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
	cost = ""
	effect = "" #heal
	value = "" #amount of heal
	levelreq = ""

	def __init__(self, name, shortname, desc, cost, effect, value="0", levelreq="1"):
		self.name = name
		self.shortname = shortname
		self.desc = desc
		self.cost = cost
		self.effect = effect
		self.value = value
		self.levelreq = levelreq
#classes end

#declarations start
player, hp, majhp, mindetector, majdetector, rock, paper, scissors, boulder, tinfoil, knife, anvil, duct, sword, enemy, playerselect, playerweapon, enemyweapon = (0,)*18
#mob declarations start
thug, bandit, eblob, chorse, wolf, magician, madp, lordling = (0,)*8 #level 1 mobs
bleader, mmagician, cblob, mlumberjack, osailor, gnometroll, eknight, slayerman, deserter, lord = (0,)*10 #level 2 mobs
wyvern, lynx, kblob, gmad, cminelo, hbandit, cunicorn, kgnometroll, enlord, mcriminal, ebear, king = (0,)*12 #level 3 mobs
#mob declarations end
l1mobs = ["thug", "bandit", "eblob", "chorse", "wolf", "magician", "madp", "lordling"]
l2mobs = ["bleader", "mmagician", "cblob", "mlumberjack", "osailor", "gnometroll", "eknight", "slayerman", "deserter", "lord"]
l3mobs = ["wyvern", "lynx", "kblob", "gmad", "cminelo", "hbandit", "cunicorn", "kgnometroll", "enlord", "mcriminal", "ebear", "king"]
levelreqs = {"2":"25","3":"50","4":"9999"}
apothstock = ["hp", "majhp", "mindetector", "majdetector"]
smithr = ["boulder", "anvil"]
smithp = ["tinfoil", "duct"]
smiths = ["knife", "sword"]
weaponcategories = {"r": "Rock", "p": "Paper", "s": "Scissors"}
rtiers = ["rock", "boulder", "anvil"] #remember- index based
ptiers = ["paper", "tinfoil", "duct"] #remember- index based
stiers = ["scissors", "knife", "sword"] #remember- index based
weapontypes = ["r","p","s"] #so 1,2 and 3 correspond to the different weapon types
locations = {"town":"Town Center","oot":"Out of Town","apoth":"Ole Apothecary","smith": "Ye Smithe o'er All"} #for def: locations
#declarations end

#functions start
def buy(item):
	global player
	c = str_to_class(item) #no eval, yo
	if int(player.bp) >= int(c.cost) and int(player.bp) > 0:
		if c.shortname in player.items: #if item exists in inventory
			player.items[c.shortname] = str(int(player.items[c.shortname]) + 1) #add to the quantity
		else: #if it does not exist in inventory
			player.items[c.shortname] = '1' #create it
		player.bp = str(int(player.bp) - int(c.cost)) #convert to int, subtract, convert to string and add to player class
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
		#print(str(str_to_class(player.weapons[a.type]).tier))
		player.bp = str(int(player.bp) - int(b.cost))
		player.weapons[type] = b.shortname
		print(player.weapons[type])
		return "1"
	else:
		return "0"

def use(item):
	global player
	def mainuse():
		if int(player.items[item]) == 1: #if it is the last of item - delete it from dictionary
			application = applyeffect(item)
			if application == 1:
				del player.items[item]
				return(1)
			else:
				return(0)
		else: #if not the last, remove one from quantity
			application = applyeffect(item)
			if application == 1:
				player.items[item] = str(int(player.items[item]) - 1)
				return(1)
			else:
				return(0)

	def applyeffect(item):
		item = str_to_class(item)

		if(item.effect == "heal"):
			if (int(player.curhp)) <= (int(player.tothp) - int(item.value)):
				player.curhp = str(int(player.curhp) + int(item.value))
				return(1)
			elif (int(player.curhp)) < int(player.tothp):
				player.curhp = str(int(player.tothp))
				return(1)
			else:
				return(0)
		if(item.effect == "detect"):
			clear()
			prefs = enemy.pref
			amntofone = 0
			for key, value in prefs.items():
				if value == 1:
					amntofone = amntofone + 1
			prefmax = max(prefs.keys(), key=(lambda key: prefs[key]))
			types = weaponcategories
			prefmin = min(prefs.keys(), key=(lambda key: prefs[key]))
			detected = random.random()
			if detected > 0.40 or item.value == "1":
				print("You managed to succesfully detect " + enemy.name + "'s weapon preferences:")
				if(amntofone > 1 and amntofone < 3):
					print(enemy.name + "'s preferred weapon is: " + types[prefmax] + "-type weapons.")
					del types[prefmax]
					print(enemy.name + "'s least preferred weapons are: " + types[1] + "-type weapons and " + types[2] + "-type weapons.")
				elif(amntofone == 3):
					print(enemy.name + " does not have a preferred weapon type.")
				else:
					print(enemy.name + "'s most preferred weapon is: " + types[prefmax] + "-type weapons.")
					print(enemy.name + "'s least preferred weapon is: " + types[prefmin] + "-type weapons.")
				input("> ")
				return(1)
			else:
				print("You did not manage to detect " + enemy.name + "'s weapon preferences.\n")
				input("> ")
				return(0)
	return mainuse()

def location(loc):
	print("Location: " + locations[loc] + "\n")

def createplayer(name, gender, race):
	global player
	player = Player(name, gender, race)

def createitems():
	#Adding more items? Remember to declare the global as well, and create it as an empty variable in the declarations block
	global hp, majhp, mindetector, majdetector
	hp = Item("Health Potion", "hp", "heals 1 HP", "10", "heal", "1", "1")
	majhp = Item("Major Health Potion", "majhp", "heals 2 HP", "15", "heal", "2", "2")
	mindetector = Item("Minor Revelation Potion", "detector", "tries to detect enemy weapon preferences", "5", "detect", "0", "1")
	majdetector = Item("Major Revelation Potion", "majdetector", "detects enemy weapon preferences", "7", "detect", "1", "2")

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

def createenemies(number=4):
	#argument order name, shortname, taunts, pref, weapons, tothp, curhp, level
	global thug, bandit, eblob, chorse, wolf, magician, madp, lordling, bleader, mmagician, cblob, mlumberjack, osailor, gnometroll, eknight, slayerman, deserter, lord, wyvern, lynx, kblob, gmad, cminelo, hbandit, cunicorn, kgnometroll, enlord, mcriminal, ebear, king
	#level 1 enemies
	thug = Enemy("Thug", "thug", ["Eh, what are you up to?", "Come over here, mate.", "What have we here?"], {"r":1.1,"p":0.95,"s":0.95})
	bandit = Enemy("Bandit", "bandit", ["Let me rob you.", "You're too far from home!", "Hehehe."], {"r":1.1,"p":0.95,"s":0.95})
	eblob = Enemy("Evil Blob", "eblob", ["Bloob."])
	chorse = Enemy("Corrupted Horse", "chorse", ["Neeeigh! (Oxford Dictionary says this is the sound a horse makes)"])
	wolf = Enemy("Wolf", "wolf", ["Grrrr!"])
	magician = Enemy("Magician", "magician", ["I've got this new spell. It's called SCISSORS!", "Hullo, hullo. Dis is ma' forest.", "It shall be delightful to slaughter you."], {"r":0.9,"p":1,"s":1.1})
	madp = Enemy("Mad Peasant", "madp", ["Where am I? Who are you? DIE!", "I am so angry with my wife. You shall suffer from it.", "Watch where you stand! This is my soil!"])
	lordling = Enemy("Lordling", "lordling", ["How darest thou step feet on my property? Watch this piece of silver paper eradicate you.", "Peasant! Obey me, and die to this piece of magical silver paper.", "Silver paper is what saves me. As you shall well discover."], {"r":1,"p":1,"s":1}, {"r": "rock", "p": "tinfoil", "s": "scissors"})
	
	#level 2 enemies
	bleader = Enemy("Bandit Leader", "bleader", ["You might seem so big and strong and cool. But, watch me!", "Welcome to the dark part of the lands.", "Heeeheeeheee! Exterminate!"], {"r":1.1,"p":0.95,"s":0.95}, {"r": "boulder", "p": "paper", "s": "scissors"}, "5", "5", "2")
	mmagician = Enemy("Master Magician", "mmagician", ["I've got this well practiced magical spell. It's called KNIFE!", "Feel my eternal wrath.", "I am the Master of the Lesser Magicians."], {"r":0.9,"p":1,"s":1.1}, {"r": "rock", "p": "paper", "s": "knife"}, "5", "5", "2")
	cblob = Enemy("Corrupted Blob", "cblob", ["Blooob."], {"r":1,"p":1,"s":1}, {"r": "rock", "p": "tinfoil", "s": "scissors"}, "5", "5", "2")
	mlumberjack = Enemy("Maniac Lumberjack", "mlumberjack", ["Yiaargh! I will chop yer down like an oak!!", "Chop, chop, chop. All day long. Now for some smashing.", "I had a wife once. Hehehe."], {"r":0.95,"p":0.95,"s":1.1}, {"r": "rock", "p": "paper", "s": "knife"}, "5", "5", "2")
	osailor = Enemy("Old Sailor", "osailor", ["I have sailed all the seven seas. Now, I want to sail in your blood.", "Once I was a sailor. I lost everything I owned, because one of these petty lords came and took her while I was away. To this day, anger and rage is all I know.", "Hoist the sails!"], {"r":0.9,"p":1.1,"s":1}, {"r": "rock", "p": "tinfoil", "s": "scissors"}, "5", "5", "2")
	gnometroll = Enemy("Gnometroll", "gnometroll", ["Yeargheeeaaa! Huxklaen ma, da hexin pelof!"], {"r":1,"p":1,"s":1}, {"r": "bolder", "p": "paper", "s": "scissors"}, "5", "5", "2")
	eknight = Enemy("Evil Knight", "eknight", ["Valor and honour. These are the words by which I live. At least when the princess is nearby.", "I serve the king, and the darkness of my rotten heart.", "What are you doing so far from any civilization? Now die."], {"r":1.1,"p":0.95,"s":0.95}, {"r": "boulder", "p": "paper", "s": "scissors"}, "5", "5", "2")
	slayerman = Enemy("Slayerman", "slayerman", ["Mhe. Heh. I.. Well, yes.. I am the Slayerman. Hah. Haha! Heh.", "Heeeellooo, heelloooo. Who.. Who is this dawdling person I.. I meet? HAH! Hehe. I am the Slayerman.", "I.. I am the Slayerman. And I want to play a game."], {"r":1,"p":1.1,"s":0.9}, {"r": "rock", "p": "tinfoil", "s": "scissors"}, "5", "5", "2")
	deserter = Enemy("Deserter", "deserter", ["I've got half the kingdom chasing me down. I am not afraid of a mere peasant such as you.", "Don't blink, or you'll die.", "STOP! And fight."], {"r":1,"p":1,"s":1}, {"r": "boulder", "p": "paper", "s": "scissors"}, "5", "5", "2")
	lord = Enemy("Lord", "lord", ["I am the Lord of Meagerlands, and you have most definitely trespassed.", "For as I, the Lord, has decreed, so shall you be slain.", "What a little, powerless person you are. Take up your arms!"], {"r":1,"p":1,"s":1}, {"r": "rock", "p": "paper", "s": "sword"}, "5", "5", "2")

	#level 3 enemies
	wyvern = Enemy("Wyvern", "wyvern", ["Raaaaarrrgh!", "Reearrgh!"], {"r":1,"p":1,"s":1}, {"r": "anvil", "p": "paper", "s": "scissors"}, "7", "7", "3")
	lynx = Enemy("Lynx", "lynx", ["Grrrr!"], {"r":1,"p":1,"s":1}, {"r": "rock", "p": "duct", "s": "scissors"}, "7", "7", "3")
	klob = Enemy("King Blob", "klob", ["Bloooob!"], {"r":1,"p":1,"s":1}, {"r": "rock", "p": "paper", "s": "sword"}, "7", "7", "3")
	gmad = Enemy("General Mad", "gmad", ["I was once a general. I lost it all to the test of time. Too bad, so sad.", "Mad. Mad. Who's mad? Me mad? You mad. Die, you cow.", "I just wanted to ride the horse."], {"r":1.1,"p":0.9,"s":1}, {"r": "anvil", "p": "paper", "s": "scissors"}, "7", "7", "3")
	cminelo = Enemy("Captain Minelo", "cminelo", ["Hi there! Have you seen my friend, the old sailor? I've been looking everywhere for him, btu he is simply gone. Oh my, oh my. Well, you'll do as good as any.", "I come from the ocean. And as the ocean, I show no mercy.", "Merciful is the one who is merciful. I am not that one."], {"r":1,"p":1.1,"s":0.9}, {"r": "rock", "p": "paper", "s": "sword"}, "7", "7", "3")
	hbandit = Enemy("Horse Bandit", "hbandit", ["What have we here? A frisk one. More likely a dead one.", "Hello. Goodbye.", "I've been watching you for days, slaying all these people. Now you're up."], {"r":1,"p":1,"s":1}, {"r": "rock", "p": "duct", "s": "scissors"}, "7", "7", "3")
	cunicorn = Enemy("Corrupted Unicorn", "cunicorn", ["Neeeeeigh!"], {"r":1,"p":1,"s":1}, {"r": "rock", "p": "paper", "s": "sword"}, "7", "7", "3")
	kgnometroll = Enemy("King Gnometroll", "kgnometroll", ["Se mulos, mulos mak. Der teflaren digmo!"], {"r":1,"p":1,"s":1}, {"r": "anvil", "p": "paper", "s": "scissors"}, "7", "7", "3")
	enlord = Enemy("Envious Lord", "enlord", ["Oh, how I wish I could be free from these chains. These shackles burden me.", "All this responsibility is most definitely tiring.", "I am a sleepwalker, and oh how I wish I was not!"], {"r":0.95,"p":1,"s":0.95}, {"r": "rock", "p": "duct", "s": "scissors"}, "7", "7", "3")
	mcriminal = Enemy("Mad-eyed Criminal", "mcriminal", ["I robbed a wagon full of jewelry. Which is why I wear this pretty necklace.", "I killed an entire family, and afterwards I slept in their beds. Heeh.", "I stabbed a lord in the heart. He was too lordly for me."], {"r":1,"p":1,"s":1}, {"r": "rock", "p": "paper", "s": "sword"}, "7", "7", "3")
	ebear = Enemy("Evil Bear", "ebear", ["Raargh!"], {"r":1,"p":1,"s":1}, {"r": "anvil", "p": "paper", "s": "scissors"}, "7", "7", "3")
	king = Enemy("King of Ropasci", "king", ["Halt, company! Who is this traveler? He seems to be challenging to me. Off you pop, little one.", "Halt, company! It seems we've hit a bump in the road, and the bump shall now suffer.", "I am the great King of Ropasci. How darest thou look at me?"], {"r":1,"p":1,"s":1}, {"r": "anvil", "p": "duct", "s": "sword"}, "7", "7", "3")

def create(name, gender, race):
	createplayer(name, gender, race)
	createnoplayer()

def createnoplayer():
	createitems()
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

def str_to_class(str): # no need to use eval. Eval is bad for you.
	return getattr(sys.modules[__name__], str)
#functions end

#run it all
if __name__ == '__main__':
	main()