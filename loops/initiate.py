def initiate():
	clear()

	print(
"""Welcome to RopasciRPG

You're playing "%s".

Please select an option.""" % (gameloaded))

	if gameloaded == None:
		print(bold("No game is loaded. The engine cannot function without a loaded game.\n"))

	helper_printmenu('initiate')
	helper_checkmenu('initiate', input("> "), 'initiate')