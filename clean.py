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
    #make a copy of the input DataFrame
    clean_df = df.copy()

    #convert 'Student Number' to a string
    clean_df['Student Number'] = clean_df['Student Number'].astype(str)

    #select specific columns for the cleaned DataFrame
    clean_df = clean_df[['Student Number', 'Student', 'Event Type', 'Date', 'Submitted By', 'Comments']]

    #Replace .0 in Student Number and convert to string again
    clean_df['Student Number'] = clean_df['Student Number'].str.replace('.0', '', regex=True)
    clean_df['Student Number'] = clean_df['Student Number'].astype(str)
    return(clean_df)
    
##Race is currently as dummy variable --> need to add to funciton to rewrite as specific name of race
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
     #make a copy of the input DataFrame
    clean_grades_df = df.copy()

    clean_grades = clean_grades_df[['Student ID', 'Academy', 'Gender', 'Race']]
    clean_grades = clean_grades.rename(columns={'Student ID':'Student Number'})

    #convert NaN values to a float
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