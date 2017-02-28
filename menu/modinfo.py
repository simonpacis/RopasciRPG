def modinfo():
	clear()
	print("The mods currently loaded are:")
	if len(loadedmods) != 0:
		for mod in loadedmods:
			print("\n")
			with open('mods/'+mod+'/mod.json') as data_file:    
			    data = json.load(data_file)
			    print(bold("Name: ") +data['name'])
			    del data['name']
			    for entity, value in data.items():
			    	print(bold(entity.title()) + ": " + value)
	else:
		print("\nNo mods loaded.")
	input("\n> (Press enter to go back)")
	initiate()