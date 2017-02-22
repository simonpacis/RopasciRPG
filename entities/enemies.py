def createenemies(number=4):
	#argument order name, shortname, taunts, pref, weapons, tothp, curhp, level
	global thug, bandit, eblob, chorse, wolf, magician, madp, lordling, bleader, mmagician, cblob, mlumberjack, osailor, gnometroll, eknight, slayerman, deserter, lord, wyvern, lynx, klob, gmad, cminelo, hbandit, cunicorn, kgnometroll, enlord, mcriminal, ebear, king
	#level 1 enemies
	thug = Enemy("Thug", "thug", ["Eh, what are you up to?", "Come over here, mate.", "What have we here?"], {"r":1.1,"p":0.95,"s":0.95})
	bandit = Enemy("Bandit", "bandit", ["Let me rob you.", "You're too far from home!", "Hehehe."], {"r":1.1,"p":0.95,"s":0.95})
	eblob = Enemy("Evil Blob", "eblob", ["Bloob."])
	chorse = Enemy("Corrupted Horse", "chorse", ["Neeeigh! (Oxford Dictionary says this is the sound a horse makes)"])
	wolf = Enemy("Wolf", "wolf", ["Grrrr!"])
	magician = Enemy("Magician", "magician", ["I've got this new spell. It's called SCISSORS!", "Hullo, hullo. Dis is ma' forest.", "It shall be delightful to slaughter you."], {"r":0.9,"p":1,"s":1.1})
	madp = Enemy("Mad Peasant", "madp", ["Where am I? Who are you? DIE!", "I am so angry with my wife. You shall suffer from it.", "Watch where you stand! This is my soil!"])
	lordling = Enemy("Lordling", "lordling", ["How darest thou step feet on my property? Watch this piece of silver paper eradicate you.", "Peasant! Obey me, and die to this piece of magical silver paper.", "Silver paper is what saves me. As you shall well discover."], {"r":1,"p":1,"s":1}, {"r": "rock", "p": "tinfoil", "s": "scissors"})
	
	#level 2 enemies
	bleader = Enemy("Bandit Leader", "bleader", ["You might seem so big and strong and cool. But, watch me!", "Welcome to the dark part of the lands.", "Heeeheeeheee! Exterminate!"], {"r":1.1,"p":0.95,"s":0.95}, {"r": "boulder", "p": "paper", "s": "scissors"}, "5", "5", "2")
	mmagician = Enemy("Master Magician", "mmagician", ["I've got this well practiced magical spell. It's called KNIFE!", "Feel my eternal wrath.", "I am the Master of the Lesser Magicians."], {"r":0.9,"p":1,"s":1.1}, {"r": "rock", "p": "paper", "s": "knife"}, "5", "5", "2")
	cblob = Enemy("Corrupted Blob", "cblob", ["Blooob."], {"r":1,"p":1,"s":1}, {"r": "rock", "p": "tinfoil", "s": "scissors"}, "5", "5", "2")
	mlumberjack = Enemy("Maniac Lumberjack", "mlumberjack", ["Yiaargh! I will chop yer down like an oak!!", "Chop, chop, chop. All day long. Now for some smashing.", "I had a wife once. Hehehe."], {"r":0.95,"p":0.95,"s":1.1}, {"r": "rock", "p": "paper", "s": "knife"}, "5", "5", "2")
	osailor = Enemy("Old Sailor", "osailor", ["I have sailed all the seven seas. Now, I want to sail in your blood.", "Once I was a sailor. I lost everything I owned, because one of these petty lords came and took her while I was away. To this day, anger and rage is all I know.", "Hoist the sails!"], {"r":0.9,"p":1.1,"s":1}, {"r": "rock", "p": "tinfoil", "s": "scissors"}, "5", "5", "2")
	gnometroll = Enemy("Gnometroll", "gnometroll", ["Yeargheeeaaa! Huxklaen ma, da hexin pelof!"], {"r":1,"p":1,"s":1}, {"r": "boulder", "p": "paper", "s": "scissors"}, "5", "5", "2")
	eknight = Enemy("Evil Knight", "eknight", ["Valor and honour. These are the words by which I live. At least when the princess is nearby.", "I serve the king, and the darkness of my rotten heart.", "What are you doing so far from any civilization? Now die."], {"r":1.1,"p":0.95,"s":0.95}, {"r": "boulder", "p": "paper", "s": "scissors"}, "5", "5", "2")
	slayerman = Enemy("Slayerman", "slayerman", ["Mhe. Heh. I.. Well, yes.. I am the Slayerman. Hah. Haha! Heh.", "Heeeellooo, heelloooo. Who.. Who is this dawdling person I.. I meet? HAH! Hehe. I am the Slayerman.", "I.. I am the Slayerman. And I want to play a game."], {"r":1,"p":1.1,"s":0.9}, {"r": "rock", "p": "tinfoil", "s": "scissors"}, "5", "5", "2")
	deserter = Enemy("Deserter", "deserter", ["I've got half the kingdom chasing me down. I am not afraid of a mere peasant such as you.", "Don't blink, or you'll die.", "STOP! And fight."], {"r":1,"p":1,"s":1}, {"r": "boulder", "p": "paper", "s": "scissors"}, "5", "5", "2")
	lord = Enemy("Lord", "lord", ["I am the Lord of Meagerlands, and you have most definitely trespassed.", "For as I, the Lord, has decreed, so shall you be slain.", "What a little, powerless person you are. Take up your arms!"], {"r":1,"p":1,"s":1}, {"r": "rock", "p": "paper", "s": "sword"}, "5", "5", "2")

	#level 3 enemies
	wyvern = Enemy("Wyvern", "wyvern", ["Raaaaarrrgh!", "Reearrgh!"], {"r":1,"p":1,"s":1}, {"r": "anvil", "p": "paper", "s": "scissors"}, "7", "7", "3")
	lynx = Enemy("Lynx", "lynx", ["Grrrr!"], {"r":1,"p":1,"s":1}, {"r": "rock", "p": "duct", "s": "scissors"}, "7", "7", "3")
	klob = Enemy("King Blob", "klob", ["Bloooob!"], {"r":1,"p":1,"s":1}, {"r": "rock", "p": "paper", "s": "sword"}, "7", "7", "3")
	gmad = Enemy("General Mad", "gmad", ["I was once a general. I lost it all to the test of time. Too bad, so sad.", "Mad. Mad. Who's mad? Me mad? You mad. Die, you cow.", "I just wanted to ride the horse."], {"r":1.1,"p":0.9,"s":1}, {"r": "anvil", "p": "paper", "s": "scissors"}, "7", "7", "3")
	cminelo = Enemy("Captain Minelo", "cminelo", ["Hi there! Have you seen my friend, the old sailor? I've been looking everywhere for him, btu he is simply gone. Oh my, oh my. Well, you'll do as good as any.", "I come from the ocean. And as the ocean, I show no mercy.", "Merciful is the one who is merciful. I am not that one."], {"r":1,"p":1.1,"s":0.9}, {"r": "rock", "p": "paper", "s": "sword"}, "7", "7", "3")
	hbandit = Enemy("Horse Bandit", "hbandit", ["What have we here? A frisk one. More likely a dead one.", "Hello. Goodbye.", "I've been watching you for days, slaying all these people. Now you're up."], {"r":1,"p":1,"s":1}, {"r": "rock", "p": "duct", "s": "scissors"}, "7", "7", "3")
	cunicorn = Enemy("Corrupted Unicorn", "cunicorn", ["Neeeeeigh!"], {"r":1,"p":1,"s":1}, {"r": "rock", "p": "paper", "s": "sword"}, "7", "7", "3")
	kgnometroll = Enemy("King Gnometroll", "kgnometroll", ["Se mulos, mulos mak. Der teflaren digmo!"], {"r":1,"p":1,"s":1}, {"r": "anvil", "p": "paper", "s": "scissors"}, "7", "7", "3")
	enlord = Enemy("Envious Lord", "enlord", ["Oh, how I wish I could be free from these chains. These shackles burden me.", "All this responsibility is most definitely tiring.", "I am a sleepwalker, and oh how I wish I was not!"], {"r":0.95,"p":1,"s":0.95}, {"r": "rock", "p": "duct", "s": "scissors"}, "7", "7", "3")
	mcriminal = Enemy("Mad-eyed Criminal", "mcriminal", ["I robbed a wagon full of jewelry. Which is why I wear this pretty necklace.", "I killed an entire family, and afterwards I slept in their beds. Heeh.", "I stabbed a lord in the heart. He was too lordly for me."], {"r":1,"p":1,"s":1}, {"r": "rock", "p": "paper", "s": "sword"}, "7", "7", "3")
	ebear = Enemy("Evil Bear", "ebear", ["Raargh!"], {"r":1,"p":1,"s":1}, {"r": "anvil", "p": "paper", "s": "scissors"}, "7", "7", "3")
	king = Enemy("King of Ropasci", "king", ["Halt, company! Who is this traveler? He seems to be challenging to me. Off you pop, little one.", "Halt, company! It seems we've hit a bump in the road, and the bump shall now suffer.", "I am the great King of Ropasci. How darest thou look at me?"], {"r":1,"p":1,"s":1}, {"r": "anvil", "p": "duct", "s": "sword"}, "7", "7", "3")
