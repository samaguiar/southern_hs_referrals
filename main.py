import pandas as pd
import matplotlib.pyplot as plt

def event_type(df):
    event = input('Which referral event do you want to look at?  ')
    df_event = df[df['Event Type']]
    return(df_event)
    #have user input type of violation and show breakdown by gender, race, academy

def teacher_data(df):
    pass
    #have user input a teacher and output graph breakdown of referral type
