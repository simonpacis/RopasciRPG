#declarations start
menus = {}
menuorders = {}
player, rock, paper, scissors, boulder, tinfoil, knife, anvil, duct, sword, enemy, playerselect, playerweapon, enemyweapon = (0,)*14


gameloaded = "Classic"
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


helper_createmenu('initiate')
helper_addmenuitem('initiate', 'New game','ng1','ng1')
helper_addmenuitem('initiate', 'Load game', 'load', 'load')
helper_addmenuitem('initiate', 'Instructions','instructions','instructions')
helper_addmenuitem('initiate', 'About','about','about')
helper_addmenuitem('initiate', 'Mod info','modinfo','modinfo')
helper_addmenuitem('initiate', 'Exit game', 'gameexit', 'gameexit')

helper_createmenu('maingame')
helper_addmenuitem('maingame', 'Look for trouble','initfight','initfight')
helper_addmenuitem('maingame', 'Go to "' + locations['apoth'] + '"', 'apoth', 'apoth')
helper_addmenuitem('maingame', 'Go to "' + locations['smith'] + '"', 'smith', 'smith')
helper_addmenuitem('maingame', 'Go to "' + locations['merchant'] + '"', 'merchant', 'merchant')
helper_addmenuitem('maingame', 'Save game','save','save')
helper_addmenuitem('maingame', 'Exit to main menu', 'exitsure', 'exitsure')
#declarations end