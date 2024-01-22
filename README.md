# exploratory-data-analysis---customer-loans-in-finance827

## Description

The goal of this project is to perform comprehensive exploratory data analysis on the customer loans dataframe given in order to improve the company's management of the loans and reduce losses.

This project uses guidelines and a template given by AiCore to develop the analysis. It is split into four milestones to make it readable and manageable for a beginner to follow.

During this project, the core skills and principles of Python are developed and practiced. The skills developed are as follows:

- Object Oriented Programming (OOP)
- Familiarisation with GitHub and Visual Code Studio
- Implementing classes, funtions, methods and data structures

The core skills and principles of SQL and exploratory data analysis (EDA) are also developed and practiced. This includes the following skills:

- Data cleaning
- Data transformation and visualisation
- Statistical analysis

## Installation

Downloading the credentials.yaml file allows a connection to be established with the database. This is needed for the db_utilis.py file to run. 

## Milestone 1

The dev environment and GitHub repository are set up.
GitHub is used to track changes to the code and save them online in a GitHub repo. 


## Milestone 2

This milestone is concerned with extracting the loans data from the cloud. The goal of this milestone is to create the Python classes and code to extract the loans payment from a database in the cloud. This is performed in the file db_utils.py. loan_payments.csv is the file generated from the data extracted by the db_utils.py script and contains the DataFrame.

The following steps are performed:

1. Initialsie a class to extract the data
2. Extract the data from the RDS Database
3. Familiarisation with the data


## Milestone 3

This milestone is concerned with cleaning and performing EDA on the loans data. The goals of this milestone are to gain a deeper understanding of the data and identify any patterns that might exist. 
Missing or incorrectly formatted data is identified and transformed in the Python files datatype_transformations.py, PLotter.py and DataFrameTransform.py. The analysis behind these decisions is delivered in the files datatype_transformations.ipynb and NULL_transformations.ipynb.
Statistical and visualisation techniques are utilised to gain insight on the data's distribution and identify any patterns or trends. This is performed in the Plotter.py and DataFrameTransform.py files. The analysis is present in the file skew_and_outliers_transformations.ipynb.

The following steps are performed:

1. Convert columns to correct format
2. Get information from teh DataFrame.
3. Remove/impute missing values in the data
4. Perform transformations on skewed columns
5. Remove outliers from the data
6. Remove overly correlated columns


## Milestone 4

This milestone is concerned with analysis and visualisaion of the data. The goals of this milestone are to draw deeper insights from the data and identify any patterns or trends not visible in the previous milestones. This analysis is present in the file df_analysis_and_visualisation.ipynb.

The following steps are performed:

1. Visualise the current state of the loans
2. Calculate loss
3. Calculate projected loss
4. Calculate possible loss
5. Present the indicators of loss

## License information

None