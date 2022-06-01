# southern_hs_referrals

## Overview ##
This project focuses on analyzing referral data from Southern High School. Referrals are 

## The Questions ##
1) What is the most written type of referral? 
2) Which academy has the most referals? 
3) For a specific referral, is there bias towards a certain group?
4) How has the number of referrals progressed over time?
5) How are teachers documenting the situation that consistuted the referral?

## Data Source ##
There are two data sets that were used: behaviorEvents.csv and southernGrades.csv. Both were obtained by JCPS and added to the .gitignore file to align with FERPA. behaviorEvents.csv has the following variables: 
- School,
- Group By,
- Submitted By,
- Event Type,
- Date,
- Student,
- Student Number,
- Grade,
- Role,
- Comments

To obtain the students race, academy, and gender, southernGrades.csv was used. southernGrades.csv has the following variables:
- Grade,
- Last,
- First,
- Student ID,
- Academy,
- Section,
- Class Name,
- Letter Grade,
- Percentage Grade,
- Teacher,
- Race,
- Gender

Two new data sets were created to remove student and teacher identification to align with FERPA.

## Requirements ##
All needed packages can be installed by the requirements.txt file. The following packages are included: 
- pandas
- matplotlib

## Features Included ##

The features included for the Data Anaylsis 2 Project are: 

#### Feature 1: Loading Data ####
- Read two data files in csv

#### Feature 2: Cleaning Data ####
- Clean your data and perform a pandas merge with your two data sets, then calculate some new values based on the new data set.  

#### Feature 3: Visualize/Present Data ####
- Make 3 matplotlib or seaborn (or another plotting library) visualizations to display your data.
- Make a Tableau dashboard to display your data

#### Feature 4: Best Practices ####
- Utilize a virtual environment and include instructions in your README on how the user should set one up
- Build a custom data dictionary and include it either in your README or as a separate document. This will only apply if your data set does not already have a data dictionary or if you’re building a custom data set. For an example, see the resources to the right.

#### Feature 5: Interpretation of your data ####
- Annotate your .py files with well-written comments and a clear README.md (only applicable if you’re not using a jupyter notebook).



