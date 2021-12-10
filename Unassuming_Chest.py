# Unassuming_Chest.py

import pandas as pd
import random

Unassuming_Chest_Table = pd.DataFrame()
Unassuming_Chest_Table['Roll'] = range(1,21)
Unassuming_Chest_Table['Item(s)'] = [
    'MIMIC','MIMIC','Potion (1d8 Health)','Common Gun (Random)','Common Gun (Favored)',
    'Grenades (2)','Shield Mod','Uncommon Gun (Random)','Uncommon Gun (Favored)','Potion (2d8 Health)',
    'Potion (2d8 Shield)','Rare Gun (Random)','Rare Gun (Favored)','Grenade Mod + Shield Mod','Epic Gun (Random)',
    'Epic Gun (Favored)','Epic Health Potion','Rare Relic','Legendary Gun (Random)','Legendary Gun (Favored)'
]

def UnassumingChest(roll):
    if roll==1 or roll==2:
        print('BM say, "SURPRISE, SUCKER". Then a MIMIC spawns right in front of the PC.')
    if roll==3:
        roll_1d8 = random.randint(1,8)
        print('Chest Item: Health Potion ({})'.format(roll_1d8))
    elif roll==10:
        roll_1d8 = random.randint(1,8)
        roll_2d8 = roll_1d8 + random.randint(1,8)
        print('Chest Item: Health Potion ({})'.format(roll_2d8))
    elif roll==11:
        roll_1d8 = random.randint(1,8)
        roll_2d8 = roll_1d8 + random.randint(1,8)
        print('Chest Item: Shield Potion ({})'.format(roll_2d8))
    else:
        ChestItem = Unassuming_Chest_Table['Item(s)'].iloc[roll]
        print('Chest Item:',ChestItem)