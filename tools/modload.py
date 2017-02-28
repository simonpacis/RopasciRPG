dirs = []
if os.path.isdir("mods"):
	for item in os.listdir("mods"):
	    if os.path.isdir(os.path.join("mods", item)):
	        dirs.append(item)

	for dir in dirs:
		if not os.path.isfile("mods/"+dir+"/disabled"):
			if os.path.isfile("mods/"+dir+"/mod.json"):
				loadedmods.append(dir)
				for file in glob.glob("mods/"+dir+"/*.py"):
					exec(open(file).read())
			else:
				print("\nMod \"" + dir + "\" was not loaded due to missing mod.json file.")
				input("> (Press enter to continue)")