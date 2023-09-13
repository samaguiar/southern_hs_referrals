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

#function written to answer "For a specific referral, is there bias towards a certain group?"
##currently only looking at dress code violations
###future goals:
    ####have user input type of violation and show breakdown by gender, race, academy
    ####event = input('Which referral event do you want to look at?  ')
    ####creating dataframe using only event type and number of referrals
def dress_code_bias_gender(df):
    """
    input: takes csv file with data set with teacher/admin and student data removed

    ouput: pie chart showing the breakdown of dress code data for race or gender, depending on user input
    """
    df_dressCode = df[df['Event Type'].str.contains('Dress Code')]
    question = '''Do you want to analyze the dress code violations in terms of gender or race? 
    Press 1 for Gender, 2 for Race, and E to exit to main screen.
    '''
    user_input = input(question)
    while user_input.upper() != "E":
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
            plt.pie(dressCode_Gender['# of Referrals'], labels=labels, autopct='%1.1f%%', 
                    colors=palette, wedgeprops={'linewidth': 1, 'edgecolor': 'black'})
            plt.title('Referrals by Gender for Dress Code Events')
            #show pie chart
            return(plt.show())
        elif user_input == "2":
            # Count the number of referrals by race
            dressCode_Race = df_dressCode['Race'].value_counts().reset_index()
            dressCode_Race = dressCode_Race.rename(columns={'index':'Race', 'Race':'# of Referrals'})
            dressCode_Race = dressCode_Race.replace({'1':'Hispanic', '3':'Asian', 
                                                     '4':'African American/Black', '5':'Pacific Islander','6':'White', '7':'Two or More Races'})
            #define size of pie chart
            plt.figure(figsize=(6, 6))
            #define labels
            labels = dressCode_Race['Race']
            #define color choice for pie chart
            palette = sns.color_palette('muted')
            #create pie chart using mathplotlib
            plt.pie(dressCode_Race['# of Referrals'], labels=labels, autopct='%1.1f%%', 
                    colors=palette, wedgeprops={'linewidth': 1, 'edgecolor': 'black'})
            plt.title('Referrals by Race for Dress Code Events')
            #show pie chart
            return(plt.show())
        else:
            print('Error. Press 1 for Gender, 2 for Race, and E to exit.')
            user_input = input(question)

#function written to answer 'How has the number of referrals progressed over time?'
###future goals:
    ####have user input type to view overall number of referrals by gender, race, academy
    ####event = input('Which referral event do you want to look at?  ')
    ####creating dataframe using only event type and number of referrals
def change_in_referrals_gender(df):
    """
    input: takes csv file with data set with teacher/admin and student data removed

    ouput: bar graph showing the breakdown of the number of referrals for each month by gender
    """
    #convert data column to strings
    df['Date'] = df['Date'].astype(str)

    #remove parenthesis and split the date range into individual rows
    df['Date'] = df['Date'].str.strip('()')
    df['Date'] = df['Date'].str.strip('[]')
    df['Date'] = df['Date'].str.split(',')

    #makes list of dates into individual rows
    df = df.explode('Date')

    #create new column to only cateogrize by month
    df['Date'] = pd.to_datetime(df['Date'], format = '%m/%d/%Y')
    df['Month'] = df['Date'].dt.month
    #convert number of month to word
    df['Month']=df['Month'].replace({1:'January', 2: 'February', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'})
    #reorganized referral
    month_order = ['August', 'September', 'October', 'November', 'December', 'January']
    # Convert the 'Month' column to a categorical data type with the specified order
    df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)
    
    #create bar chart using mathplotlib
    referral_counts = df.groupby(['Month', 'Gender']).size().unstack(fill_value=0)
    referral_counts.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.xlabel('Month')
    plt.ylabel('Number of Referrals')
    plt.title('Number of Referrals by Month and Gender')
    plt.legend(title='Gender')
    #show bar chart
    return(plt.show())

#future goal: have user input a teacher and output graph breakdown of referral type
def teacher_data(df):
    pass

def main():
    df1 = pd.read_csv('behaviorEvents.csv')
    df2 = pd.read_csv('southernGrade.csv')
    df = c.csv_export(df1, df2)
    question = '''Select a number to review referral breakdown. Press Q to quit.
    1. What is the most written type of referral?
    2. For a dress code referrals, is there bias towards a certain group?
    3. How has the number of referrals progressed over time?
    '''
    determine = input(question).upper()
    while determine != 'Q':
        if determine == '1':
            event_type_graph(df)
            determine = input(question)
        elif determine == '2':
            dress_code_bias_gender(df)
            determine = input(question)
        elif determine == '3':
            change_in_referrals_gender(df)
            determine = input(question)
        else:
            print('Invaild input.')
            determine = input(question)
    print('You have quit the program.')

if __name__ == "__main__":
    main()
    