#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

#import start
import sys
import os
import random
import pathlib
import pickle
#import end

if("compile" in sys.argv):
	with open('rrpg.py', 'r') as file:
	    data = file.readlines()
	i = 0
	found = 0
	for line in data:
		if "exec(open(" in line and found > 2:
			path = line[len('exec(open("'):-(len('").read()'))-2]
			data[i] = open(path).read()
		elif "exec(open(" in line:
			found = found + 1
		i = i + 1
	with open('rrpgp.py', 'w') as file:
	    file.writelines( data )
	print("Compiled to rrpgp.py!")
	sys.exit(0)

exec(open("classes.py").read())

exec(open("declarations.py").read())

exec(open("functions.py").read())

#entities

exec(open("entities/enemies.py").read())

exec(open("entities/items.py").read())

exec(open("entities/weapons.py").read())

exec(open("entities/itemeffects.py").read())

#entities end

#gameloops start
exec(open("loops/initiate.py").read())

exec(open("loops/main.py").read())

exec(open("loops/fighting.py").read())

exec(open("loops/general.py").read())

exec(open("loops/newgame.py").read())

exec(open("menu/instructions.py").read())

exec(open("menu/about.py").read())

exec(open("menu/saveload.py").read())

exec(open("menu/exit.py").read())

#gameloops end

#run it all
if __name__ == '__main__':
	initiate()