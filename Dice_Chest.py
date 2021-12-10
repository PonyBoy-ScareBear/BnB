# Dice_Chest.py

import pandas as pd
import random

Dice_Chest_Table = pd.DataFrame()
Dice_Chest_Table['Roll'] = range(1,21)
Dice_Chest_Table['Item(s)'] = [
    'Uncommon Gun (Random)','Uncommon Gun (Favored)','Uncommon Gun (Favored) + Rare Health Potion','Uncommon Gun (Favored) + Common Relic','Uncommon Gun (Favored) + Random Potions (2)',
    'Rare Gun (Random)','Rare Gun (Favored)','Rare Gun (Favored) + Grenades (2)','Rare Gun (Favored) + Uncommon Relic','Rare Gun (Favored) + Grenades (2) + Shield Mod',
    'Epic Gun (Random)','Epic Gun (Favored)','Epic Gun (Favored) + Epic Health Potion','Epic Gun (Favored) + Rare Relic','Epic Gun (Favored) + Grenades (3) + Shield Mod',
    'Legendary Gun (Random)','Legendary Gun (Favored)','Legendary Gun (Favored) + Grenade Mod','Legendary Gun (Favored) + Epic Relic + Legendary Health Potion','Legendary Gun (Random) + Shield Mod + Grenade Mod + Random Potions (3)'
]

def DiceChest(roll):
    ChestItem = Dice_Chest_Table['Item(s)'].iloc[roll]
    print('Chest Item:',ChestItem)