# Loot_Drop.py

import pandas as pd
import random

Drop_Table = pd.DataFrame()
Drop_Table['Roll'] = range(1,5)
Drop_Table['1st'] = ['10g','Health Potion (1d8)','Shield Potion (1d8)','Grenade (1)']
Drop_Table['2nd'] = ['30g','Health Potion (2d8+5)','Shield Potion (1d8)','Grenades (2)']
Drop_Table['3rd'] = ['Health Potion (3d8+10)','Shield Potion (3d8+10)','Random Potion (1)','Grenades (3)']
Drop_Table['4th'] = ['Random Potions (2)','Grenade Mod','Shield Mod','Random Gun']
Drop_Table['5th'] = ['Grenade Mod','Shield Mod','Common Relic','Random Gun']
Drop_Table['6th'] = ['Grenade Mod','Uncommon Relic','Random Gun','Random Gun']

def LootDrop(BR,D4=[1,0,0,0,0,0]):
    # 1 Roll
    # 1st Item
    if BR>=1 and BR<=3:
        print('1st Item:',Drop_Table['1st'].iloc[D4-1])

    # 2 Rolls
    elif BR>=4 and BR<=6:
        # 1st Item
        print('1st Item:',Drop_Table['1st'].iloc[D4[0]-1])
        # 2nd Item
        print('2nd Item:',Drop_Table['2nd'].iloc[D4[1]-1])

    # 3 Rolls
    elif BR>=7 and BR<=12:
        # 1st Item
        print('1st Item:',Drop_Table['1st'].iloc[D4[0]-1])
        # 2nd Item
        print('2nd Item:',Drop_Table['2nd'].iloc[D4[1]-1])
        # 3rd Item
        print('3rd Item:',Drop_Table['3rd'].iloc[D4[2]-1])

    # 4 Rolls
    elif BR>=13 and BR<=18:
        # 1st Item
        print('1st Item:',Drop_Table['1st'].iloc[D4[0]-1])
        # 2nd Item
        print('2nd Item:',Drop_Table['2nd'].iloc[D4[1]-1])
        # 3rd Item
        print('3rd Item:',Drop_Table['3rd'].iloc[D4[2]-1])
        # 4th Item
        print('4th Item:',Drop_Table['4th'].iloc[D4[3]-1])

    # 5 Rolls
    elif BR>=19 and BR<=24:
        # 1st Item
        print('1st Item:',Drop_Table['1st'].iloc[D4[0]-1])
        # 2nd Item
        print('2nd Item:',Drop_Table['2nd'].iloc[D4[1]-1])
        # 3rd Item
        print('3rd Item:',Drop_Table['3rd'].iloc[D4[2]-1])
        # 4th Item
        print('4th Item:',Drop_Table['4th'].iloc[D4[3]-1])
        # 5th Item
        print('5th Item:',Drop_Table['5th'].iloc[D4[4]-1])

    # 6 Rolls
    else:
        # 1st Item
        print('1st Item:',Drop_Table['1st'].iloc[D4[0]-1])
        # 2nd Item
        print('2nd Item:',Drop_Table['2nd'].iloc[D4[1]-1])
        # 3rd Item
        print('3rd Item:',Drop_Table['3rd'].iloc[D4[2]-1])
        # 4th Item
        print('4th Item:',Drop_Table['4th'].iloc[D4[3]-1])
        # 5th Item
        print('5th Item:',Drop_Table['5th'].iloc[D4[4]-1])
        # 6th Item
        print('6th Item:',Drop_Table['6th'].iloc[D4[5]-1])