# NPC.py
# ------

import pandas as pd
import random
NPC_Quirk = pd.DataFrame()
NPC_Quirk['Roll'] = range(1,21)
NPC_Quirk['Quirk'] = ['Uses too few words','Uses too many words','Worships the player characters','Absurdly upbeat','Disgustingly unhygienic','Terrified of player characters','Constantly curses','Sings all their dialogue like a song','So arrogant that they are basically a villain','Horrifyingly hedonistic','Has a bizarre (BUT NOT RACIST) accent','Does not really care about the players, just wants to go back to [their hobby]','Distantly related to one of your players','Wants to fight the players, but will immediately wuss out if the players call them on it','Impressibly flirty','All sentences are questions','Reformed Enemy','Wants to be shot in the face','Echocast influencer','Constantly shouting']
NPC_Trait = pd.DataFrame()
NPC_Trait['Roll'] = range(1,21)
NPC_Trait['Trait'] = ['Long-Legged','Very old','Quite young','Eye-Patched','Two left feet','Toothless','Bad-breathed','Mohawked','Squinty','Sunburned','On a unicycle','Sleepy','Your Dad','Jumpy','Always chewing','No ears','Drunk','Nerdy','Half-dead','Masked']
print('NPC Trait:')
print('----------')
DiceRoll = random.randint(1, NPC_Trait['Roll'].iloc[-1])
print('Dice Roll =',DiceRoll)
print('Trait:',NPC_Trait.iloc[DiceRoll-1,1])