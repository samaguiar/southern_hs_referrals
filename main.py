import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import csv_export as c


def event_type_graph(df):
    """
    input: takes csv file with data set with teacher/admin and student data removed

    ouput: bar graph showing the number of referrals for each event
    """
    df_events = df['Event Type'].value_counts().reset_index()

    #renaming columns
    df_events = df_events.rename(columns = {'index': 'Event Type', 'Event Type': 'Number of Referrals'})

    #create bar graph
    ax = plt.bar(df_events['Event Type'], df_events['Number of Referrals'])

    #rotate event names
    plt.xticks(rotation=90)

    #change labels
    plt.xlabel('Event Type')
    plt.ylabel('Number of Referrals')
    plt.title('Number of Referrals for Each Event')
    return(plt.show())

    ###future goals:
    ####have user input type of violation and show breakdown by gender, race, academy
    ####event = input('Which referral event do you want to look at?  ')
    ####creating dataframe using only event type and number of referrals
    

def teacher_data(df):
    pass
    #have user input a teacher and output graph breakdown of referral type

if __name__ == "__main__":
    df1 = pd.read_csv('behaviorEvents.csv')
    df2 = pd.read_csv('southernGrade.csv')
    df = c.csv_export(df1, df2)