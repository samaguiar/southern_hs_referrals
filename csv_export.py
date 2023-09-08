import pandas as pd
import matplotlib.pyplot as plt
import clean as c
import os

##thought: combine with tableu_export.py to have one export program to run

def csv_export(df1, df2):
    #combines two csv files into one data frame
    df = c.combined_data(c.clean_behavior(df1), c.clean_grades(df2))
    df = c.ferpa_data(df)

    #creates csv file of the clean data file for clean data frame
    #if there is already a file exisiting, this will not run
    if not os.path.exists("output_file.csv"):
        df.to_csv('output_file.csv', index=False)
    else:
        print("The file 'output_file.csv' already exsists in the directory.")
    return(df)
