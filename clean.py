import pandas as pd
import plotly.express as px


def clean_data(df, df2):
    df = df.drop(columns ='School')
    df = df.drop(columns='Group By')
    df = df.drop(columns='Role')

    df2 = df2.drop(columns='Unnamed: 0')
    df2 = df2.drop(columns='Section')
    df2 = df2.drop(columns='Class Name')
    df2 = df2.drop(columns='Letter Grade')
    df2 = df2.drop(columns='Percentage Grade')
    df2 = df2 = df2.drop(columns='Teacher')

    return(df, df2)