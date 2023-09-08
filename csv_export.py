import pandas as pd
import matplotlib.pyplot as plt
import clean as c
import os

df1 = pd.read_csv('behaviorEvents.csv')
df2 = pd.read_csv('southernGrade.csv')

#combines two csv files into one data frame
df = c.combined_data(c.clean_behavior(df1), c.clean_grades(df2))
df = c.ferpa_data(df)

#creates csv file of the clean data file for clean data frame for Tableau
if not os.path.exists("output_file.csv"):
    df.to_csv('output_file.csv', index=False)
else:
    print("The file 'output_file.csv' already exsists in the directory.")