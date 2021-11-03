# Code by: Anuradha Gunawardhana
# Date: 2021.11.03
# Usage: python plot_random_split.py DATA.npy LABELS.npy
# This will plot randomly selected four eeg chunks from DATA.npy

import matplotlib.pyplot as plt
import numpy as np
import random
import sys

data = np.load(sys.argv[1])
labels = np.load(sys.argv[2])

fig, axs = plt.subplots(4,1,figsize=(8,8),constrained_layout=True)

t = np.arange(data.shape[1])
electrodes = ['AF3','T7','Pz','T8','AF4']

for p in range(4):
    idx = random.randint(0,data.shape[0])
    for i in range(5):
        axs[p].plot(t, data[idx,:,i],alpha=0.8, label=electrodes[i])
        axs[p].set_ylabel(r'$Amplitude\ \mathrm{(\mu V)}$')
    axs[p].set_title("Chunk ID: {} Label: {:n}".format(idx, labels[idx]),)

axs[0].legend()
axs[3].set_xlabel(r'$Samples\ (128\ Hz)$')
plt.show()
