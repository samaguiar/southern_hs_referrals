import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import csv_export as c

#function written to answer "What is the most written type of referral?"
###future goals:
    ####have user input type of violation and show breakdown by gender, race, academy
    ####event = input('Which referral event do you want to look at?  ')
    ####creating dataframe using only event type and number of referrals
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
    
#function written to answer "Which academy has the most referals?"
def academy_data(df):
    pass

#function written to answer "For a specific referral, is there bias towards a certain group?"
##currently only looking at dress code violations
###future goals:
    ####have user input type of violation and show breakdown by gender, race, academy
    ####event = input('Which referral event do you want to look at?  ')
    ####creating dataframe using only event type and number of referrals
def dress_code_bias_gender(df):
    df_dressCode = df[df['Event Type'].str.contains('Dress Code')]
    user_input = input('Do you want to analyze the dress code violations in terms of gender or race? Press 1 for Gender, 2 for Race, and E to exit.')
    if user_input == "1":
        #Count the number of referrals by gender
        dressCode_Gender = df_dressCode['Gender'].value_counts().reset_index()
        dressCode_Gender = dressCode_Gender.rename(columns={'index':'Gender', 'Gender':'# of Referrals'})
        #define size of pie chart
        plt.figure(figsize=(6, 6))
        #define labels
        labels = dressCode_Gender['Gender']
        #define color choice for pie chart
        palette = sns.color_palette('bright')
        #create pie chart using mathplotlib
        plt.pie(dressCode_Gender['# of Referrals'], labels=labels, autopct='%1.1f%%', colors=palette)
        plt.title('Referrals by Gender for Dress Code Events')
        #show pie chart
        return(plt.show())
    elif user_input == "2":
        # Count the number of referrals by race
        dressCode_Race = df_dressCode['Race'].value_counts().reset_index()
        dressCode_Race = dressCode_Race.rename(columns={'index':'Race', 'Race':'# of Referrals'})
        #define size of pie chart
        plt.figure(figsize=(6, 6))
        #define labels
        labels = dressCode_Race['Race']
        #define color choice for pie chart
        palette = sns.color_palette('muted')
        #create pie chart using mathplotlib
        plt.pie(dressCode_Race['# of Referrals'], labels=labels, autopct='%1.1f%%', colors=palette)
        plt.title('Referrals by Race for Dress Code Events')
        #show pie chart
        return(plt.show())
    else:
        print('Error. Press 1 for Gender, 2 for Race, and E to exit.')

#future goal: have user input a teacher and output graph breakdown of referral type
def teacher_data(df):
    pass
    

if __name__ == "__main__":
    df1 = pd.read_csv('behaviorEvents.csv')
    df2 = pd.read_csv('southernGrade.csv')
    df = c.csv_export(df1, df2)
    #ask user to input 1, 2, 3, 4, 5 for each question type
    dress_code_bias_gender(df)