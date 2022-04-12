#Alpha 2.1.0 Complete (Everything except rules and commands)  (updated security stuff)

from collections import Counter

import Spellchecker
from Embeds import *

global memes_enabled
memes_enabled = False

derpfile = Spellchecker.words(open('commandlist.txt').read())
new_file = []
for e in range(len(derpfile)):
    new_file.append(derpfile[e].replace('_', ' '))

WORDS = list(Counter(set(new_file)))

import discord
hibernation = []


client = discord.Client()

#---------------------------------------------------------------------------------------------

async def CheckCommands(message, channel):
    await client.change_presence(activity=discord.Game(name='working...'), status=discord.Status('idle'))
    if message.content.upper().startswith('!CREATUR'):
        await channel.send(content="```diff\n- Creatures and Creature Rules:\n!surface - list of surface creatures and surface rules.\n!middle - list of middle creatures and rules.\n!deep - list of deep creatures and rules.\n!mariana trench - you know the drill...\n- Make sure you know the strength of the creatures of the zone you are going into before you go down a level. The creatures get more powerful, and by gratuitous amounts each time you go down!```")

    elif message.content.upper().startswith('!SURFACE'):
        await channel.send(
            content=
            "```diff\n- Surface Creatures and Rules:\n1) The instant you enter the surface, your oxygen fills up to max and remains that way until you leave.\n2) There are no surprise attacks at the surface.\n3) You may farm for coral at the surface. You have a 50% chance of receiving 2 coral.\n4) You can access the middle from the surface.\n5) All surface creatures can be caught by the player.\n\n- Creatures will be listed in the following form: (name,HP+(shield if any),atk), for more information on a creature such as its drops, abilities, and catchability (for pet), type: .(name of creature) remember to type in spaces when necessary\n(ariel leviathan,400,10)\n(saltwater croc,100+100shield,100)\n(tiger fish,100,30)\n(gar,100,40)\n(turtle,80+90shield,10)\n(piranha,70,10)\n(hatchet fish,70,30)\n(octofish,70,30)\n(big trout,60,20)\n(water bug,50,10)\n(tummy tetra,50,30)\n(trout,50,10)```"
        )

    elif message.content.upper().startswith('!MIDDLE'):
        await channel.send(
            content=
            "```diff\n- Middle Creatures and Rules:\n1) You will lose 1 oxygen at the beginning of your turn in the middle.\n2) You have a 1/6 chance of surprise attack in the middle, this will be calculated immediately.\n3) You may farm for wood and coral in the middle, you have a 1/2 chance of getting 1 wood, and a 1/2 chance of getting 2 coral.\n4) You can access the surface and the deep from the middle.\n5) You can also mine for iron and steel in the middle, which you need a shovel for. You have a 1/2 chance of getting attacked by the stonefish while mining, and you have a 1/2 chance of getting 1 iron, and a 1/4 chance of getting steel.\n\n- Look at surface creatures and rules, so you know how the following creature list is formatted.\n(blue whale,600,20)\n(great white shark,300,200)\n(albino tiger oscar,250,70)\n(giant lionfish,250,60)\n(marlin,150,100)\n(mushroom fish,150,50)\n(tiger oscar,150,30)\n(barracuda,100,30)\n(shovelnose guitarfish,100,30)\n(vortex fish,100,20)\n(largemouth bass,80,50)\n(tuna,70,20)\n(moray eel,50,50)\n(electric eel,50,20)\n(pufferfish,50,35)\n(great diving minnow,50,10)\n(reefback,undefined,0)\n(stonefish,50,20)```"
        )

    elif message.content.upper().startswith('!DEEP'):
        await channel.send(
            content=
            "```diff\n- Deep Creatures and Rules:\n1.) You will lose one oxygen at the beginning of your turn in the deep.\n2.) You have a 1/3 chance of surprise attack in the deep, this will be calculated immediately.\n3.) You can access the middle and the mariana trench from the deep.\n4.) You can mine for titanium in the deep. You have a 1/4 chance of getting 1 titanium (which you need a shovel for), and 1/2 chance of getting attack by the warp fish while doing so.\n\n- Look at surface creatures and rules, so you know how the following creature list is formatted.\n(grave whale,800,200)\n(phantom leviathan,600,200)\n(necro eel,500,200)\n(giant squid,500,150)\n(sand leviathan,400,200)\n(electric ray,300,200)\n(warp fish,300,210)\n(wobbegong,300,200)\n(trench reaper,200,30)\n(anglerfish,50,35)```"
        )

    elif message.content.upper().startswith('!MARI'):
        await channel.send(
            content=
            "```diff\n- Mariana Trench Creatures and Rules:\n1.) You will lose one oxygen at the beginning of your turn in the trench.\n2.) You have a 1/2 chance of surprise attack in the trench, this will be calculated immediately.\n3.) You can access the deep from the mariana trench.\n\n- Look at surface creatures and rules, so you know how the following creature list is formatted.\n(dark arowana,6000,300)\n(Cthulhu the god,4000,600)\n(bull clam,1500+3000shield,1000)\n(electric leviathan,4900,300)\n(redtail catfish,4800,600)\n(cachalot,4000,500)\n(microbacteria swarm,3000,450)\n(ghost knife fish,2000,200)\n(frilled shark,2000,500)\n(armored ghost shrimp,1+1shield,1000)```"
        )

    elif message.content.upper().startswith('!RESOURCE'):
        await channel.send(
            content=
            "```diff\n-Resources:\nTo get more information about a given resource, type in .(name of resource).\Immediately following the resource name will be location in which to find it.```\n```css\niron - middle\nsteel - middle\nmarlin sword - middle\ncoral - surface,middle\nwhale cock - middle\ntitanium - deep\nslime coat - middle\nwood - middle\nmeat - anywhere\nblubber - middle\nsuit - surface\nwatt - anywhere\np corpse - middle\nplatinum elixir - middle\nw corpse - deep\nsky blade - surface\nscales - surface\ncorpse - surface\nghost suit - deep\nshovelnose - middle\nnecro blade - deep\noxygen - surface\npearl - mariana trench```"
        )

    elif message.content.upper().startswith('!CRAFTITEMS') or message.content.upper().startswith('!CRAFT ITEMS'):
        await channel.send(
            content=
            "```diff\n-List of Craftable Items:\nTo get more information about a given craftable item, type in .(name of item).\n```\n```css\nblubber base\nbig shovel\nbio wheel\nlamp\nfishing net\nplatinum juice\nshrine of Cthulhu\nshovel\noxygen tank\nbio reactor\ngenerator\nrepair kit\nsea hawk submarine\nstingray submarine\ntriclops submarine\ntitanium plate\ntitanium laser\nnanocell cartridge\nnecro saber\nrecovered necro saber\ninfinity shield\nw armor\nplatinum chestplate\nplatinum helmet\nplatinum greaves\nplatinum boots\nshifting armor\nsky sword\nshotgun\nhatchet\nvegan battle axe\nclassical freeze gun\nnanocell freeze beam\nquantum orbital freeze ray\nflaming platinum sword of ultra death```"
        )

    elif message.content.upper().startswith('!WEAPON'):
        await channel.send(
            content=
            "```diff\n- List of Weapons, submarines, and armors:\nList will display HP or ATK buff, but for special abilities, type .(name of weapon)\nnecro saber +50 ATK\nrecovered necro saber +50 ATK\nInfinity shield +10 shield\nw. armor +50 HP\nplatinum chestplate +75 HP\nplatinum greaves +25 HP\nplatinum helmet +50 HP\nplatinum boots +50 HP\nshifting armor +70 HP\nsky sword +50 ATK\nshotgun +30 ATK\nhatchet +20 ATK\nvegan battle axe +60 ATK\nmarlin sword +20 ATK\nclassical freeze gun +40 ATK\nnanocell freeze beam +60 ATK\nquantum orbital freeze ray + 150 ATK\nflaming platinum sword of ultra death +50 ATK\nsea hawk submarine 200 HP, 100 Shield, 100 ATK\nstingray submarine 300 HP, 200 Shield, 200 ATK\ntriclops submarine 600 HP, 400 Shield, 400 ATK\ntitanium plate +50 HP to submarine\ntitanium laser +50 ATK to submarine```\n```css\nWeapon, Submarine, and Armor Rules:\n1) Weapons and Armor add a specified amount of damage or HP to the PLAYER'S ATK/HP. (Submarines, titanium plates, and titanium lasers, function differently.)/n2) If you have more than one of a weapon, the damage and the stats of those weapons or armor do not exist. (No stacking weapons or armor of the same type).\n3.) You can only have ONE submarine, at a time, if you craft a new submarine, your old one is instantly destroyed.\n4) Armor adds to your base HP and is permanent until you die or give the armor away.\nFor sub rules type .submarine rules, or .sub rules or .sub or .subs!```"
        )

    elif message.content.upper().startswith('!SUB'):
        await channel.send(
            content=
            "```diff\n- Sub rules:\nSubs are complicated in how the work so this entire section is about rules about subs.  (Note for simplicity, whenever you see sub, it means submarine, as we will be abbreviating submarine to sub.\n1) You may get in or out of your submarine once per battle turn and once per playing turn.\n2) Titanium Lasers add +50 ATK to the sub's ATK and the Titanium Plates add +50 HP to the sub's HP. (These attachments are for submarines only, and do not add to your players HP or ATK.) Unlike player weapons and armor, titanium plates and lasers are stackable but they have a stack limit. A sea hawk sub can have a total of 10 titanium add-ons attached. A stingray sub can have a total of 20 add-ons in effect, and a triclops can have as many as 40 add-ons in effect. You can choose to distribute these add-ons however you like. You may have 20 titanium plates and 0 lasers on a stingray, or you can have 10 of each.  It doesn't matter.\n2.5) When you craft a titanium add-on is built, it is automatically attached to your submarine, assuming it does not cross the add on limit.\n- YOU CAN DETACH A TITANIUM ADD-ON FROM YOU SUB BY TYPING '!remove plate', or '!remove laser', depending on which one you wish to uninstall.\n3) When in the sub, your own stats do not matter, only the sub’s stats matter, and vice versa when you are not. So lowering your subs HP does not heighten a berserker's attack.  Your normal HP can not go down until your sub is destroyed. Or until you exit the sub. A sub’s shield takes and identified amount of watts to regen. (in stats next to shield is # of watts to regen.)\n4) The subs allow you to access certain levels without taking pressure damage, as long as you are in the sub. The sea hawk can access the deep, middle, and surface. If it enters the Trench it take 20 pressure damage per turn. The other subs can access any level without taking pressure damage.\n5) You can only have ONE sub, at a time, if you craft a new sub, your old one is instantly destroyed.\n6) If you are in your submarine at the beginning of your turn, you oxygen does not do down, but remains stagnant.\n7) Submarines cannot be healed by meat. The only way to heal a sub (not it's shield) is to use a repair kit. Repair kits require a move or battle turn to use, and they heal your sub HP by 50, repair kits can be used an infinite amount of times.```"
        )
    elif message.content.upper().startswith('!RULE'):
        await channel.send(content='```diff\n- Type "!manual" for a easy step-by step explanation of how to play the game.```')
    
    elif message.content.upper().startswith('!MANUAL'):
        await channel.send(content='```diff\n- Manual:\n+1) To learn about starting or entdisering a game, type "!SETUP".\n+2) Once you are in the quene for a game, you must type ".enter (class)" in order to start playing.  To learn about the different classes, type "!CLASSES".\n+3) At this point you should be in the game, once the bot says that it is your turn, you may start you move.  You can only do one of these actions per turn. Some things you may do are:\n    Fight: "!FIGHTING"\n    Change your depth (what level you are on): "!DIVING"\n    Crafting: "!CRAFTING"\n    Gathering resources: "!GATHERING"\n    Regen: "!REGENERATION"\n    Use specifc items: "!USING ITEMS"```')
    
    elif message.content.upper().startswith('!FIGHTING'):
        await channel.send(content='```diff\n- Fighting:\n+To fight on your  turn simply type ".fight" and you will enter into a fight with a random creature from the depth you are at.\n+Each turn there is a 50/50 chance you will hit the enemy and a 50/50 chance the enemy will hit you, based on an imaginary coin flip. When prompted, type ".heads" or ".tails" to call a side on the coin. If you call the side the coin lands on correctly, it is now your battle turn (otherwise the creature hits you and you call again)\n+There are a variety of things you can do on your battleturn. Some of them are\n    - Attack the enemy: Type ".attack"\n    - Flee: Type ".flee" #fill\n    - Regen: Type ".regen" to heal without meat on your battle turn\n    - Drag (diver only): Type "insert command here" to drag an enemy up or down one level\n    - Use an item: Type "!USING ITEMS" to learn about what items can be used in battle, and whether they use your turn, or if you can still move after using them.```')
    
    elif message.content.upper().startswith('!USING ITEMS'):
        await channel.send(content='```diff\n- Using items:\n  - Using items can use your move, or they can be used at any time on your turn, depending on the item. In addition, some items can be used in battle, and some of them use your battle turn. Below will be a list of items, which can be used. Each item will say next to it, how to use it, when it can be used, and if it requires a move.\n  - NOTE: These are only items that can be used with the ".USE" command, and does not include all items. For a list of all items, type "!RESOURCES" for a list of farmable resources (not crafted) or "!CRAFTITEMS" for a list of items that can be crafted\n  - Command: ".use (item) #" (item) represents the name of an item. "#" is optional depending on the item, and specifies the amount of the item you would like to use. For meat enter "auto" instead of a number in order to heal to full using meat. If you do not specify an amount of meat, the bot will assume auto, and heal you to full.\n    +Iron, Steel, Marlin Sword, Coral, Wood,  ```')
    
    #elif message.content.upper().startswith('!SETUP'):
        #await channel.send(content='```css\nGoal: to obtain a pearl, which when used allows you to win the game\nSet up:\n1) Every player chooses a class (type "!classes"). Please note the character abilities have precedence over, and often override basic game rules. Items can also change or create new mechanics.\n2) If you are playing irl (without the discord bot) you will need a coin. Most decisions are decided with a 1/2 chance (coin) or 1/6 (die)\n3) Players will take turns in a sequential matter. The order is governed by the order the players join the game. See "!commands" to know the commands to join a game and choose your class\nCongratulations! Now you know how games start, go back to main rule text, to see some basic and more complicated playing rules.```')
    
    elif message.content.upper().startswith('!SETUP'):
        await channel.send(content='```css\nThere are two ways to start playing a match:\n1) You may create a game in any room that does not already have a game in it.  Type ".game" to see if there is a game in the current channel, and who is in it.\n  How to create a game:\n    Type ".creategame (player)" Use pings to identify who you will invite to your game, seperate pings with spaces.\n    Ex: ".creategame @RyantheKing @not a cat, @Oceanus" (This will create a game and add you and the 3 mentioned people to the quene.\nNOTE: Creating a game adds you to the quene, after creating a game, you must follow option 2 (below)\n2) If you are not in the quene and did not create the game, you must ask someone already in the game to invite you.\n\Congratulations! Now you should be in the quene of a game, to start playing go to the next step of the manual.```')
    
    elif message.content.upper().startswith('!STARTTURN'):
        await channel.send(content='css\nList of things that happen at the beginning of your turn, before you even make a move:\n1) If you died or changed your class on the last turn, you will be at the surface. (You may change your class at any time, which results in you dying instantly and respawning at the surface with no items, and the specified class.)\n2) 1 OX or oxygen is subtracted from you oxygen count.\n3) If you have 0 oxygen, you will receive 100 dmg, to your base HP. Note that oxygen is subtracted before oxygen damage is calculated, so if you have 1 oxygen, you will take oxygen damage the next turn unless you get oxygen.\n4) If you are below your allowed pressure area, you will take 20 pressure damage directly to your HP for each level you are away from your lowest allowed level. If you are in a sub, you do not take pressure damage, but if your sub is below its allowed level it will take pressure damage.5) surprise attack: If you are in the middle, you have a 1/6 chance of surprise attack, deep = 1/3 chance, mariana trench = 1/2 chance. You cannot get surprise attacked in the surface. Note: a LAMP can lower your chance of getting surprise attacked, and a ghost suit changes the surprise attack rules slightly.\nRules of surprise attack - When you get surprise attacked, you receive a hit from the enemy immediately, without a chance of you hitting it. This is the first hit. After the first hit, the battle continues like a normal battle, with you getting a 1/2 chance of hitting the enemy. A surprise attack wastes your "move", so you cannot do any action that uses a "move" during this turn. The player DOES receive drops by a creature killed after a surprise attack.\n6) Once these calculations are complete, you may carry on with you turn and use your move, or do stuff such as using items and donating that do not require a turn.\nImportant note: pets are not affected by oxygen or pressure damage.```')
    
    elif message.content.upper().startswith('!START TURN'):
        await channel.send(content='css\nList of things that happen at the beginning of your turn, before you even make a move:\n1) If you died or changed your class on the last turn, you will be at the surface. (You may change your class at any time, which results in you dying instantly and respawning at the surface with no items, and the specified class.)\n2) 1 OX or oxygen is subtracted from you oxygen count.\n3) If you have 0 oxygen, you will receive 100 dmg, to your base HP. Note that oxygen is subtracted before oxygen damage is calculated, so if you have 1 oxygen, you will take oxygen damage the next turn unless you get oxygen.\n4) If you are below your allowed pressure area, you will take 20 pressure damage directly to your HP for each level you are away from your lowest allowed level. If you are in a sub, you do not take pressure damage, but if your sub is below its allowed level it will take pressure damage.5) surprise attack: If you are in the middle, you have a 1/6 chance of surprise attack, deep = 1/3 chance, mariana trench = 1/2 chance. You cannot get surprise attacked in the surface. Note: a LAMP can lower your chance of getting surprise attacked, and a ghost suit changes the surprise attack rules slightly.\nRules of surprise attack - When you get surprise attacked, you receive a hit from the enemy immediately, without a chance of you hitting it. This is the first hit. After the first hit, the battle continues like a normal battle, with you getting a 1/2 chance of hitting the enemy. A surprise attack wastes your "move", so you cannot do any action that uses a "move" during this turn. The player DOES receive drops by a creature killed after a surprise attack.\n6) Once these calculations are complete, you may carry on with you turn and use your move, or do stuff such as using items and donating that do not require a turn.\nImportant note: pets are not affected by oxygen or pressure damage.```')

    elif message.content.upper().startswith('!DEATH'):
        await channel.send(content='css\nWays to die:\n1) Suicide - you can kill yourself, your pet, or submarine/blubber base. You commit suicide when you change class (commands in "!commands"\n2) Pressure or oxygen - if you take too much oxygen or pressure damage, you may die. The player can die from both oxygen and pressure damage. Submarines can die of pressure damage. And pets and blubber bases, cannot die of these causes.\n3) Too much damage in battle - In battle a player can die when their HP becomes 0 or lower. Same applies for subs and blubber bases. A pets HP cannot go below -40. Pets only die, if their owner is not in possession of a fishing net at the time. (see "!petrules)\nUpon death - what happens when a player, pet, sub, or base dies?\n1) Player death - When a player dies, they lose all their items (necro saber exception), including submarines, and pets, but not blubber bases. Blubber bases hold 2 stacks of items, so when you die, you can come back and collect your items. A blubber basse has HP as well, but it stays in the same level and is not lost upon player death. When a player dies they also respawn on the surface with their classes base stats, and no items (necro saber exception) and their turn immediately ends.\n2) Pet death - A pet HP cannot go lower than -40 HP, once it is below 1 HP, the pet can no longer take damage or attack. If the holder of the pet does not have a fishing net, the pet disappears upon death, if the owner does have a fishing net, it can no longer take damage or attack, but it can be revived, and once it reaches 10 HP it can take damage and attack again. If a pet takes a lot of damage that would allow its HP to become below  -40, it will stay at -40HP and not go lower.\n3) Submarine death - Submarines cannot be healed with meat, only with repair kits (see "!sub rules" or "!repair kit") When a submarines HP becomes lower than 1, the player instantly exits it and the sub disappears and must be rebuilt. All the plates and laser upgrades that were added, also disappear.\n4) Blubber Base death - When blubber bases are destroyed indirectly, since they cannot take part in battles directly, they disappear along with any blubber add-ons and with any items inside of them. (see "!blubber base rules" for extra details.)```')
    
    elif message.content.upper().startswith('!OXYGEN RULE') or message.content.upper().startswith('!OXYGENRULE'):
        await channel.send(content='```css\nOxygen Rules:\n1) Oxygen is NOT DONATEABLE.\n2) If your oxygen is 0 at the beginning of your turn, you take 100 oxygen damage.\n3) At the beginning of your turn 1 oxygen is subtracted unless you are in the surface.\n4) Going to the surface refills you oxygen to max.\n5) Max oxygen is 5```')

    elif message.content.upper().startswith('!TROUT'):
        await channel.send(embed=embeds['TROUT'])

    elif message.content.upper().startswith('!ARIEL'):
        await channel.send(embed=embeds['ARIEL'])

    elif message.content.upper().startswith('!SALT'):
        await channel.send(embed=embeds['SALT'])

    elif message.content.upper().startswith('!TIGER F'):
        await channel.send(embed=embeds['TIGERF'])

    elif message.content.upper().startswith('!TIGERF'):
        await channel.send(embed=embeds['TIGERF'])

    elif message.content.upper().startswith('!GAR'):
        await channel.send(embed=embeds['GAR'])

    elif message.content.upper().startswith('!TURTLE'):
        await channel.send(embed=embeds['TURTLE'])

    elif message.content.upper().startswith('!PIR'):
        await channel.send(embed=embeds['PIRANHA'])

    elif message.content.upper().startswith('!HATCHET F') or message.content.upper().startswith('!HATCHETF'):
        await channel.send(embed=embeds['HATCHETFISH'])

    elif message.content.upper().startswith('!OCTO'):
        await channel.send(embed=embeds['OCTO'])

    elif message.content.upper().startswith('!BIG T'):
        await channel.send(embed=embeds['BIG'])

    elif message.content.upper().startswith('!BIGT'):
        await channel.send(embed=embeds['BIG'])

    elif message.content.upper().startswith('!WATER'):
        await channel.send(embed=embeds['WATER'])

    elif message.content.upper().startswith('!TUMMY') or message.content.upper().startswith('!TET'):
        await channel.send(embed=embeds['TUMMY'])

    elif message.content.upper().startswith('!TOXIC') or message.content.upper().startswith('!WASTE'):
        await channel.send(embed=embeds['TOXIC'])

    elif message.content.upper().startswith('!BLUE'):
        await channel.send(embed=embeds['BLUE'])

    elif message.content.upper().startswith('!GREAT W'):
        await channel.send(embed=embeds['GREATW'])

    elif message.content.upper().startswith('!GREATW') or message.content.upper().startswith('!WHITE'):
        await channel.send(embed=embeds['GREATW'])

    elif message.content.upper().startswith('!GIANT L') or message.content.upper().startswith('!LIO'):
        await channel.send(embed=embeds['GIANTL'])

    elif message.content.upper().startswith('!GIANTL'):
        await channel.send(embed=embeds['GIANTL'])

    elif message.content.upper().startswith('!MARLIN'):
        await channel.send(embed=embeds['MARLIN'])

    elif message.content.upper().startswith('!ALBINO'):
        await channel.send(embed=embeds['ALBINO'])

    elif message.content.upper().startswith('!MUSH'):
        await channel.send(embed=embeds['MUSH'])

    elif message.content.upper().startswith('!BARRACUDA'):
        await channel.send(embed=embeds['BARRACUDA'])

    elif message.content.upper().startswith('!TIGER O'):
        await channel.send(embed=embeds['TIGERO'])

    elif message.content.upper().startswith('!TIGERO'):
        await channel.send(embed=embeds['TIGERO'])

    elif message.content.upper().startswith('!SHOVELNOSE G'):
        await channel.send(embed=embeds['SHOVELNOSE'])

    elif message.content.upper().startswith('!SHOVELNOSEG'):
        await channel.send(embed=embeds['SHOVELNOSE'])

    elif message.content.upper().startswith('!SHOVEL NOSE G'):
        await channel.send(embed=embeds['SHOVELNOSE'])

    elif message.content.upper().startswith('!VORTEX'):
        await channel.send(embed=embeds['VORTEX'])

    elif message.content.upper().startswith('!LARGEMOUTH'):
        await channel.send(embed=embeds['LARGEMOUTH'])

    elif message.content.upper().startswith('!LARGE MOUTH'):
        await channel.send(embed=embeds['LARGEMOUTH'])

    elif message.content.upper().startswith('!TUNA'):
        await channel.send(embed=embeds['TUNA'])

    elif message.content.upper().startswith('!MORAY'):
        await channel.send(embed=embeds['MORAY'])

    elif message.content.upper().startswith('!ELECTRIC E'):
        await channel.send(embed=embeds['ELECTRICE'])

    elif message.content.upper().startswith('!ELECTRICE'):
        await channel.send(embed=embeds['ELECTRICE'])

    elif message.content.upper().startswith('!PUFFER'):
        await channel.send(embed=embeds['PUFFER'])

    elif message.content.upper().startswith('!GREAT D'):
        await channel.send(embed=embeds['MINNOW'])

    elif message.content.upper().startswith('!GREATD') or message.content.upper().startswith('!DIVING M') or message.content.upper().startswith('!MINNOW'):
        await channel.send(embed=embeds['MINNOW'])

    elif message.content.upper().startswith('!REEFBACK'):
        await channel.send(embed=embeds['REEFBACK'])

    elif message.content.upper().startswith('!REEF BACK'):
        await channel.send(embed=embeds['REEFBACK'])

    elif message.content.upper().startswith('!STONEFISH'):
        await channel.send(embed=embeds['STONEFISH'])

    elif message.content.upper().startswith('!STONE FISH'):
        await channel.send(embed=embeds['STONEFISH'])

    elif message.channel.guild.get_member(client.user.id).mentioned_in(message) and memes_enabled:
        await channel.send(
            content=
            'WHO DAFUQ PINGED ME?!?!\nhttps://cdn.discordapp.com/attachments/456279746955706378/480396163607166986/ping_angerey.gif'
        )
        await channel.send(content=('Aha, it was you who pinged me!'))
        await channel.send(content=message.author.mention)

    elif ('BOT OF THE DEPTHS' in message.content.upper()) and memes_enabled:
        await channel.send(content='Did someone need me?')

    elif message.content.upper().startswith('!GLITCH'):
        await channel.send(embed=embeds['GLITCH'])
        await (await channel.send(
            content=
            'attack is 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9',tts=memes_enabled)).delete() 

    elif message.content.upper().startswith('!GRAVE'):
        await channel.send(embed=embeds['GRAVE'])

    elif message.content.upper().startswith('!PHAN'):
        await channel.send(embed=embeds['PHAN'])

    elif message.content.upper().startswith('!NECRO E'):
        await channel.send(embed=embeds['NECRO'])

    elif message.content.upper().startswith('!NECROE'):
        await channel.send(embed=embeds['NECRO'])

    elif message.content.upper().startswith('!GIANT S'):
        await channel.send(embed=embeds['GIANTS'])

    elif message.content.upper().startswith('!GIANTS'):
        await channel.send(embed=embeds['GIANTS'])

    elif message.content.upper().startswith('!SAND'):
        await channel.send(embed=embeds['SAND'])

    elif message.content.upper().startswith('!ELECTRIC R'):
        await channel.send(embed=embeds['ELECTRICR'])

    elif message.content.upper().startswith('!ELECTRICR'):
        await channel.send(embed=embeds['ELECTRICR'])

    elif message.content.upper().startswith('!WARP'):
        await channel.send(embed=embeds['WARP'])

    elif message.content.upper().startswith('!WOB'):
        await channel.send(embed=embeds['WOB'])

    elif message.content.upper().startswith('!TRENCH'):
        await channel.send(embed=embeds['TRENCH'])

    elif message.content.upper().startswith('!ANGLER'):
        await channel.send(embed=embeds['ANGLER'])

    elif message.content.upper().startswith('!DARK'):
        await channel.send(embed=embeds['DARK'])

    elif message.content.upper().startswith('!CTHU'):
        await channel.send(embed=embeds['CTHU'])

    elif message.content.upper().startswith('!BULL'):
        await channel.send(embed=embeds['BULL'])

    elif message.content.upper().startswith('!ELECTRIC L'):
        await channel.send(embed=embeds['ELECTRICL'])

    elif message.content.upper().startswith('!ELECTRICL'):
        await channel.send(embed=embeds['ELECTRICL'])

    elif message.content.upper().startswith('!RED'):
        await channel.send(embed=embeds['RED'])

    elif message.content.upper().startswith('!CA'):
        await channel.send(embed=embeds['CA'])

    elif message.content.upper().startswith('!MICRO'):
        await channel.send(embed=embeds['MICRO'])

    elif message.content.upper().startswith('!GHOST'):
        await channel.send(embed=embeds['GHOST'])

    elif message.content.upper().startswith('!FRILLED'):
        await channel.send(embed=embeds['FRILLED'])

    elif message.content.upper().startswith('!ARMORED'):
        await channel.send(embed=embeds['ARMORED'])

    elif message.content.upper().startswith('!IRON'):
        await channel.send(embed=embeds['IRON'])

    elif message.content.upper().startswith('!STEEL'):
        await channel.send(embed=embeds['STEEL'])

    elif message.content.upper().startswith('!MARLIN S'):
        await channel.send(embed=embeds['MSWORD'])

    elif message.content.upper().startswith('!MARLINSW'):
        await channel.send(embed=embeds['MSWORD'])

    elif message.content.upper().startswith('!MARLINSO'):
        await channel.send(embed=embeds['MSWORD'])

    elif message.content.upper().startswith('!CORAL'):
        await channel.send(embed=embeds['CORAL'])

    elif message.content.upper().startswith('!WHALE'):
        await channel.send(embed=embeds['COCK'])

    elif message.content.upper().startswith('!WOOD'):
        await channel.send(embed=embeds['WOOD'])

    elif message.content.upper().startswith('!MEAT'):
        await channel.send(embed=embeds['MEAT'])

    elif message.content.upper().startswith('!BLUBBER'):
        await channel.send(embed=embeds['BLUBBER'])

    elif message.content.upper().startswith('!SUIT'):
        await channel.send(embed=embeds['SUIT'])

    elif message.content.upper().startswith('!SLIME'):
        await channel.send(embed=embeds['SLIME'])

    elif message.content.upper().startswith('!WAT'):
        await channel.send(embed=embeds['WATT'])

    elif message.content.upper().startswith('!P CORPSE'):
        await channel.send(embed=embeds['PCORPSE'])

    elif message.content.upper().startswith('!PUFFERFISH CORPSE'):
        await channel.send(embed=embeds['PCORPSE'])

    elif message.content.upper().startswith('!PUFFER FISH CORPSE'):
        await channel.send(embed=embeds['PCORPSE'])

    elif message.content.upper().startswith('!PLAT'):
        await channel.send(embed=embeds['PLATINUM'])

    elif message.content.upper().startswith('!SHOVELNOSE'):
        await channel.send(embed=embeds['SHOVEL1NOSE'])

    elif message.content.upper().startswith('!SHOVEL NOSE'):
        await channel.send(embed=embeds['SHOVEL1NOSE'])

    elif message.content.upper().startswith('!SCALE'):
        await channel.send(embed=embeds['SCALES'])

    elif message.content.upper().startswith('!SKY BLADE'):
        await channel.send(embed=embeds['SKYBLADE'])

    elif message.content.upper().startswith('!SKYBLADE'):
        await channel.send(embed=embeds['SKYBLADE'])

    elif message.content.upper().startswith('!W C'):
        await channel.send(embed=embeds['WCORPSE'])

    elif message.content.upper().startswith('!WOBBEGONG C'):
        await channel.send(embed=embeds['WCORPSE'])

    elif message.content.upper().startswith('!OX'):
        await channel.send(embed=embeds['OXYGEN'])

    elif message.content.upper().startswith('!BLUBBER BASE'):
        await channel.send(embed=embeds['BLUBBERBASE'])

    elif message.content.upper().startswith('!BLUBBERBASE'):
        await channel.send(embed=embeds['BLUBBERBASE'])

    elif message.content.upper().startswith('!NECRO BLADE'):
        await channel.send(embed=embeds['NECROBLADE'])

    elif message.content.upper().startswith('!NECROBLADE'):
        await channel.send(embed=embeds['NECROBLADE'])

    elif message.content.upper().startswith('!GHOST'):
        await channel.send(embed=embeds['GHOSTSUIT'])

    elif message.content.upper().startswith('!BIO W'):
        await channel.send(embed=embeds['BIOWHEEL'])

    elif message.content.upper().startswith('!BIOW'):
        await channel.send(embed=embeds['BIOWHEEL'])

    elif message.content.upper().startswith('!BIG S'):
        await channel.send(embed=embeds['BIGSHOVEL'])

    elif message.content.upper().startswith('!BIGSH'):
        await channel.send(embed=embeds['BIGSHOVEL'])

    elif message.content.upper().startswith('!LAMP'):
        await channel.send(embed=embeds['LAMP'])

    elif message.content.upper().startswith('!FISHING'):
        await channel.send(embed=embeds['FISHINGNET'])

    elif message.content.upper().startswith('!PLATINUM JUICE'):
        await channel.send(embed=embeds['JUICE'])

    elif message.content.upper().startswith('!PLATINUMJUICE'):
        await channel.send(embed=embeds['JUICE'])

    elif message.content.upper().startswith('!SHRINE'):
        await channel.send(embed=embeds['SHRINE'])

    elif message.content.upper().startswith('!OXYGEN TANK'):
        await channel.send(embed=embeds['TANK'])

    elif message.content.upper().startswith('!OXYGENTANK'):
        await channel.send(embed=embeds['TANK'])

    elif message.content.upper().startswith('!SHOVEL'):
        await channel.send(embed=embeds['SHOVEL'])

    elif message.content.upper().startswith('!BIO R'):
        await channel.send(embed=embeds['BIOREACTOR'])

    elif message.content.upper().startswith('!BIOR'):
        await channel.send(embed=embeds['BIOREACTOR'])

    elif message.content.upper().startswith('!GEN'):
        await channel.send(embed=embeds['GENERATOR'])

    elif message.content.upper().startswith('!REPAIR'):
        await channel.send(embed=embeds['REPAIR KIT'])

    elif message.content.upper().startswith('!NANOCELL F'):
        await channel.send(embed=embeds['NANOCELLFREEZE'])

    elif message.content.upper().startswith('!NANO CELL F'):
        await channel.send(embed=embeds['NANOCELLFREEZE'])

    elif message.content.upper().startswith('!NANOCELLF'):
        await channel.send(embed=embeds['NANOCELLFREEZE'])

    elif message.content.upper().startswith('!CLASSIC'):
        await channel.send(embed=embeds['CLASSICALFREEZE'])

    elif message.content.upper().startswith('!QUAN'):
        await channel.send(embed=embeds['QUANTUMFREEZE'])

    elif message.content.upper().startswith('!SEA HAWK'):
        await channel.send(embed=embeds['SEAHAWK'])

    elif message.content.upper().startswith('!SEAHAWK'):
        await channel.send(embed=embeds['SEAHAWK'])

    elif message.content.upper().startswith('!TRI'):
        await channel.send(embed=embeds['TRICLOPS'])

    elif message.content.upper().startswith('!STINGRAY'):
        await channel.send(embed=embeds['STINGRAY'])

    elif message.content.upper().startswith('!STING RAY'):
        await channel.send(embed=embeds['STINGRAY'])

    elif message.content.upper().startswith('!NANO'):
        await channel.send(embed=embeds['NANOCELL'])

    elif message.content.upper().startswith('!TITANIUM LASER'):
        await channel.send(embed=embeds['LASER'])

    elif message.content.upper().startswith('!TITANIUMLASER'):
        await channel.send(embed=embeds['LASER'])

    elif message.content.upper().startswith('!TITANIUM PLATE'):
        await channel.send(embed=embeds['PLATES'])

    elif message.content.upper().startswith('!TITANIUMPLATE'):
        await channel.send(embed=embeds['PLATES'])

    elif message.content.upper().startswith('!NECRO SAB'):
        await channel.send(embed=embeds['NECROSABER'])

    elif message.content.upper().startswith('!NECROSAB'):
        await channel.send(embed=embeds['NECROSABER'])

    elif message.content.upper().startswith('!RECOVERED'):
        await channel.send(embed=embeds['RECOVEREDSABER'])

    elif message.content.upper().startswith('!INFINITY'):
        await channel.send(embed=embeds['INFINITY'])

    elif message.content.upper().startswith('!W AR'):
        await channel.send(embed=embeds['WARMOR'])

    elif message.content.upper().startswith('!WOBBEGONG AR'):
        await channel.send(embed=embeds['WARMOR'])

    elif message.content.upper().startswith('!PLATINUM CHEST'):
        await channel.send(embed=embeds['CHESTPLATE'])

    elif message.content.upper().startswith('!PLATINUMCHEST'):
        await channel.send(embed=embeds['CHESTPLATE'])

    elif message.content.upper().startswith('!PLATINUM HELMET'):
        await channel.send(embed=embeds['HELMET'])

    elif message.content.upper().startswith('!PLATINUMHELMET'):
        await channel.send(embed=embeds['HELMET'])

    elif message.content.upper().startswith('!PLATINUM GR'):
        await channel.send(embed=embeds['GREAVES'])

    elif message.content.upper().startswith('!PLATINUMGR'):
        await channel.send(embed=embeds['GREAVES'])

    elif message.content.upper().startswith('!PLATINUM BOOT'):
        await channel.send(embed=embeds['BOOTS'])

    elif message.content.upper().startswith('!PLATINUMBOOT'):
        await channel.send(embed=embeds['BOOTS'])

    elif message.content.upper().startswith('!SKY S'):
        await channel.send(embed=embeds['SKYSWORD'])

    elif message.content.upper().startswith('!SKYSW'):
        await channel.send(embed=embeds['SKYSWORD'])

    elif message.content.upper().startswith('!SKY SO'):
        await channel.send(embed=embeds['SKYSWORD'])

    elif message.content.upper().startswith('!FLAMING'):
        await channel.send(embed=embeds['FLAMING'])

    elif message.content.upper().startswith('!SHIFT'):
        await channel.send(embed=embeds['SHIFTING'])

    elif message.content.upper().startswith('!SHOT'):
        await channel.send(embed=embeds['SHOTGUN'])

    elif message.content.upper().startswith('!HAT'):
        await channel.send(embed=embeds['HATCHET'])

    elif message.content.upper().startswith('!VEGAN'):
        await channel.send(embed=embeds['VEGAN'])

    elif message.content.upper().startswith('!TITA'):
        await channel.send(embed=embeds['TITANIUM'])

    elif message.content.upper().startswith('!CLASS'):
        await channel.send(
            content=
            "```diff\n- Player Classses:\nWhen you start a game, or immediately after you die, you have the opprotunity to change you class. Each class has a unique ability(s). There are 5 classes, their names and abilities follow.```\n```css\nHunter:\n- starts with 150 HP.\n- starts with 50 ATK\n- Receive x2 meat received from creature drops\n\Berserker:\n- For every 10 damage below Max HP, the berserker, gets that much ATK. (For example, if the HP is 20 below Max, the berserker has +20 ATK until it heals). (ATK+HP is always the same).\n- This does not apply for shield, or submarine HP.)\n- When a enemy is about to land a killing blow on the Berserker, the Berserker gets a final hit. (If the berserker kills the enemy with this blow, the Berserker does not die).\n\nFisherman:\n- Starts with 40 ATK\n- Starts game with a fishing net\n- Can catch 1 star creatures on battle turn\n- Has a 1/2 chance on catching a 2 star creature on battle turn\n\nForager:\n- Receive x1.5 supplies from everything except donations (Rounds up)\n- Can flee creatures immediately on battle turn (only applies in surface). (instead of 1/2 chance of flee)\n\nDiver:\n- Can go one level down lower than other classes without taking pressure damage\n- gets to move up or down a level once a turn, without using their move\n- Receive +1 Max Oxygen\n- During a battle, on their turn, the Diver can drag a creature up or down one level. (The creature takes +20 pressure damage at the beginning of the turn, for every level farther away from it's 'home' level it becomes. When the battle ends, the diver exists in the level that it dragged the creature to. The drag ability is an alternative to attacking. If the Diver uses it’s drag ability it gets HALF the drops of the creature it kills (if odd number ROUND DOWN)!)\n- Only the diver can use the sky sword in battle. This does not use the battle turn, and it will move the creature and the diver up one level. Whereas dragging normally does use you battle turn.```\n```diff\n- In order to change you class, type '!changeclass (name of class)'. You will automatically die, and you class will be changed. When you die naturally, you will be prompted for a class change.```"
        )
    
    elif (len(message.content) >= 500) and memes_enabled:
        await channel.send(content='Eee, 2 long 2 reed!')
    
    elif message.content.upper().startswith('!!') and memes_enabled:
        await channel.send(content='!really?')

    elif message.content.startswith('!') and (('no u') in message.content or ('gay') in message.content or('bad') in message.content or ('trash') in message.content or ('ur mom') in message.content or ('your mom') in message.content or ('lesbian') in message.content or ('stupid') in message.content or ('dumb') in message.content or ('idiot') in message.content or ('ur fat') in message.content or ('ur trash') in message.content or ('ur dumb') in message.content) and memes_enabled:
        from random import randint
        thing = randint(1,5)
        if thing == 1:
            await channel.send(content='**NO U**')
        elif thing == 2:
            await channel.send(content='https://tothedepths.weebly.com/uploads/1/2/1/7/121779998/no_u_4.webp')
        elif thing == 3:
            await channel.send(content='https://tothedepths.weebly.com/uploads/1/2/1/7/121779998/download__1_.jpeg')
        elif thing == 4:
            await channel.send(content='https://tothedepths.weebly.com/uploads/1/2/1/7/121779998/download.jpeg')
        else:
            await channel.send(content='||ur dumb||')
    
    elif message.content.upper().startswith('.CALL') or message.content.upper().startswith('.FIGHT') or message.content.upper().startswith('.ATTACK') or message.content.upper().startswith('.REGEN') or message.content.upper().startswith('.ENDTURN') or message.content.upper().startswith('.HELP') or message.content.upper().startswith('.ENTER') or message.content.upper().startswith('.FORAGER') or message.content.upper().startswith('.BERSERKER') or message.content.upper().startswith('.HUNTER') or message.content.upper().startswith('.DIVER') or message.content.upper().startswith('.FISHERMAN') or message.content.upper().startswith('.SUICIDE') or message.content.upper().startswith('.USE') or message.content.upper().startswith('.ANNOUNCE') or message.content.upper().startswith('.ATTACK') or message.content.upper().startswith('.COMMANDSLIST') or message.content.upper().startswith('.CREATEGAME') or message.content.upper().startswith('.ENEMY') or message.content.upper().startswith('.FLEE') or message.content.upper().startswith('.GAME') or message.content.upper().startswith('.GATHER') or message.content.upper().startswith('.HELPTOPICS') or message.content.upper().startswith('.INVITE') or message.content.upper().startswith('.ITEMS') or message.content.upper().startswith('.LEAVE') or message.content.upper().startswith('.REGEN') or message.content.upper().startswith('.SHUTDOWN') or message.content.upper().startswith('.START') or message.content.upper().startswith('!HIBERNATE') or message.content.upper().startswith('!MEME') or message.content.upper().startswith('!ENABLE') or message.content.upper().startswith('!DISABLE') or message.content.upper().startswith('.STATS') or message.content.upper().startswith('!SUGGEST') or message.content.upper().startswith('!HELP'):
        pass
    
    else:
        if message.content.startswith('!') or message.content.startswith('.'):
            spellcheck_list = Spellchecker.candid_operations(message.content.upper())
            dat_message='```css\nSorry you inputted the command wrong, (or spelled it improperly) below are some input options similar to yours for each word.\nNote: It is possible that the bot still responds, that does not necessarily mean you inputted the proper command though.\n- If what you wanted did not show up, type ".commands" to get a full list of commands```'
            for i in range(len(spellcheck_list)):
                if spellcheck_list[i] != []:
                    dat_message = dat_message + '```diff\n- Word ' + str(i+1) + ":    " + ', '.join(spellcheck_list[i]) + '```'
            if spellcheck_list[0][0][0] != message.content[0]:
                dat_message = dat_message + '**You also used the wrong prefix the correct prefix is ' + spellcheck_list[0][0][0] + '**'
            await channel.send(content=dat_message)

#---------------------------------------------------------------------------------------------
 
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='working...'), status=discord.Status('idle'))
    print('We have logged in as {0.user}'.format(client))
    global datrole
    bot_mod_id_list = {}


    with open('role_ids.txt', mode='r+') as file: 
    #reads the dictionary

        for line in file: 
            #split each line into guild_id and role_id and convert each to int (since discord's stuff is int) 
            guild_id, role_id = map(int, line.split()) 
            bot_mod_id_list[guild_id] = role_id
        file.close()

    for guild in client.guilds:
        #list of all the role ids in the guild
        role_ids = [role.id for role in guild.roles] # u can do that?
        #if the role id that we be looking for no in list, it must no exist so must create we shall
        role_id = 0
        with open('role_ids.txt', mode='r+') as file: 
            for line in file:
                if int(guild.id) == int((line.split())[0]):
                    role_id = int(line.split()[1])
                    break
        if (int(role_id) in role_ids):
            pass
        else:
            try:
                datrole = await guild.create_role(name="Bot Moderator")  #if allowed (write)
                datrole.edit(mentionable=True, position=(client.self.user.top_role)-1)
                bot_mod_id_list.update({guild.id : datrole.id})
            except: discord.errors.Forbidden
                #do nothing
    file = open('role_ids.txt', 'w')
    file.seek(0)
    file.truncate() 
    for guild_id, role_id in bot_mod_id_list.items(): 
        file.write('{} {}\n'.format(guild_id, role_id))

    #roleno   = discord.utils.get(server.roles, id=idea)
    #for i in chan_list:
    #    if (('general' in i.name.lower()) or ('game-room' in i.name.lower())) and (type(i) is discord.TextChannel) and i.permissions_for(i.guild.me).send_messages:
    #       await i.send(content='```diff\nThe Catalog Bot of information is now online\n- Type "!help" to get started with the help menu.\n- Type "!commands" to get a list of commands for the game bot.```')
    await client.change_presence(activity=discord.Game(name='Ready'), status=discord.Status('online'))
@client.event
#change to yellow   
async def on_message(message):
    await client.change_presence(activity=discord.Game(name='working...'), status=discord.Status('idle'))
    #change to green
    channel = message.channel
    author = message.author
    global hibernation
    global memes_enabled
    bot_mod = False
    f = open('role_ids.txt', 'r')
    for line in f:
        if message.guild.id == int((line.split())[0]):
            role_id = int((line.split())[1])
    role_ids = [role.id for role in author.roles]
    if int(role_id) in role_ids:
        bot_mod = True
    f.close()


    if message.author == client.user:
        return

    if not (message.guild in hibernation):
        await CheckCommands(message, channel)
    
    if '@someone' in message.content:
        from random import randint
        await channel.send(content=message.guild.members[randint(0, len(message.guild.members)-1)].mention)

    if message.content.upper().startswith('!HELP'):
        await channel.send(
            content=
            "```diff\n-Commands:\n!rules - get a full description of the To the Depths Rules.\n!creatures - full list of creatures\n!resources - full list of resources.\n!craftitems - get a full list of craftable items.\n!classes - List of different types of characters you can choose from for unique abilities.\n!weapons - get a list of weapons, armor, and subs as well as special rules about these categories.\n!commands - List of commands that show you how to play the game.\n- If you want help in any category, you don't need to type help before what you want help with. Just type in the name of the item, creature, level, etc.\nIf the is a part of the game that you feel the help-bot does not provide enough help on, Type: '!SUGGEST (question/suggestion)' and I will try to add it as soon as possible```"
        )
    
    elif message.content.upper().startswith('!SUGGEST'):
        suggestion = message.content[8:]
        me = await client.get_user_info(312662306980888588)
        await me.send(content=suggestion)
        await channel.send(content='Your suggestion/complaint/suggestion has been filed')

    elif (message.content.upper().startswith('!SHUTDOWN') or message.content.upper().startswith('!SHUT DOWN')) and author.id == 312662306980888588:
            await channel.send(content='Bot of the Depths shutting down')
            await client.logout()
            quit()

    elif message.content.upper().startswith('!HIBERNATE') and bot_mod:
        if author.permissions.administrator == True:
            await channel.send(content='Catalog Bot going into hibernation mode.')
            if message.guild in hibernation:
                pass
            else:
                hibernation.append(message.guild)
        else:
            await channel.send(content='The bot in your server, does not have administrator permissions.  This means that you cannot perform this action, as the command is not secure to specific users.  Please give the bot administrator permissions in order to perform this command.')

    elif message.content.upper().startswith('!AWAKE') and bot_mod:
        if author.permissions.administrator == True:
            await channel.send(content='```diff\nThe Catalog Bot of information is now awake\n- Type "!help" to get started with the help menu.\n- Type "!commands" to get a list of commands for the game bot.```')
            if message.guild in hibernation:
                hibernation.remove(message.guild)
        else:
            await channel.send(content='The bot in your server, does not have administrator permissions.  This means that you cannot perform this action, as the command is not secure to specific users.  Please give the bot administrator permissions in order to perform this command.')

    elif message.content.upper().startswith('!ENABLE MEMES') and (author.id == 312662306980888588 or author.id == 315682382147485697):
        await channel.send(content='Memes have been enabled')
        memes_enabled = True
    
    elif message.content.upper().startswith('!DISABLE MEMES') and (author.id == 312662306980888588 or author.id ==315682382147485697):
        await channel.send(content='Memes have been disabled')
        memes_enabled = True

    elif message.content.upper().startswith('!MEME STATUS'):
        if memes_enabled == True:
            await channel.send(content='Memes are currently enabled')
        else:
            await channel.send(content='Memes are currently disabled')
    
    await client.change_presence(activity=discord.Game(name='Ready'), status=discord.Status('online'))

client.run('<your id here>')