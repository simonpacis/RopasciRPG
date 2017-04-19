# RopasciRPG
### rock-paper-scissors meet role-playing!

RopasciRPG is a Python 3 console game which mixes the old and famous game rock-paper-scissors with RPG elements and mechanics.

### RopasciRPG features:
* Levels and experience points
* Currency and shops
* 3 weapon tiers
* 30 personal and unique mobs with slight weapon preferences and unique taunts!
* Saving and loading
* 4 different player races to choose from
* 2 different player genders to choose from
* A kingdom with a king, lordlings and lords

## Instructions?
* Download Python 3 (*not* Python 2 compatible)
* Launch your Terminal/Command Line.
* Go to the directory in which rrpg.py is located
* Type in `python3 rrpg.py` and play away!

The game contains playing instructions.

**Word of warning**: Remember to save often, opponents can beat you out of the blue. Luckily, the difficulty has been lowered since the initial commit.

## Portability?
As of recently the RopasciRPG source code has been exploded into numerous files, instead of being the single file it used to be. But don't fret! You can run `python3 rrpg.py compile` to create the file `rrpgp.py`, which is the entire game compiled to one single file.

### Ideas (/wishlist/maybe roadmap)
If you want to develop a bit on this crazy game of mine, here's some ideas as to what you could create.
* Random enemy HP, so that you don't always bump into enemies that are as strong as you are.
* Boss-fight (I've got a "boss" in each of the levels as of now, but not a real boss-fight. Just a fight against an overpowered NPC, really)
* More levels and weapon tiers
* More items
* Quests!
* Regions that you can explore and region-specific NPC - remember to save region information in savegames as well, then.
* Better NPC taunts (mine are strange and remotely funny at best)
* Sounds! (I don't know how you would achieve this, but it would be great. Perhaps creating a GUI that is a pseudo-terminal? Would allow for arrow-controls too)
* NPC's that you can talk and interact with
* More towns and shops
* Different weapon types than the three default

## Explanation of some choices
Looking through the code you'll notice a lot of things rendering the game unfit for any kind of PEP-8 valdiation, and a huge amount of examples of bad practice, malpractice and generally bad, non-DRY code. Keep in mind that I initially created this game as my second ever Python project, and everything else has been piled on top of a bad initial codebase.

`exec(open().read())` was introduced to produce code that is not all contained in a single file. It is bad practice, and `import` should be used instead, but the entire codebase would have to be refactored to allow for this practice instead.

Tons of use of globals, definitions and redefinitions. Tons of useless code and so on and so forth. As mentioned, bear in mind my state as developer when it was originally written.

## License
Released under the "DWYWWIJDSI" (Do whatever you want with it, just don't sell it) license.
