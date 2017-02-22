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
				print("You have upgraded your weapon in weapon type \"" + weaponcategories[weapontypes[x-1]] + "\" to \"" + str_to_class(player.weapons[weapontypes[x-1]]).name + "\" at the price of " + str_to_class(player.weapons[weapontypes[x-1]]).cost + " gold.\n1) Back to Ye Smithe o'er All\n2) Back to town")
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