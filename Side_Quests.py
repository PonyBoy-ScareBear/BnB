# Side_Quests.py
# -----------

# Import Python Libraries & Packages
import pandas as pd
import random

# Side Quest Tables
# Location
Side_Loc_Table = pd.DataFrame()
Side_Loc_Table['Roll'] = range(1,11)
Side_Loc_Table['Location'] = ['Bandit Town','Dwarven Mining Camp','Blackpowder Workshop','Tiny Hut on the Edge of a Cliff','Feriore Lumbermill','Alas! Keep','Dahlia Commune','Enchanted Forest','Malefactor Lair','Torgue Laboratory']
# Interaction
Side_Int_Table = pd.DataFrame()
Side_Int_Table['Roll'] = range(1,11)
Side_Int_Table['Interaction'] = ['Help find a lost dragon whelp','Attempt a diplomatic takeover','Defend against bandits','Escort an NPC home','Rescue a kidnapped apothecary','Rid the area of vermin','Procure the finest hooch','Quell a rebellion','Hunt a rare creature','Search for relics']

# Side Quests Operation
print('Side Quest:')
print('-----------')
# Side Location
DiceRoll = random.randint(1, Side_Loc_Table['Roll'].iloc[-1])
print('Dice Roll =',DiceRoll)
print('Location:',Side_Loc_Table.iloc[DiceRoll-1,1])
print('')
# Side Interaction
DiceRoll = random.randint(1, Side_Int_Table['Roll'].iloc[-1])
print('Dice Roll =',DiceRoll)
print('Interaction:',Side_Int_Table.iloc[DiceRoll-1,1])