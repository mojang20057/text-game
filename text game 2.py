import random
import sys

health = random.randint(15, 38)
print(f"your health is: {health}")
while health > 0:
    while True:
        def zombie_attack(healht, damage_to):
                healht -= damage_to
                print(f"""You pick up a stick from the ground,
flailing it around in front of you. The zombie bites you dealing {damage_to} damage.""")
                return healht

        def attacking(zombieh, damage_against):
                zombieh -= damage_against
                print(f"""You manage to hit the zombie dealing {damage_against} damage.""")
                return zombieh

        def zombie_fight(healht, damage_to):
            healht -= damage_to
            print(f"""You wield your sword, slashing at the zombie.
The zombie bites you dealing {damage_to} damage.""")
            return healht
        print("""You are in a flat plain with little memory of what you were doing.
To the north is a run down barn with what seems to be a living scarecrow.
To the south is a small river, you see some fish swimming around in it.
To the east is what seems to be a small forest.
To the west you only see more flatland.""")
        direction = input("What do you do? ").lower()
        if direction in "go west"  "west" "head west":
            print("""You head west, only finding more flatland.
Nothing interesting here, so you head back.""")
        if direction in "go south" "south" "head south":
            print("""You reach the river, the sound of the water calmly being splashed about by the fish sooths you.
You watch the fish for a while before heading back.""")
        if direction in "go east" "east" "head east":
            print("""You head to the dark forest, unable to see in front of you.
You hear a loud moan come from behind you, it's a zombie!
You try to run away but trip on a fallen branch,
just as you think it's the end, you feel something grab you and lead you out of the forest.
'Hi friend, I'm sam' says the scarecrow.'
'You're lucky I lost ma hat or no one woulda saved ya, now how about helping me find ma hat? I'll give ya this sword to help kill that zombie.'
Sam hands you a sword after he finishes talking""")
            help = input("Will you help the scarecrow? ").lower()
            if help in "yes" "help":
                print("""You enter the forest and begin to search around.
You can go west back to the farm.
North or south around the edge of the forest.
Or east, deeper into the forest.""")
                while True:
                    direction2 = input("Which way will you go? ").lower()
                    if direction2 in "go west" "west" "head west":
                        print("""you arrive back at the farm.
The scarecrow is working again and looks at you as he hears your footsteps.
'I told you to get ma hat, where is it?' he asks angrily.
Upon seeing him you realise he might kill you and return to the forest""")
                    if direction2 in "north" "south" "go north" "go south" "head north" "head south":
                        print("You walk around the edge of the forest seeing no sign of a hat so return to where you were.")
                    if direction2 in "go east" "east" "head east":
                        print("""As you head deeper into the small forest it quickly becomes harder and harder to see.
After a minute its almost impossible to see in front of you.
You suddenly hear a loud moan coming from nearby.
'W-was that zombie?' The zombie approaches you, ready to fight.""")
                        while True:
                            damage_against = random.randint(0, 5)
                            damage_to = random.randint(2, 8)
                            zombie_health = random.randint(15, 20)
                            print(f"the zombies health is: {zombie_health}")
                            while True:
                                if health <= 0:
                                    print("You died to a zombie")
                                    sys.exit()
                                fight = input("What will you do? ").lower()
                                if fight in "help" "what" "what?" "what am i meant to do":
                                    print("""Enemy name: Shows you the enemies health and how much damage they can do.
Myself: Shows you your health and how much damage you can do.
Block: Needs a shield, takes a turn, allows you to take no damage from an enemy and do reduced damage back.
Potion: Use a potion to heal if you have some.
Attack: Takes a turn, attack the enemy, dealing damage.""")
                                if fight in "myself" "I" "health" "check health":
                                    print(f"Your health is {health} 3-12 damage")
                                if fight in "zombie" "zombie sats":
                                    print(f"The enemies health is {zombie_health} 2-8 damage")
                                if fight in "fight" "attack":
                                    health = zombie_fight(health, random.randint(2, 8))
                                    zombie_health = attacking(zombie_health, random.randint(3, 12))
                                if zombie_health <= 0:
                                    print("""Congrats, you killed the zombie, you took the scarecrows hat back and triumphantly return.
'Oh wow, you killed a zombie, well done, now if you'll hand over my hat I'll join you.'""")
                                    sys.exit()
            else:
                print("""You decide not to help the scarecrow by punching him in the face,
but as you move your hand the scarecrow impales the hoe he was using in your chest.
The hoe plants it's self firmly in the ground.
'No one messes with sam the scarecrow, bitch!'
you lay there bleeding out, unable to move""")
                sys.exit()
        if direction in "go north" "north" "head north":
            print("""As you approach the run down barn, you see the scarecrow plowing a field.
Nearby there are animal pens, overgrown with weeds and grass, it looks like nothing has been in them for a while.
As you reach the barn you see a run down house not to far away but before you can do anything the scarecrow pipes up.
Well it's been a long time since I saw a friendly face aroun' these parts'
you explain what you remember to the scarecrow.
'I'll join you on your journey if you can find ma hat, it's somewhere in the forest over there'""")
            help = input("Will you help the scarecrow? ").lower()
            if help in "yes" "help":
                print("""You enter the forest and begin to search around, you can go west back to the farm.
North or south around the edge of the forest.
Or east, deeper into the forest""")
                while True:
                    direction2 = input("which way will you go? ").lower()
                    if direction2 in "go west" "west" "head west":
                        print("""you arrive back at the farm, the scarecrow is working again and looks at you as he hears your footsteps.
'I told you to get ma hat, where is it?' he asks angrily.
Upon seeing him you realise he might kill you and return to the forest""")
                    if direction2 in "north" "south" "go north" "go south" "head north" "head south":
                        print("you walk around the edge of the forest seeing no sign of a hat so return to where you were.")
                    if direction2 in "go east" "east" "head east":
                        print("""As you head deeper into the small forest it quickly becomes harder and harder to see.
After a minute its almost impossible to see in front of you.
You suddenly hear a loud moan coming from nearby.
'W-was that zombie?'""")
                        decision = input("will you run away? ").lower()
                        if decision in "yes" "run away":
                            print("""you run out of the forest chased by the zombie to the treeline,
it appears it can't leave the forest, the scarecrow rushes over upon seeing you bolt out of the forest.
'well I'll be damned, that's ma hat, that zombie is wearin' my hat, i'm sure you can take it out, so here take my sword'
the scarecrow hands you a sword, a little worse for ware but it'll still kill things""")
                        else:
                            damage_against = random.randint(0, 5)
                            damage_to = random.randint(2, 8)
                            zombie_health = random.randint(15, 20)
                            print(f"the zombies health is: {zombie_health}")
                            while True:
                                if health <= 0:
                                    print("you died to a zombie")
                                    sys.exit()
                                fight = input("what will you do? ").lower()
                                if fight in "help" "what" "what?" "what am i meant to do":
                                    print("""enemy name: shows you the enemies health and how much damage they can do
myself: shows you your health and how much damage you can do
block: needs a shield, takes a turn, allows you to take no damage from an enemy and do reduced damage back
potion: use a potion to heal if you have some
attack: takes a turn, attack the enemy, dealing damage""")
                                if fight in "myself" "I" "health" "check health":
                                    print(f"{health} 0-5 damage")
                                if fight in "zombie" "zombie sats":
                                    print(f"{zombie_health} 2-8 damage")
                                if fight in "fight" "attack":
                                    health = zombie_attack(health, random.randint(2, 8))
                                    zombie_health = attacking(zombie_health, random.randint(0, 5))
                                if fight in "run" "run away":
                                    print("""you run out of the forest chased by the zombie to the treeline,
it appears it cant leave the forest, the scarecrow rushes over upon seeing you bolt out of the forest.
'well I'll be damned, that's ma hat, i'm sure you can take it out, so here take my sword'
the scarecrow hands you a sword, a little worse for ware but it'll still kill things""")
                                    break
                                if zombie_health <= 0:
                                    print("""Congrats, you killed the zombie, you took the scarecrows hat back and triumphantly return.
'Oh wow, you killed a zombie with a stick, well done, now you deserve a better weapon.
The scarecrow hands you a sword, a little worse for ware but it'll still kill things and it's better than a stick.
you hand the scarecrow's hat back to him""")
                                    sys.exit()
                        decision2 = input("you now have a sword what will you do? ").lower()
                        if decision2 in "go back" "back" "in the forest" "forest" "fight" "fight the zombie" "attack":
                            print("you walk back to the forest with confidence")
                            damage_against = random.randint(3, 12)
                            damage_to = random.randint(2, 8)
                            zombie_health = random.randint(15, 20)
                            print(f"the zombies health is: {zombie_health}")
                            while True:
                                if health <= 0:
                                    print("you died to a zombie")
                                    sys.exit()
                                fight = input("what will you do? ").lower()
                                if fight in "help"  "what" "what?" "what am i meant to do":
                                    print("""enemy name: shows you the enemies health and how much damage they can do
myself: shows you your health and how much damage you can do
block: needs a shield, takes a turn, allows you to take no damage from an enemy and do reduced damage back
potion: use a potion to heal if you have some
attack: takes a turn, attack the enemy, dealing damage""")
                                if fight in "myself" "I" "health" "check health":
                                    print(f"{health} 3-12 damage")
                                if fight in "zombie" "zombie sats":
                                    print(f"{zombie_health} 2-8 damage")
                                if fight in "fight" "attack":
                                    health = zombie_fight(health, random.randint(2, 8))
                                    zombie_health = attacking(zombie_health, random.randint(3, 12))
                                if zombie_health <= 0:
                                        print("""Congrats, you killed the zombie, you took the scarecrows hat back and triumphantly return.
'Oh wow, you killed a zombie, well done, now if you'll hand over my hat I'll join you.'""")
                                        sys.exit()
            else:
                print("""You decide not to help the scarecrow by punching him in the face,
but as you move your hand the scarecrow impales the hoe he was using in your chest.
The hoe plants it's self firmly in the ground.
'No one messes with sam the scarecrow, bitch!'
you lay there bleeding out, unable to move""")
                sys.exit()
