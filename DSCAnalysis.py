# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 12:37:49 2022

@author: Chris
"""

#This file takes a set of DSC files that have been pre-split and plots them as a matplotlib figure
#Will do this work on all folders that exist in the DSC folder - can add inputs to make it quicker.

import os
import pandas as pd
import fnmatch
import matplotlib.pyplot as plt


current_directory = os.getcwd()
folder = "C15PD_NanoCry_H80_attempt1"
path = os.path.join(current_directory,folder)

new_directory = os.chdir(path)

files = os.listdir(new_directory)

num_steps = [8,6] #What dsc steps do you want to include - make as list


graphed_files = []
for file in files: #This loop iterates over files, then checks every file for the step number in the front position
    for step in num_steps:
        index = file.find(str(step))
        if index ==0:
            graphed_files.append(file)

    
#Now we read the csv
plt.figure(figsize = (8,8), dpi=100)
#Here are generic parameters
fsize = 20

#Generate_Labels
labels = []
for file in graphed_files:
    label = file.replace(".csv","").replace(folder, "")
    labels.append(label)

for file in graphed_files:
    df = pd.read_csv(file, header = 2)
    
    x = df['°C']
    y = df['W/g']
    plt.plot(x,y)
    plt.xlabel("°C", fontsize = fsize)
    plt.ylabel('W/g', fontsize = fsize)
    plt.title(folder, fontsize = fsize*1.25)
    plt.legend(labels, loc='lower left')
    plt.yticks(fontsize = fsize*0.8)
    plt.tight_layout(pad= 1.1)
    plt.xlim([-100, 80])
    plt.ylim([-0.5, 0.5])

plt.show()
plt.savefig(folder+"loop2"+".png")