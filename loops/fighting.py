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
					print(str_to_class(items[x-1]).failed + " (Press enter to go back to fight)")
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
#fighting gameloops end