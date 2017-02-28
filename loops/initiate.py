def initiate():
	clear()

	print(
"""Welcome to RopasciRPG

Please select an option.
1) New game
2) Load game
3) Instructions
4) About
5) Mod info
6) Exit game""")

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
		modinfo()
	elif menuselection == "6":
		gameexit()
	else:
		initiate()