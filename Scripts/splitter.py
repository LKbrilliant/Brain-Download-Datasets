# Code by: Anuradha Gunawardhana
# Date: 2021.11.03
# Usage: python splitter.py RECORD_DIRECTORY
# This will split records in to smaller chunks of viewing one stimulus
# During the Splitting process, chunks which do not contain at least 250 samples of 100% contact quality will be discarded  
# After the splitting process the chunks will be saved as a numpy binary (.npy) with a separate label 

import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
import numpy as np
import sys
import time

recDir = sys.argv[1] if sys.argv[1][:-1] == '/' else sys.argv[1]+'/'

def drawProgressBar(percent, barLen = 20): 
    sys.stdout.write("\r")
    sys.stdout.write("Splitting the records: [{:<{}}] {:.0f}%".format("=" * int(barLen * percent), barLen, percent * 100))
    sys.stdout.flush()

def importData(recPath):
    records = [f for f in listdir(recPath) if isfile(join(recPath, f))]

    trainData = np.empty((0,250,5))
    labels = np.empty((0))

    total = 0

    for pp,file in enumerate(records):
        rec = recPath + file
        data = np.loadtxt(rec, delimiter=', ',skiprows=1)
 
        k = [idx for idx, tick in enumerate(data[:,7]) if tick]
        p = [i for i in k if i-1 not in k or i+1 not in k]  # Indices where the data going to be splitted 
        total += len(p)
        p.append(data.shape[0])
        if 0 not in p: p.insert(0,0)

        for i in range(len(p)-1):
            split_cq = data[:,8][p[i]:p[i+1]]
            if all(x == 100 for x in split_cq) and len(split_cq)>=250:      # CQ==100% and (length of data) >= 250
                trainData = np.append(trainData, [data[p[i]:p[i+1],1:6][:250]], axis=0)
                labels = np.append(labels, int(data[p[i]+100,6]))      
        drawProgressBar((pp+1)/len(records))

    removed = total - trainData.shape[0]
    print("\nTotal Number of Records: {}".format(len(records)))
    print("Total Samples: {}".format(total))
    print("Number of samples removed: {} - ({:.1%})".format(removed, removed/total))
    print("Training Data Shape:", trainData.shape)
    print("Labels Shape:", labels.shape)
    return trainData, labels

def dataComposition(arr): # Use this on label array(y)
    for i in np.unique(arr):
        p = np.count_nonzero(arr==i)
        print("Label:{:.1n}, Count:{} ({:.0%})".format(i, p, p/len(arr)))

t0 = time.time()
X, y = importData(recDir)

print('\n\nData Composition:')
dataComposition(y)

print('\nSaving data and labels...')
np.save(recDir[:-1]+'_data',X)
np.save(recDir[:-1]+'_labels',y)
print('Saving Complete')
print("Total processing time: {:.1f} minutes".format((time.time()-t0)/60))