# southern_hs_referrals

## Overview ##
This project focuses on analyzing referral data from Southern High School in Louisville, KY. Referrals are disciplinary tracking systems on student behavior. Teachers and admin indicate the behavior event, student identification, and comments on referrals.

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

A new combined data sets was created to remove student and teacher identification to align with FERPA. A sample data set to run the following functions is provided:

The sample data set is also used to create a Tableau dashboard to display the data.

## Requirements ##
All needed packages can be installed by the requirements.txt file. The following packages are included: 
- pandas
- matplotlib
- seaborn

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

#### Feature 5: Interpretation of your data ####
- Annotate your .py files with well-written comments and a clear README.md.

## Special Instructions ##
1. Run git clone https://github.com/samaguiar/southern_hs_referrals.git to clone repo.

#### MacOS/Unix ####

2. Create a virtual environment: python3 -m venv env
3. Activate virtual environment: source env/bin/activate
4. Install requirements: pip install -r requirements.txt
5. Run the following code to start the program: python3 main.py

#### Windows ####

2. Create a virtual environment: py -m venv env
3. Activate virtual environment: .\env\Scripts\activate
4. Install requirements: py -m pip install -r requirements.txt
5. Run the following code to start the program: py main.py


