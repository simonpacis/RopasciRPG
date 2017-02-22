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