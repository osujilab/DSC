# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 12:32:14 2024

@author: Chris
"""

#This file is intended to split .csv's of Trios exports
#These files often have multiple tables of differing names
#I want to split based on lines that denote these names so these can then
#be interpreted by simple dataframe analysis

import os
import pandas as pd
import csv
import fnmatch

#Define csvsplitter function
def csvsplitter(filename):
    step_number = 0
    record = False
    step_file = []
    with open(filename, newline='', mode='r') as csvfile:
        reader = csv.reader(csvfile, dialect='excel')
        for row in reader: #Iterate rows until you find the row that indicates a step has started
            if row == []:
                print('end writing')
                record_rows(step_file, step_number, filename) #Record the step as a csvfile in another function
                step_file = [] #Then clear it 
                record = False #Set to false to clear any chaff
            elif row[0] == '[step]':
                print("Begin writing")
                step_number += 1 #This is to iterate for steps with multiple names
                record = True
            elif record == True:
                step_file.append(row)
            elif record == False:
                pass 
            
    

def record_rows(step_file, step_number, filename):
    #This function records rows until a 'step' signifier taken from step_file list
    print(step_file[0])
    #Clean up the string so we don't have / in file
    new_step_name = step_file[0][0].replace('/','_').replace(' ','-')  #[0][0] is nested... ugly

    newfilename = str(step_number)+"_"+new_step_name+"_"+filename
    print(newfilename)
    with open(newfilename, 'w',newline='') as csvfile:
        stepwriter = csv.writer(csvfile, dialect='excel') #Writing step by step
        for row in step_file:
            stepwriter.writerow(row)
            
def filemove(current_directory, new_directory, name_restriction):
    #This function moves all files meeting a name restriction to a new directory path
    files = os.listdir(current_directory) #Iterate through all files in current directory
    for file in files: #Files here represent both input and the output
        if fnmatch.fnmatch(file, "*"+name_restriction+"*"):
            p1 = os.path.join(current_directory,file)
            p2 = os.path.join(new_directory, file)
            os.rename(p1, p2)

current_directory = os.getcwd()
files = os.listdir(current_directory)
to_split = [] #Grabbing all of our files and preparing them for splitting
for file in files:
    if file.endswith(".csv") and fnmatch.fnmatch(file, "*"):
        to_split.append(file)


#Now go through csv splitting for each file
for file in to_split:
    csvsplitter(file) #Split up the file
    new_folder = file.replace(".csv","") 
    path = os.path.join(current_directory,new_folder)
    os.mkdir(path)#create a destination folder for the file and its outputs
    filemove(current_directory, path, str(file)) #move outputs to the destination folder
    
    



#def 


csvsplitter(to_split[0])

#def



#def 