def applyeffect(item):
	global player
	orgitem = item
	""" applyeffect can return three different things. return(0) means the effect of the item has failed, and
	the item should not be removed from inventory; as in a health potion that can not be used because the
	health is full. return(1) means the item has been succesfully used. return(2) means that the item has
	been used, but the failed message should still be displayed. Basically this means that the item will
	be removed from inventory (subtract 1 from quantity), but the fail message will still be displayed
	to the player; as in a revelation potion that has been used, but you failed to detect the enemy's
	weapon preference."""

	item = str_to_class(item)

	"""
		Heal effect heals player.
	"""
	if(item.effect == "heal"):
		if (int(player.curhp)) <= (int(player.tothp) - int(item.value)):
			player.curhp = str(int(player.curhp) + int(item.value))
			return(1)
		elif (int(player.curhp)) < int(player.tothp):
			player.curhp = str(int(player.tothp))
			return(1)
		else:
			return(0)

	"""
		Detect effect detects enemy weapon preferences.
	"""
	if(item.effect == "detect"):
		clear()
		types = weaponcategories
		prefs = enemy.pref
		amntofone = 0 #amount of preferences at 1; no preference in given category

		for key, value in prefs.items():
			if value == 1:
				amntofone = amntofone + 1

		prefmax = max(prefs.keys(), key=(lambda key: prefs[key]))
		prefmin = min(prefs.keys(), key=(lambda key: prefs[key]))
		detected = random.random()

		if detected > (1-(0.60)) or item.value == "1": #60% chance to detect unless item.value is 1
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
			return(2)

	if(item.effect == "flee"):
		clear()
		escape = random.random()
		if(float(item.value) <= 1):
			if escape >= (1-float(item.value)):
				print("Got away safely. (Press enter to continue)")
				# We have to rewrite the remove item from inventory code, as we're leaving the fight without returning
				if int(player.items[orgitem]) == 1:
					del player.items[orgitem]
				else:
					player.items[orgitem] = str(int(player.items[orgitem]) - 1)
				input("> ")
				mg()
			else:
				return(2)
		else:
			player.curhp = str(int(player.curhp) - int(4))
			if(int(player.curhp) <= 0):
				playerdie()
			else:
				print("Got away safely. (Press enter to continue)")
				# We have to rewrite the remove item from inventory code, as we're leaving the fight without returning
				if int(player.items[orgitem]) == 1:
					del player.items[orgitem]
				else:
					player.items[orgitem] = str(int(player.items[orgitem]) - 1)
				input("> ")
				mg()
