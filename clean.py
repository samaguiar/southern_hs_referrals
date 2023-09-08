import pandas as pd

def clean_behavior(df):
    """
    input: csv file with following labels:
    Student Number
    Student
    Event Type
    Data
    Submitted By
    Comments

    output: cleaned csv file that converted 'Student Number' into a string
    """
    df['Student Number'] = df['Student Number'].astype(str)
    clean_behavior = df[['Student Number', 'Student', 'Event Type', 'Date', 'Submitted By', 'Comments']]
    clean_behavior['Student Number'] = clean_behavior['Student Number'].str.replace('.0', '')
    clean_behavior['Student Number'] = clean_behavior['Student Number'].astype(str)
    return(clean_behavior)
    
def clean_grades(df):
    """
    input: csv file with following labels:
    Student ID
    Academy
    Gender 
    Race


    output: cleaned csv file that has dropped Student Numbers containing NaN 
    and dropped duplicates of Student Numbers
    """
    clean_grades = df[['Student ID', 'Academy', 'Gender', 'Race']]
    clean_grades = clean_grades.rename(columns={'Student ID':'Student Number'})
    nan_value = float('NaN')
    clean_grades.replace('JCPS #', nan_value, inplace=True)
    clean_grades.dropna(subset = ['Student Number'], inplace=True)
    clean_grades['Student Number'].drop_duplicates(keep='first')
    return(clean_grades)

def combined_data(df, df2):
    """
    input: takes two csv files (grades and behavior) that both contain key 
    'Student Number'

    ouput: one csv files that contains information on grades and 
    behavior events by Student number
    """
    df_combined = pd.merge(df2, df, on='Student Number', how='outer')
    df_combined.dropna(subset = ['Student'], inplace=True)
    return(df_combined)

def ferpa_data(df):
    """
    input: combined data set of grades and behavior events

    output: data set with teacher/admin and student data removed
    """
    df_ferpa = df[['Gender', 'Race', 'Event Type', 'Date', 'Comments']].copy()
    return(df_ferpa)