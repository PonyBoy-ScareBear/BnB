# Potions.py

import pandas as pd
import random

Potions_Table = pd.DataFrame()
Potions_Table['Roll'] = range(1,101)
Potions_Table['Potion'] = [
    'Common Tina Potion','Common Tina Potion','Common Tina Potion','Common Tina Potion','Common Tina Potion',
    'Common Health Potion','Common Health Potion','Common Health Potion','Common Health Potion','Common Health Potion',
    'Common Shield Potion','Common Shield Potion','Common Shield Potion','Common Shield Potion','Common Shield Potion',
    'Check Potion','Check Potion','Check Potion','Check Potion','Check Potion',
    'Element Potion','Element Potion','Element Potion','Element Potion','Element Potion',
    'Rare Tina Potion','Rare Tina Potion','Rare Tina Potion','Rare Tina Potion','Rare Tina Potion',
    'Rare Health Potion','Rare Health Potion','Rare Health Potion','Rare Health Potion','Rare Health Potion',
    'Rare Shield Potion','Rare Shield Potion','Rare Shield Potion','Rare Shield Potion','Rare Shield Potion',
    'Stat Potion','Stat Potion','Stat Potion','Stat Potion','Stat Potion',
    'Twofer Potion','Twofer Potion','Twofer Potion','Twofer Potion','Twofer Potion',
    'Epic Tina Potion','Epic Tina Potion','Epic Tina Potion','Epic Tina Potion','Epic Tina Potion',
    'Epic Health Potion','Epic Health Potion','Epic Health Potion','Epic Health Potion','Epic Health Potion',
    'Epic Shield Potion','Epic Shield Potion','Epic Shield Potion','Epic Shield Potion','Epic Shield Potion',
    'Lucky Potion','Lucky Potion','Lucky Potion','Lucky Potion','Lucky Potion',
    'Invisibility Potion','Invisibility Potion','Invisibility Potion','Invisibility Potion','Invisibility Potion',
    'Legendary Tina Potion','Legendary Tina Potion','Legendary Tina Potion','Legendary Tina Potion','Legendary Tina Potion',
    'Legendary Health Potion','Legendary Health Potion','Legendary Health Potion','Legendary Health Potion','Legendary Health Potion',
    'Legendary Shield Potion','Legendary Shield Potion','Legendary Shield Potion','Legendary Shield Potion','Legendary Shield Potion',
    'Fumble Potion','Fumble Potion','Fumble Potion','Fumble Potion','Fumble Potion',
    'Gold Farmer Potion','Gold Farmer Potion','Gold Farmer Potion','Gold Farmer Potion','Gold Farmer Potion']
Potions_Table['Effect'] = [
    'Roll 1d20 for bombass effect','Roll 1d20 for bombass effect','Roll 1d20 for bombass effect','Roll 1d20 for bombass effect','Roll 1d20 for bombass effect',
    'Regens 1d8 Health','Regens 1d8 Health','Regens 1d8 Health','Regens 1d8 Health','Regens 1d8 Health',
    'Recharges 1d8 Shield','Recharges 1d8 Shield','Recharges 1d8 Shield','Recharges 1d8 Shield','Recharges 1d8 Shield',
    '+5 to x Check for 1 hour','+5 to x Check for 1 hour','+5 to x Check for 1 hour','+5 to x Check for 1 hour','+5 to x Check for 1 hour',
    'Protection from x Element for 2 turns','Protection from x Element for 2 turns','Protection from x Element for 2 turns','Protection from x Element for 2 turns','Protection from x Element for 2 turns',
    'Roll 1d20+3 for bombass effect','Roll 1d20+3 for bombass effect','Roll 1d20+3 for bombass effect','Roll 1d20+3 for bombass effect','Roll 1d20+3 for bombass effect',
    'Regens 2d8+5 Health','Regens 2d8+5 Health','Regens 2d8+5 Health','Regens 2d8+5 Health','Regens 2d8+5 Health',
    'Recharges 2d8+5 Shield','Recharges 2d8+5 Shield','Recharges 2d8+5 Shield','Recharges 2d8+5 Shield','Recharges 2d8+5 Shield',
    '3 to x Stat Mod for 1 hour','3 to x Stat Mod for 1 hour','3 to x Stat Mod for 1 hour','3 to x Stat Mod for 1 hour','3 to x Stat Mod for 1 hour',
    'Gain 1d8+3 Health and Shield','Gain 1d8+3 Health and Shield','Gain 1d8+3 Health and Shield','Gain 1d8+3 Health and Shield','Gain 1d8+3 Health and Shield',
    'Roll 1d20+5 for bombass effect','Roll 1d20+5 for bombass effect','Roll 1d20+5 for bombass effect','Roll 1d20+5 for bombass effect','Roll 1d20+5 for bombass effect',
    'Regens 3d8+10 Health','Regens 3d8+10 Health','Regens 3d8+10 Health','Regens 3d8+10 Health','Regens 3d8+10 Health',
    'Recharges 3d8+10 Shield','Recharges 3d8+10 Shield','Recharges 3d8+10 Shield','Recharges 3d8+10 Shield','Recharges 3d8+10 Shield',
    'Reroll 1 Die per Attack for 2 turns','Reroll 1 Die per Attack for 2 turns','Reroll 1 Die per Attack for 2 turns','Reroll 1 Die per Attack for 2 turns','Reroll 1 Die per Attack for 2 turns',
    'Become Cloaked for 3 turns','Become Cloaked for 3 turns','Become Cloaked for 3 turns','Become Cloaked for 3 turns','Become Cloaked for 3 turns',
    'Roll 1d20+10 for bombass effect','Roll 1d20+10 for bombass effect','Roll 1d20+10 for bombass effect','Roll 1d20+10 for bombass effect','Roll 1d20+10 for bombass effect',
    'Regens 4d8+20 Health','Regens 4d8+20 Health','Regens 4d8+20 Health','Regens 4d8+20 Health','Regens 4d8+20 Health',
    'Recharges 4d8+20 Shield','Recharges 4d8+20 Shield','Recharges 4d8+20 Shield','Recharges 4d8+20 Shield','Recharges 4d8+20 Shield',
    'All 1s rolled become 20s for 2 hours','All 1s rolled become 20s for 2 hours','All 1s rolled become 20s for 2 hours','All 1s rolled become 20s for 2 hours','All 1s rolled become 20s for 2 hours',
    '+2d6 to all Cache Rolls for 2 hours','+2d6 to all Cache Rolls for 2 hours','+2d6 to all Cache Rolls for 2 hours','+2d6 to all Cache Rolls for 2 hours','+2d6 to all Cache Rolls for 2 hours']
Potions_Table['Price'] = [
    '15g','15g','15g','15g','15g',
    '20g','20g','20g','20g','20g',
    '15g','15g','15g','15g','15g',
    '20g','20g','20g','20g','20g',
    '15g','15g','15g','15g','15g',
    '25g','25g','25g','25g','25g',
    '40g','40g','40g','40g','40g',
    '30g','30g','30g','30g','30g',
    '40g','40g','40g','40g','40g',
    '70g','70g','70g','70g','70g',
    '80g','80g','80g','80g','80g',
    '100g','100g','100g','100g','100g',
    '90g','90g','90g','90g','90g',
    '100g','100g','100g','100g','100g',
    '120g','120g','120g','120g','120g',
    '200g','200g','200g','200g','200g',
    '250g','250g','250g','250g','250g',
    '230g','230g','230g','230g','230g',
    '250g','250g','250g','250g','250g',
    '270g','270g','270g','270g','270g']

def potion(roll):
    print(Potions_Table['Potion'].iloc[roll-1])
    print('------------------------------')
    print('Effect:',Potions_Table['Effect'].iloc[roll-1])
    print('Price:',Potions_Table['Price'].iloc[roll-1])