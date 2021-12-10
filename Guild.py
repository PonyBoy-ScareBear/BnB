# Guild.py

import pandas as pd
import random

Guild_Table = pd.DataFrame()
Guild_Table['Roll'] = range(1,9)
Guild_Table['Guild'] = [
    'Ashen','Dahlia','Feriore','Hyperius',
    'Malefactor','Pangoblin','Stoker','Torgue']

Guild = Guild_Table['Guild'].iloc[random.randint(1,8)-1]