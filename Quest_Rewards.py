# Quest_Rewards.py

import pandas as pd
import random

Quest_Rewards_Table = pd.DataFrame()
Quest_Rewards_Table['Quest Level'] = range(1,31)
Quest_Rewards_Table['XP'] = [300,300,300,400,400,500,500,500,600,600,700,700,700,800,800,900,900,900,1000,1000,1100,1100,1100,1200,1200,1300,1300,1300,1500,1500]
Quest_Rewards_Table['Gold'] = [300,300,300,400,400,500,500,500,600,600,700,700,700,800,800,900,900,900,1000,1000,1200,1200,1200,1400,1400,1600,1600,1600,2000,2000]
Quest_Rewards_Table['Encounter BR (Per VH)'] = [7,7,7,10,10,12,12,12,14,14,17,17,17,19,19,21,21,21,23,23,25,25,27,27,27,28,28,28,30,30]

def QuestRewards_QL(QL):
    print(Quest_Rewards_Table[Quest_Rewards_Table['Quest Level']==QL])

def QuestRewards_VHL(VHL):
    print(Quest_Rewards_Table[Quest_Rewards_Table['Encounter BR (Per VH)']==VHL])