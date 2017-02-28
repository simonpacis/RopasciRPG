#declarations start
player, hp, fleer, majfleer, majhp, mindetector, majdetector, constdetector, rock, paper, scissors, boulder, tinfoil, knife, anvil, duct, sword, enemy, playerselect, playerweapon, enemyweapon = (0,)*21

levelreqs = {"2":"25","3":"50","4":"9999"}
apothstock = ["hp", "majhp", "fleer", "majfleer", "mindetector", "majdetector"]

smithr = ["boulder", "anvil"]
smithp = ["tinfoil", "duct"]
smiths = ["knife", "sword"]
weaponcategories = {"r": "Rock", "p": "Paper", "s": "Scissors"}
rtiers = ["rock", "boulder", "anvil"] #remember- index based
ptiers = ["paper", "tinfoil", "duct"] #remember- index based
stiers = ["scissors", "knife", "sword"] #remember- index based
weapontypes = ["r","p","s"] #so 1,2 and 3 correspond to the different weapon types
locations = {"town":"Town Center","oot":"Out of Town","apoth":"Ole Apothecary","smith": "Ye Smithe o'er All", "merchant": "Travelling Merchant"} #for def: locations
loadedmods = []
#declarations end