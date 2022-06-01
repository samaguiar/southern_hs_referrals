import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('behaviorEvents.csv')
df2 = pd.read_csv('southernGrade.csv')

def clean_behavior(df):
    df['Student Number'] = df['Student Number'].astype(str)
    clean_behavior = df[['Student Number', 'Student', 'Event Type', 'Date', 'Submitted By', 'Comments']]
    clean_behavior['Student Number'] = clean_behavior['Student Number'].str.replace('.0', '')
    clean_behavior['Student Number'] = clean_behavior['Student Number'].astype(str)
    return(clean_behavior)
    
def clean_grades(df):
    clean_grades = df[['Student ID', 'Academy', 'Gender', 'Race']]
    clean_grades = clean_grades.rename(columns={'Student ID':'Student Number'})
    nan_value = float('NaN')
    clean_grades.replace('JCPS #', nan_value, inplace=True)
    clean_grades.dropna(subset = ['Student Number'], inplace=True)
    clean_grades['Student Number'].drop_duplicates(keep='first')
    return(clean_grades)

def combined_data(df, df2):
    df_combined = pd.merge(df2, df, on='Student Number', how='outer')
    df_combined.dropna(subset = ['Student'], inplace=True)
    return(df_combined)

def event_type(df):
    event = input('Which referral event do you want to look at?  ')
    df_event = df[df['Event Type']]
    return(df_event)
    #have user input type of violation and show breakdown by gender, race, academy

def teacher_data(df):
    pass
    #have user input a teacher and output graph breakdown of referral type

print('Behavior', clean_behavior(df))
print('Grades', clean_grades(df2))

print(combined_data(clean_behavior(df), clean_grades(df2)))