# Trauma.py
# ---------

import pandas as pd
import random
Temp_Trauma = pd.DataFrame()
Temp_Trauma['Roll'] = range(1,21)
Temp_Trauma['Trauma'] = ['Bad Luck','Immersive','Unloaded','Refractory','No Boom','Stumbling','Pistol Perplexion','Health Drain','Power Drain','Punch Drunk','Impatient','Wellllll Hello There','Catch-a-Phrase','Four Hundred and Four','Your Hands are Guns','You Had Me At "Roll For Initiative"','Brain Freeze','The Best Policy','Minor Issue','You are Claptrap']
Temp_Trauma['Description'] = ['The BREW-U malfunctions: roll on Permanent table','Must do a silly character voice. If you ever forget, take 1d6 damage.','A random equipped gun doesn;t spawn with you. You will see if for sale at the next shop you find.','Every time you roll a natural 20 on an attack roll, fall asleep for the next turn','Current grenades is set to 0','-1 on Talk and Traverse Checks for the day','Your vault hunter is unable to tell the difference between guns and food','-5 max health for the day','-20 max shields for the day','You must punch every non-combatant NPC you meet','-1 on search and sneak checks for the day','You must flirt with every NPC you meet.Including Bosses.','Your vault hunter is now desperate to popularize a stupid catch phrase they have come up with','One of your non-current guns does not respawn','Your currently equipped gun fuses into the bones of your hands. You no longer have fingers or the ability to grab things','Your vault hunter is now unrequitedly in love with another player vault hunter. Before the end of the day you must reveal your true feelings.','-1 on Insight and Interact Checks for the day','Your vault hunter is now incapable of lying for the rest of the day','Your vault hunter is now four years old. All their stats are the same, but they look like a four year old.','A bolt of lightning strikes you and turns you into a claptrap unit. All of your stats are reduced by 2 and you have to speak in an annoying voice until the end of the day.']
DiceRoll = random.randint(1, Temp_Trauma['Roll'].iloc[-1])
if DiceRoll==1:
    print('Temporary Trauma:')
    print('-----------------')
    print('Dice Roll =',DiceRoll)
    print('')
    print(Temp_Trauma.iloc[DiceRoll-1,1])
    print(Temp_Trauma.iloc[DiceRoll-1,2])
    print('')
    Perm_Trauma = pd.DataFrame()
    Perm_Trauma['Roll'] = range(1,21)
    Perm_Trauma['Trauma'] = ['Bad Reputation','How2English?','I Had a Bad Experience','Trinket','Least Favorite','Scar Tissue','Touchy Feely','Cool Eyepatch','Love and Loss','Synapse Oops','Your Dad is Dissapointed in You','Willful Ignorance','Riverdance','Family Vengeance','Crybaby','No Ships, Sherlock','Fart Fartington','18/20','Unsteady Hands','Godkiller']
    Perm_Trauma['Description'] = ['Word of how you fell in battle gets around. There is a 25 percent chance that any NPC you meet will have heard the embarrassing story of how you got beaten up, and will respect you less for it.','You forget 10 percent of your vocabulary. -1 on Talk Checks','You become terrified of the particular enemy type who defeated you. In all future combats with this particular enemy type, take -1 to all accuracy rolls','Loss of sentimental item. Probably something important to campaign','The other players must determine your least favorite food/music/film/book/whatever. That is now your FAVORITE thing in the world, and they will bring it up any time they can elegantly do so','Generates a horrific scar in the location where you took damage. 25 percent chance to be recognized when entering a town.','You have the insatiable urge to touch everything you see, including things you probably should not. -1 on Interact Checks','Your character loses an eye and has to wear a badass eyepatch over the socket. You get a 02 on search checks, but a +3 to interact checks','Your character is nursed back to health by an adorable, friendly animal that the BM chooses.The BM must then work the cute animal into the story, and then somehow tragically remove them within the next two sessions','Brain farts are now a medical condition you have. -1 on Insight Checks','Your dad hears about how you died. He is dissapointed in you. Your mom is still proud of you, though.','Your vault hunter refuses to believe they fell in battle and assumes everyone is misremembering the event.','Metal clogs get stuck to your feet. -1 on sneak checks.','Add "Jr." to the name of your character. You are now your own child, avenging the death of your parent.','Death hurts a lot, and your vault hunter cries when they think about it.','Your trusty sleuthing cap got rakk poop on it. -1 on search checks.','The name of you vault hunter is now Fart Fartington. This can never be changed. If your name is already Fart Fartington, "Fart Fartington" becomes their new nickname. Their name would now be Fart "Fart Fartington" Fartington.','Your depth perception got really deep. -1 on traverse checks','Whenever you swap guns, roll a d20. On a 1, the gun flies out of your hands and lands 2 squares away.','Your vault hunter blames the one TRULY responsible for their death: You. Your vault hunter now has a personal vendetta against you. The BM will insert you into the story somewhere and your vault hunter will do whatever is necessary to hunt you down and say some very harsh words.',]
    DiceRoll = random.randint(1, Perm_Trauma['Roll'].iloc[-1])
    print('Permanent Trauma:',Perm_Trauma.iloc[DiceRoll-1,1])
    print(Perm_Trauma.iloc[DiceRoll-1,2])
else:
    print('Temporary Trauma:')
    print('-----------------')
    print('Dice Roll =',DiceRoll)
    print('')
    print(Temp_Trauma.iloc[DiceRoll-1,1])
    print(Temp_Trauma.iloc[DiceRoll-1,2])