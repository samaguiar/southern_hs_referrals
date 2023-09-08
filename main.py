import pandas as pd
import matplotlib.pyplot as plt
import clean as c

df1 = pd.read_csv('behaviorEvents.csv')
df2 = pd.read_csv('southernGrade.csv')

def event_type(df):
    event = input('Which referral event do you want to look at?  ')
    df_event = df[df['Event Type']]
    return(df_event)
    #have user input type of violation and show breakdown by gender, race, academy

def teacher_data(df):
    pass
    #have user input a teacher and output graph breakdown of referral type

#print('Behavior', clean_behavior(df))
#print('Grades', clean_grades(df2))

df = c.combined_data(c.clean_behavior(df1), c.clean_grades(df2))
df = c.ferpa_data(df)
print(df)