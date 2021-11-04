# Code by: Anuradha Gunawardhana
# Date: 2021.11.03
# Usage: python plot_random_full.py RECORD_DIRECTORY
# This will plot a random complete (.csv) record

import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
import pandas as pd
import random
import sys

path = sys.argv[1] if sys.argv[1][:-1] == '/' else sys.argv[1]+'/'

records = [f for f in listdir(path) if isfile(join(path, f))]
idx = random.randint(0, len(records))
rec = path + records[idx]
df = pd.read_csv(rec, delimiter=", ",engine='python')
df.plot(subplots=True,figsize=(10,8),title="Record: {}".format(records[idx]))
print("{} Record (ID:{})".format("Last" if idx==-1 else "",len(records)))
plt.xlabel(r'$Samples\ (For\ 40s)$')
plt.show()