if("compile" in sys.argv):
	with open('rrpg.py', 'r') as file:
	    data = file.readlines()
	i = 0
	found = 0
	for line in data:
		if "exec(open(" in line and "compile" not in line:
			path = line[len('exec(open("'):-(len('").read()'))-2]
			data[i] = open(path).read()
		if "exec(open(" in line and "compile" in line:
			data[i] = " "
		i = i + 1
	with open('rrpgp.py', 'w') as file:
	    file.writelines( data )
	print("Compiled to rrpgp.py!")
	sys.exit(0)