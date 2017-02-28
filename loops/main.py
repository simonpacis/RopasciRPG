#maingame gameloops start
def mg():
	clear()
	location("town")
	print(underline(player.name) + red("\tHP: " + player.curhp + "/" + player.tothp) + "\t\tLives: " + player.lives + "\nLvl: " + player.level + blue("\tExp: " + player.exp + "/" + lreq()) + yellow("\tGold: " + player.bp) + "\n" + player.race + "\t" + player.gender + "\n") #print player information
	if player.items: #if inventory is not empty
		print(bold("Inventory:"), end=" ")
		for item in player.items: #iterate over items in inventory
			c = items[item] #string to class without using eval
			print(c.name + ": " + player.items[item] + "\t", end=" ") #print item and tab it at the end + no newline
	else:
		print(bold("Inventory: ") + "(empty)", end=" ")

	print(bold("\n\nCurrent weapons:") + "\nRock: " + str_to_class(player.weapons["r"]).name + " (" + str_to_class(player.weapons["r"]).tier + ")\nPaper: " + str_to_class(player.weapons["p"]).name + " (" + str_to_class(player.weapons["p"]).tier + ")\nScissors: " + str_to_class(player.weapons["s"]).name + " (" + str_to_class(player.weapons["s"]).tier + ")\n")

	print(
	bold("Please select an option")
	+ """
1) Look for trouble
2) Go to \"""" + locations['apoth'] + """\"
3) Go to \"""" + locations['smith'] + """\"
4) Go to \"""" + locations['merchant'] + """\"
5) Save game
6) Exit to main menu""")

	selection = input("> ")

	if selection == "1":
		initfight()
	elif selection == "2":
		apoth()
	elif selection == "3":
		smith()
	elif selection == "4":
		merchant()
	elif selection == "5":
		save()
	elif selection == "6":
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