#declarations start
player, hp, fleer, majhp, mindetector, majdetector, rock, paper, scissors, boulder, tinfoil, knife, anvil, duct, sword, enemy, playerselect, playerweapon, enemyweapon = (0,)*19
#mob declarations start
thug, bandit, eblob, chorse, wolf, magician, madp, lordling = (0,)*8 #level 1 mobs
bleader, mmagician, cblob, mlumberjack, osailor, gnometroll, eknight, slayerman, deserter, lord = (0,)*10 #level 2 mobs
wyvern, lynx, kblob, gmad, cminelo, hbandit, cunicorn, kgnometroll, enlord, mcriminal, ebear, king = (0,)*12 #level 3 mobs
#mob declarations end
l1mobs = ["thug", "bandit", "eblob", "chorse", "wolf", "magician", "madp", "lordling"]
l2mobs = ["bleader", "mmagician", "cblob", "mlumberjack", "osailor", "gnometroll", "eknight", "slayerman", "deserter", "lord"]
l3mobs = ["wyvern", "lynx", "kblob", "gmad", "cminelo", "hbandit", "cunicorn", "kgnometroll", "enlord", "mcriminal", "ebear", "king"]
levelreqs = {"2":"25","3":"50","4":"9999"}
apothstock = ["hp", "majhp", "fleer", "mindetector", "majdetector"]
smithr = ["boulder", "anvil"]
smithp = ["tinfoil", "duct"]
smiths = ["knife", "sword"]
weaponcategories = {"r": "Rock", "p": "Paper", "s": "Scissors"}
rtiers = ["rock", "boulder", "anvil"] #remember- index based
ptiers = ["paper", "tinfoil", "duct"] #remember- index based
stiers = ["scissors", "knife", "sword"] #remember- index based
weapontypes = ["r","p","s"] #so 1,2 and 3 correspond to the different weapon types
locations = {"town":"Town Center","oot":"Out of Town","apoth":"Ole Apothecary","smith": "Ye Smithe o'er All"} #for def: locations
#declarations end