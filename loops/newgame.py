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