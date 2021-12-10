# Cache.py

import pandas as pd
import random

# Cache Size
# ----------
# Single Box / Tiny Chest   =   1d6
# Small Cache               =   2d6
# Medium Cache              =   3d6
# Large Cache               =   5d6
# Legendary Cache           =   6d6

Tiny = random.randint(1,6)
Small = Tiny + random.randint(1,6)
Medium = Small + random.randint(1,6)
Large = Medium + random.randint(1,6) + Tiny
Legendary = Large + random.randint(1,6)

Cache_Table = pd.DataFrame()
Cache_Table['Roll'] = range(1,37)
Cache_Table['Item(s)'] = [
    '30g','Common Health Potion (1d8)','Common Shield Potion (1d8)',
    '30g + Common Health Potion (1d8)','30g + Common Shield Potion (1d8)','50g + Random Potion',
    '30g + Uncommon Health Potion','30g + Uncommon Shield Potion','50g + Uncommon Health Potion',
    '50g + Uncommon Shield Potion','50g + Common Gun (Random)','80g + Common Health Potion (1d8)',
    '80g + Uncommon Health Potion + Random Potion','80g + Uncommon Shield Potion + Grenades (2)','80g + Random Potions (2) + Common Relic',
    '80g + Uncommon Gun (Random) + Grenades (2)','80g + Uncommon Gun (Random) + Uncommon Health Potion','100g + Grenades (2) + Random Potions (2)',
    '100g + Uncommon Gun (Random) + Random Potion','100g + Rare Health Potions (2) + Grenade Mod','100g + Rare Shield Potions (2) + Grenade Mod',
    '100g + Random Potions (3) + Uncommon Relic','100g + Rare Gun (Random) + Shield Mod','100g + Rare Gun (Random) + Grenades (2) + Shield Mod',
    '120g + Common Relic + Rare Health Potions (2) + Grenades (2)','120g + Grenades (3) + Random Potions (2)','120g + Rare Gun (Random) + Random Potions (2)',
    '120g + Uncommon Relic Twofer Potions (2) + Shield Mod','120g + Rare Gun (Random) + Grenade Mod','150g + Epic Health Potions (2) + Epic Shield Potion + Grenade Mod',
    '150g + Rare Relics (2) + Shield Mod + Random Potions (2)','150g + Epic Gun (Random) + Random Potions (2) + Grenade Mod','150g + Epic Gun (Random) + Grenades (6)',
    '150g + Random Potions (3) + Grenade Mod + Rare Relic','150g + Epic Gun (Random) + Rare Relic + Epic Health Potions (3) + Shield Mod','200g + Epic Gun (Random) + Grenade Mod + Grenades (5) + Epic Health Potions (3) + Shield Mod + Rare Relics (3)'
]


def Cache(Cache_size):
    if Cache_size=='Tiny':
        Cache_Item = Cache_Table['Item(s)'].iloc[Tiny]

    elif Cache_size=='Small':
        Cache_Item = Cache_Table['Item(s)'].iloc[Small]

    elif Cache_size=='Medium':
        Cache_Item = Cache_Table['Item(s)'].iloc[Medium]

    elif Cache_size=='Large':
        Cache_Item = Cache_Table['Item(s)'].iloc[Large]

    else:
        Cache_Item = Cache_Table['Item(s)'].iloc[Legendary]
    
    print('{} Cache: {}'.format(Cache_size,Cache_Item))