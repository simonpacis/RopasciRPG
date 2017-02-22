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