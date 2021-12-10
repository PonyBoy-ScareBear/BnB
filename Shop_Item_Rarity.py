# Shop_Item.py

import pandas as pd
import random

Shop_Rarity = pd.DataFrame()
Shop_Rarity['Roll'] = range(1,21)
Shop_Rarity['Rarity'] = [
    'Common','Common','Common','Common','Common','Common','Common',
    'Uncommon','Uncommon','Uncommon','Uncommon','Uncommon','Uncommon',
    'Rare','Rare','Rare','Rare',
    'Epic','Epic',
    'Legendary']

Shop_Type = pd.DataFrame()
Shop_Type['Roll'] = range(1,6)
Shop_Type['Type'] = ['Gun','Potion','Relic','Grenade','Shield']

# define size: 'Cart', 'Shack', 'Market', 'Shop', 'Store'
def shop_item(size,VHL):

    Shop_Items = pd.DataFrame()
    Shop_Items['Item #'] = []
    Shop_Items['Rarity'] = []
    Shop_Items['Type'] = []
    Shop_Items['Price'] = []

    if size=='Cart':
        for i in range(6):
            Shop_Items['Item #'].iloc[i] = i+1
            Shop_Items['Rarity'].iloc[i] = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
            Shop_Items['Type'].iloc[i] = Shop_Type[Shop_Type['Roll']==random.randint(1,5)]['Type']
            if Shop_Items['Type']=='Gun':
                if Shop_Items['Rarity']=='Common':
                    Shop_Items['Price'].iloc[i] = '50g'
                elif Shop_Items['Rarity']=='Uncommon':
                    Shop_Items['Price'].iloc[i] = '80g'
                elif Shop_Items['Rarity']=='Rare':
                    Shop_Items['Price'].iloc[i] = '120g'
                elif Shop_Items['Rarity']=='Epic':
                    Shop_Items['Price'].iloc[i] = '180g'
                else:
                    Shop_Items['Price'].iloc[i] = '300g'
            elif Shop_Items['Type']=='Relic':
                if Shop_Items['Rarity']=='Common':
                    Shop_Items['Price'].iloc[i] = '100g'
                elif Shop_Items['Rarity']=='Uncommon':
                    Shop_Items['Price'].iloc[i] = '250g'
                elif Shop_Items['Rarity']=='Rare':
                    Shop_Items['Price'].iloc[i] = '500g'
                elif Shop_Items['Rarity']=='Epic':
                    Shop_Items['Price'].iloc[i] = '1000g'
                else:
                    Shop_Items['Price'].iloc[i] = '2500g'
            elif Shop_Items['Type']=='Potion':
                
            

    elif size=='Shack':
        Item_1_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_2_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_3_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_4_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_5_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_6_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_7_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_8_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_9_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_10_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
    elif size=='Market':
        Item_1_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_2_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_3_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_4_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_5_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_6_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_7_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_8_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_9_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_10_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_11_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_12_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_13_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_14_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_15_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
    elif size=='Shop':
        Item_1_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_2_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_3_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_4_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_5_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_6_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_7_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_8_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_9_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_10_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_11_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_12_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_13_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_14_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_15_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_16_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_17_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_18_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_19_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_20_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
    else:
        Item_1_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_2_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_3_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_4_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_5_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_6_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_7_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_8_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_9_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_10_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_11_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_12_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_13_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_14_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_15_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_16_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_17_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_18_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_19_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_20_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_21_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_22_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_23_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_24_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_25_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_26_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_27_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_28_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_29_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_30_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_31_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_32_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_33_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_34_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_35_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_36_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_37_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_38_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_39_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_40_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_41_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_42_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_43_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_44_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_45_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_46_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_47_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_48_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_49_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']
        Item_50_rarity = Shop_Rarity[Shop_Rarity['Roll']==random.randint(1,20)]['Rarity']