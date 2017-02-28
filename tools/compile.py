if("compile" in sys.argv):
	with open('rrpg.py', 'r') as file:
	    data = file.readlines()
	i = 0
	for line in data:
		if "exec(open(" in line and "compile" not in line:
			path = line[len('exec(open("'):-(len('").read()'))-2]
			data[i] = open(path).read()
		if "exec(open(" in line and "compile" in line:
			data[i] = " "
		i = i + 1
	with open('rrpgp.py', 'w') as file:
	    file.writelines( data )
	print("Compiled to rrpgp.py!\nPlease note that mods are not compiled to rrpgp, but that mods placed in a mods folder will still be loaded in rrpgp.")
	sys.exit(0)