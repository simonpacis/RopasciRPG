#fighting gameloops start
def initfight():
	global player, enemy, playerselect
	clear()
	if player.oot == "0":
		location("oot")
		print("As you leave behind the town, and enter out into the wild nature and fresh air, you begin to slowly grow more and more worried. You think you hear sounds around every single corner. You're slowly, slowly walking. Wh-what was that s-sound?\n\n" + player.name + ": \"Hello? Anyone there?\"")
		input("> ")
		clear()
		player.oot = "1"
	#create and select the opponent
	
	enemy = pickle.loads(pickle.dumps(enemies[random.choice(list(enemies.keys()))])) # select random enemy from enemies dict and do pickle.dump and load to make a clone of the enemy.
	while int(enemy.level) != int(player.level):
		enemy = pickle.loads(pickle.dumps(enemies[random.choice(list(enemies.keys()))]))
		pass

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
		print(underline(player.name) + red("\tHP: " + player.curhp + "/" + player.tothp) + "\t\tLives: " + player.lives + "\nLvl: " + player.level + blue("\tExp: " + player.exp + "/" + lreq() + "\n")) #print player information
		print(bold("Your enemy:") + "\n" + underline(enemy.name) + red("\tHP: " + enemy.curhp + "/" + enemy.tothp) + "\n\n")

		if player.items: #if inventory is not empty
			print(bold("Inventory:"), end=" ")
			for item in player.items: #iterate over items in inventory
				c = items[item] #string to class without using eval
				print(c.name + ": " + player.items[item] + "\t", end=" ") #print item and tab it at the end + no newline
		else:
			print(bold("Inventory: ") + "(empty)", end=" ")

		print(bold("\n\nCurrent weapons:") + "\nRock: " + str_to_class(player.weapons["r"]).name + " (" + str_to_class(player.weapons["r"]).tier + ")\nPaper: " + str_to_class(player.weapons["p"]).name + " (" + str_to_class(player.weapons["p"]).tier + ")\nScissors: " + str_to_class(player.weapons["s"]).name + " (" + str_to_class(player.weapons["s"]).tier + ")\n")

	def mainbattle():
		global playerselect
		if int(player.curhp) <= 0:
			playerdie()
		elif int(enemy.curhp) <= 0:
			enemydie()

		battlescreen()
		prefs = enemy.pref

		amntofone = 0 #amount of preferences at 1; no preference in given category

		for key, value in prefs.items():
			if value == 1:
				amntofone = amntofone + 1

		if "constdetector" in player.items: #player has obtained constant preference detector
			types = weaponcategories

			prefmax = max(prefs.keys(), key=(lambda key: prefs[key]))
			if(amntofone == 2 or amntofone == 1):
				if(prefmax == "r"):
					print("\n1) (or r) " + str_to_class(player.weapons["r"]).name)
					print(bold("2) (or p) " + str_to_class(player.weapons["p"]).name))
					print("3) (or s) " + str_to_class(player.weapons["s"]).name)					
				if(prefmax == "p"):
					print("\n1) (or r) " + str_to_class(player.weapons["r"]).name)
					print("2) (or p) " + str_to_class(player.weapons["p"]).name)
					print(bold("3) (or s) " + str_to_class(player.weapons["s"]).name))
				if(prefmax == "s"):
					print(bold("\n1) (or r) " + str_to_class(player.weapons["r"]).name))
					print("2) (or p) " + str_to_class(player.weapons["p"]).name)
					print("3) (or s) " + str_to_class(player.weapons["s"]).name)
				print("4) Use item")
				print("5) Taunt")
			else:
				print(bold("\n1) (or r) " + str_to_class(player.weapons["r"]).name + "\n2) (or p) " + str_to_class(player.weapons["p"]).name + "\n3) (or s) " + str_to_class(player.weapons["s"]).name) + "\n4) Use item\n5) Taunt")
		else:
			print("\n1) (or r) " + str_to_class(player.weapons["r"]).name + "\n2) (or p) " + str_to_class(player.weapons["p"]).name + "\n3) (or s) " + str_to_class(player.weapons["s"]).name + "\n4) Use item\n5) Taunt")
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
		elif fsel == "4":
			fightinventory()
		else:
			fighttaunt()

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

	def fighttaunt():
		clear()
		print("As you taunt %s, you hear in response:\n" % (enemy.name))
		print(enemy.name + ": \"" + random.choice(enemy.taunts) + "\"\n")
		input("> (Press enter to return to battle)")
		clear()
		mainbattle()

	def fightinventory():
		global player
		localitems = []
		clear()
		i=1
		if player.items: #if inventory is not empty
			print("Inventory:\n")
			print("Please select an item to use")
			for item in player.items: #iterate over items in inventory
				c = items[item] #string to class without using eval
				print(str(i) + ") Use 1 x " + c.name + " (Qty: " + player.items[item] + ")")
				localitems.append(item)
				i=i+1
		else:
			print("Inventory: (empty)\n")
		print(str(i) + ") Back to fight")
		selection = input("> ")
		for x in range(1, i): #create the actual options - iterating over the amount of items in inventory
			if selection == str(x): #if the selected item is item being iterated right now
				usage = use(localitems[x-1]) #use selected item
				if usage == 1:
					clear()
					mainbattle() #back to fight
				else:
					clear()
					print(items[localitems[x-1]].failed + " (Press enter to go back to fight)")
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


	def enemydie():
		global player, enemy
		clear()
		eexp = str(int(enemy.tothp) * 2)
		ebp = str((int(player.curhp) + int(enemy.level)) + 2)
		player.exp = str(int(player.exp) + int(eexp))
		player.bp = str(int(player.bp) + int(ebp))
		player.curhp = player.tothp
		print("Congratulations!\n" + player.name + " won the fight, and " + enemy.name + " died!\n")
		print("You earned " + blue(eexp + " exp ") + "and " + yellow(ebp + " gold!"))

		loot()

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

def loot():
	global player, enemy
	looted = []
	for x in range(1, int(enemy.maxloot) + 1):
		lootchance = random.random()
		potentialloot = random.sample(list(enemy.loot), 1)[0]
		if(lootchance <= float(enemy.loot[potentialloot])):
			looted.append(potentialloot)
			c = items[potentialloot]
			if c.shortname in player.items: #if item exists in inventory
				player.items[c.shortname] = str(int(player.items[c.shortname]) + 1) #add to the quantity
			else: #if it does not exist in inventory
				player.items[c.shortname] = '1' #create it
	if(len(looted) != 0):
		print("\n" + yellow(bold("You found loot!")))
		print("You found:")
		for x in range(0, len(looted)):
			itm = items[looted[x]]
			print("1 x " + bold(itm.name) + ": " + itm.desc)
		print(" ")

def playerdie():
	global player
	clear()
	player.lives = str(int(player.lives) - 1)
	player.curhp = player.tothp
	if int(player.lives) == int(0):
		print("You took a huge amount of beatings, and therefore you have perished. It is indeed a sad day.")
		input("> ")
		player = 0
		initiate()
	else:	
		print(enemy.name + " won the fight.")
		print(player.name + " fainted! You can only faint " + player.lives + " more times. (Press enter to continue)")
		input("> ")
		mg()
#fighting gameloops end