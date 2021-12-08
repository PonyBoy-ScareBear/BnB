# Badass_Modifier.py
# -----------------

import pandas as pd
import random
Badass_Modifier = pd.DataFrame()
Badass_Modifier['Roll'] = range(1,11)
Badass_Modifier['Modifier'] = ['TOUGH','FIRE','ELECTRIC','RAGING','CORROSIVE','EXPLOSIVE','FERAL','RAD','FROZEN','CHUBBY']
Badass_Modifier['Description'] = ['Takes a max of 10 damage from each attack','Deals and is immune to incendiary damage','Deals and is immune to shock damage','Deals double damage','Deals and is immune to corrosive damage','Deals and is immune to explosive damage','Gains extra movement each turn','Deals and is immune to radiation damage','Deals and is immune to cryo damage','Triple Health/Armor instead (always drops legendary item)']
DiceRoll = random.randint(1, Badass_Modifier['Roll'].iloc[-1])
print('Badass Modifier:')
print('----------------')
print('Dice Roll =',DiceRoll)
print('')
print(Badass_Modifier.iloc[DiceRoll-1,1])
print(Badass_Modifier.iloc[DiceRoll-1,2])