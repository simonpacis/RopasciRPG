def helper_createmenu(menu_name):
	menuorders[menu_name] = []
	menus[menu_name] = {}

def helper_addmenuitem(menu_name, display_name, short_name, function_name, add_after="last", add_before="none", function_params = []):
	global menus, menuorders
	menus[menu_name][short_name] = {'display_name': display_name, 'function_name': function_name, 'function_params': function_params}

	if add_before == "none":
		if add_after == "last":
			menuorders[menu_name].append(short_name)
		elif add_after != "last":
			menuorders[menu_name].insert(int(add_after), short_name)
	elif add_before != "none":
		if add_before == "last":
			menuorders[menu_name].insert((len(menuorders[menu_name])-1), short_name)
		elif add_before != "last":
			menuorders[menu_name].insert((int(add_before)-2), short_name)

def helper_printmenu(menu_name):
	i = 1
	for menuitem in menuorders[menu_name]:
		print(str(i) + ") "+ menus[menu_name][menuitem]['display_name'])
		i = i + 1

def helper_checkmenu(menu_name, checker, option_not_found_function):
	try:
		if menuorders[menu_name][int(checker)-1] in menuorders[menu_name]:
			if len(menus[menu_name][menuorders[menu_name][int(checker)-1]]['function_params']) == 0:
				exec(menus[menu_name][menuorders[menu_name][int(checker)-1]]['function_name'] + "()")
			else:
				i = 0
				paramstring = ""
				for param in menus[menu_name][menuorders[menu_name][int(checker)-1]]['function_params']:
					try:
						float(param)
					except ValueError:
						param = "\"" + param + "\""
					if i == 0:
						paramstring += param
					else:
						paramstring += ", " + param
				exec(menus[menu_name][menuorders[menu_name][int(checker)-1]]['function_name'] + "(" + paramstring + ")")

	except ValueError:
		exec(option_not_found_function + "()")