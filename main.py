import pandas as pd
import matplotlib.pyplot as plt
import csv_export as c


def event_type(df):
    event = input('Which referral event do you want to look at?  ')
    df_event = df[df['Event Type']]
    return(df_event)
    #have user input type of violation and show breakdown by gender, race, academy

def teacher_data(df):
    pass
    #have user input a teacher and output graph breakdown of referral type

if __name__ == "__main__":
    df1 = pd.read_csv('behaviorEvents.csv')
    df2 = pd.read_csv('southernGrade.csv')
    df = c.csv_export(df1, df2)
    print(df)