import os
import pandas as pd
import numpy as np

file_path = './val2017label'
file_list = os.listdir(file_path)

files = []
for file1 in file_list:
    files.append(file1)
date = pd.DataFrame()
f = open('label.txt','w')
for file2 in files:
    for a in file_list:
        a = open('./val2017label/'+ file2,'r') 
        first_line = a.readlines()
        label = str(first_line)
        label = label[2:4]
    file_name = './val2017/' + file2[:] +' '+ label + '\n'
    file_name = file_name.replace('txt','jpg')
    f.write(file_name)
    
f.close()
